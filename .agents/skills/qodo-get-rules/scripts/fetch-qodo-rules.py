#!/usr/bin/env python3
"""
Fetch Qodo coding rules for the current repository.

This script is designed to work cross-platform (Windows, macOS, Linux).
On Windows, it automatically detects Python using: py -3, python3, python (in that order).
"""

import json
import os
import sys
import subprocess
import uuid
import urllib.parse
from pathlib import Path


def log(stmt, file=sys.stderr):
    """Print status messages to stderr."""
    print(f":: {stmt}", file=file)


def error(message, exit_code=1):
    """Print error message and exit."""
    print(f"❌ Error: {message}", file=sys.stderr)
    sys.exit(exit_code)


def warn(message):
    """Print warning message."""
    print(f"⚠️  Warning: {message}", file=sys.stderr)


def info(message):
    """Print info message."""
    print(f"ℹ️  {message}", file=sys.stderr)


def detect_python():
    """Find an available Python interpreter."""
    # Try common commands in order
    commands = ["py -3", "python3", "python"]

    for cmd in commands:
        try:
            # Check if command exists by running --version
            result = subprocess.run(
                cmd.split() + ["--version"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                log(f"Using Python: {cmd}")
                return cmd.split()
        except (subprocess.TimeoutExpired, FileNotFoundError):
            continue

    error("Python not found. Please install Python 3.6+ and ensure it's in your PATH.")


def find_git_root():
    """Find the root directory of the current git repository."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            return Path(result.stdout.strip())
        else:
            error("Not in a git repository", 0)
    except subprocess.TimeoutExpired:
        error("Git command timed out", 0)
    except FileNotFoundError:
        error("Git is not installed or not in PATH", 0)


def get_git_remote_url():
    """Get the origin remote URL from git."""
    try:
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            # No origin remote - exit silently per spec
            log("No origin remote found")
            sys.exit(0)
    except subprocess.TimeoutExpired:
        error("Git remote command timed out", 0)


def parse_repo_scope(url):
    """Parse git remote URL to extract org/repo scope."""
    # SSH: git@github.com:org/repo.git
    # HTTPS: https://github.com/org/repo.git
    import re

    # Try SSH format
    ssh_match = re.match(r'git@github\.com[:/](?P<path>.+?)(?:\.git)?$', url)
    if ssh_match:
        path = ssh_match.group('path')
        return f"/{path}/"

    # Try HTTPS format
    https_match = re.match(r'https://github\.com/(?P<path>.+?)(?:\.git)?/?$', url)
    if https_match:
        path = https_match.group('path')
        return f"/{path}/"

    error(f"Could not parse git URL: {url}")


def detect_module_scope(repo_scope, git_root, cwd):
    """Check if current directory is inside modules/* and adjust scope."""
    # Get relative path from git root to current directory
    try:
        rel_path = cwd.relative_to(git_root)
        parts = rel_path.parts

        if len(parts) >= 2 and parts[0] == "modules":
            # Inside a module - module name is first subdirectory
            module_name = parts[1]
            # Scope becomes: /org/repo/modules/{module_name}/
            base_scope = repo_scope.rstrip('/')
            return f"{base_scope}/modules/{module_name}/"

        return repo_scope
    except ValueError:
        # cwd not under git root (shouldn't happen)
        return repo_scope


def load_config():
    """Load Qodo configuration from ~/.qodo/config.json."""
    config_path = Path.home() / ".qodo" / "config.json"

    if not config_path.exists():
        error(
            "Qodo configuration not found.\n"
            "Please create ~/.qodo/config.json with:\n"
            '{"API_KEY": "your-api-key", "ENVIRONMENT_NAME": "production"}'
        )

    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
    except json.JSONDecodeError as e:
        error(f"Invalid JSON in config file: {e}")

    # Validate required fields
    if 'API_KEY' not in config:
        error("Config missing required field: API_KEY")

    return config


def construct_api_url(config):
    """Construct the API URL from config."""
    if 'QODO_API_URL' in config:
        # Use custom URL (append /rules/v1)
        base_url = config['QODO_API_URL'].rstrip('/')
        return f"{base_url}/rules/v1"
    else:
        # Use ENVIRONMENT_NAME-based construction
        env_name = config.get('ENVIRONMENT_NAME', '')
        if not env_name:
            # Default to production
            return "https://qodo-platform.qodo.ai/rules/v1"
        else:
            return f"https://qodo-platform.{env_name}.qodo.ai/rules/v1"


def generate_request_id():
    """Generate a UUID for request tracking."""
    return str(uuid.uuid4())


def fetch_rules_page(api_url, api_key, request_id, trace_id, encoded_scope, page, page_size=50):
    """Fetch a single page of rules from the API."""
    import urllib.request

    # Build URL with query parameters
    params = {
        'scopes': encoded_scope,
        'state': 'active',
        'page': page,
        'page_size': page_size
    }
    url = f"{api_url}/rules?{urllib.parse.urlencode(params)}"

    # Prepare headers
    headers = {
        'Authorization': f"Bearer {api_key}",
        'request-id': request_id,
        'qodo-client-type': 'skill-qodo-get-rules',
        'Accept': 'application/json'
    }
    if trace_id:
        headers['trace_id'] = trace_id

    # Make request
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as response:
            if response.status == 200:
                return json.loads(response.read().decode('utf-8'))
            else:
                # Handle different error statuses
                error_msg = f"API error: HTTP {response.status}"
                if response.status == 401:
                    error_msg = "Invalid or expired API key (401)"
                elif response.status == 403:
                    error_msg = "Access forbidden (403) - check permissions"
                elif response.status == 404:
                    error_msg = "Endpoint not found (404) - check ENVIRONMENT_NAME"
                elif response.status == 429:
                    error_msg = "Rate limit exceeded (429) - please wait and retry"
                elif 500 <= response.status < 600:
                    error_msg = f"Server error ({response.status}) - API temporarily unavailable"

                error(error_msg)
    except urllib.error.URLError as e:
        error(f"Failed to connect to API: {e.reason}")
    except TimeoutError:
        error("API request timed out")
    except json.JSONDecodeError as e:
        error(f"Invalid JSON response from API: {e}")


def fetch_all_rules(api_url, api_key, request_id, trace_id, encoded_scope):
    """Fetch all pages of rules."""
    all_rules = []
    page = 1
    max_pages = 100

    while page <= max_pages:
        data = fetch_rules_page(api_url, api_key, request_id, trace_id, encoded_scope, page)

        rules = data.get('rules', [])
        all_rules.extend(rules)

        # Check if this was the last page (less than page_size results)
        if len(rules) < 50:
            break

        page += 1

    if page > max_pages:
        warn(f"Reached safety limit of {max_pages} pages. Some rules may be missing.")

    return all_rules


def format_rules_output(repo_scope, query_scope, rules):
    """Format rules for output to stdout."""
    total_count = len(rules)

    # Header
    print(f"# 📋 Qodo Rules Loaded\n")
    print(f"Scope: `{query_scope}`")
    print(f"Rules loaded: **{total_count}** (universal, org level, repo level, and path level rules)\n")
    print("These rules must be applied during code generation based on severity:\n")

    if total_count == 0:
        print("---")
        return

    # Group by severity
    error_rules = [r for r in rules if r.get('severity') == 'error']
    warning_rules = [r for r in rules if r.get('severity') == 'warning']
    recommendation_rules = [r for r in rules if r.get('severity') == 'recommendation']

    # ERROR section
    if error_rules:
        print(f"## ❌ ERROR Rules (Must Comply) - {len(error_rules)}\n")
        for rule in sorted(error_rules, key=lambda r: r.get('name', '')):
            name = rule.get('name', 'Unnamed Rule')
            category = rule.get('category', 'general')
            description = rule.get('description', 'No description')
            print(f"- **{name}** ({category}): {description}")
        print()

    # WARNING section
    if warning_rules:
        print(f"## ⚠️  WARNING Rules (Should Comply) - {len(warning_rules)}\n")
        for rule in sorted(warning_rules, key=lambda r: r.get('name', '')):
            name = rule.get('name', 'Unnamed Rule')
            category = rule.get('category', 'general')
            description = rule.get('description', 'No description')
            print(f"- **{name}** ({category}): {description}")
        print()

    # RECOMMENDATION section
    if recommendation_rules:
        print(f"## 💡 RECOMMENDATION Rules (Consider) - {len(recommendation_rules)}\n")
        for rule in sorted(recommendation_rules, key=lambda r: r.get('name', '')):
            name = rule.get('name', 'Unnamed Rule')
            category = rule.get('category', 'general')
            description = rule.get('description', 'No description')
            print(f"- **{name}** ({category}): {description}")
        print()

    # End marker
    print("---")


def main():
    """Main entry point."""
    # Get current working directory
    cwd = Path.cwd().resolve()

    # Step 1: Find git root
    git_root = find_git_root()
    log(f"Git root: {git_root}")

    # Step 2: Get origin remote URL and parse scope
    remote_url = get_git_remote_url()
    log(f"Remote URL: {remote_url}")

    repo_scope = parse_repo_scope(remote_url)
    log(f"Repository scope: {repo_scope}")

    # Step 3: Check for module-level scope
    query_scope = detect_module_scope(repo_scope, git_root, cwd)
    if query_scope != repo_scope:
        log(f"Module scope detected: {query_scope}")

    # Step 4: Load config
    config = load_config()
    api_key = config['API_KEY']
    env_name = config.get('ENVIRONMENT_NAME', '')
    custom_url = config.get('QODO_API_URL')

    log(f"Environment: {env_name if env_name else 'production (default)'}")

    # Step 5: Construct API URL
    api_url = construct_api_url(config)
    log(f"API URL: {api_url}")

    # Step 6: Generate request ID and get trace ID
    request_id = generate_request_id()
    trace_id = os.environ.get('TRACE_ID', '')

    # Step 7: Encode scope for URL
    encoded_scope = urllib.parse.quote(query_scope, safe='')

    # Step 8: Fetch all rules
    log("Fetching rules...")
    rules = fetch_all_rules(api_url, api_key, request_id, trace_id, encoded_scope)

    # Step 9: Output formatted rules
    format_rules_output(repo_scope, query_scope, rules)


if __name__ == "__main__":
    main()
