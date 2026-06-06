#!/usr/bin/env node

/**
 * validate-pipeline.js — AI Agent Brain Pipeline Linter
 *
 * Validates the structural integrity of the brain system:
 * 1. All referenced files exist
 * 2. No absolute/hardcoded paths remain in markdown
 * 3. Required directories are present
 * 4. Core pipeline files are intact
 *
 * Usage: node .agent/scripts/validate-pipeline.js
 * Exit code 0 = pass, 1 = failures found
 */

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..', '..');
const errors = [];
const warnings = [];

// --- Helpers ---
function check(condition, msg) {
  if (!condition) errors.push(`❌ ${msg}`);
}

function warn(condition, msg) {
  if (!condition) warnings.push(`⚠️  ${msg}`);
}

function fileExists(relPath) {
  return fs.existsSync(path.join(ROOT, relPath));
}

function readFile(relPath) {
  const full = path.join(ROOT, relPath);
  if (!fs.existsSync(full)) return null;
  return fs.readFileSync(full, 'utf-8');
}

// --- 1. Required Directory Structure ---
console.log('\n🔍 Checking directory structure...');
const requiredDirs = [
  '.agent',
  '.agent/cores',
  '.agent/skills',
  '.agent/workflows',
  '.agent/rules',
  '.agent/ERD',
  '.agent/project-source',
];
for (const dir of requiredDirs) {
  check(fs.existsSync(path.join(ROOT, dir)), `Required directory missing: ${dir}`);
}

// --- 2. Core Pipeline Files Exist ---
console.log('🔍 Checking core pipeline files...');
const requiredCores = [
  '.agent/cores/CORE-00-INTENT-MATRIX.md',
  '.agent/cores/CORE-01-BOOTLOADER.md',
  '.agent/cores/CORE-02-MUTATOR.md',
  '.agent/cores/CORE-03-DISCOVERY.md',
  '.agent/cores/CORE-04-UI-MATHEMATICS.md',
];
for (const core of requiredCores) {
  check(fileExists(core), `Core pipeline file missing: ${core}`);
}

// --- 3. Master Orchestrator Exists ---
console.log('🔍 Checking master orchestrator...');
check(fileExists('.antigravity-agents.md'), 'Master orchestrator .antigravity-agents.md is missing');

// --- 4. No Hardcoded Absolute Paths ---
console.log('🔍 Scanning for hardcoded absolute paths...');
const ABSOLUTE_PATH_REGEX = /[A-Z]:\\[^\s"'`\]]+/g;
const mdFiles = [];

function collectMdFiles(dir) {
  if (!fs.existsSync(dir)) return;
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const entry of entries) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      // Skip node_modules, .git, .next
      if (['node_modules', '.git', '.next', '.serena'].includes(entry.name)) continue;
      collectMdFiles(full);
    } else if (entry.name.endsWith('.md')) {
      mdFiles.push(full);
    }
  }
}
collectMdFiles(ROOT);

for (const file of mdFiles) {
  const content = fs.readFileSync(file, 'utf-8');
  const matches = content.match(ABSOLUTE_PATH_REGEX);
  if (matches) {
    const relFile = path.relative(ROOT, file);
    for (const match of matches) {
      errors.push(`❌ Hardcoded absolute path in ${relFile}: "${match}"`);
    }
  }
}

// --- 5. .gitattributes exists (language classification) ---
console.log('🔍 Checking language classification...');
warn(fileExists('.gitattributes'), '.gitattributes missing — GitHub may misclassify repo language');

// --- 6. IDE integration dotfiles exist ---
console.log('🔍 Checking IDE integration files...');
const ideFiles = ['.cursorrules', '.claude/CLAUDE.md'];
for (const f of ideFiles) {
  warn(fileExists(f), `IDE integration file missing: ${f}`);
}

// --- Results ---
console.log('\n' + '='.repeat(50));
if (errors.length === 0 && warnings.length === 0) {
  console.log('✅ All checks passed! Pipeline is valid.');
  process.exit(0);
} else {
  if (warnings.length > 0) {
    console.log(`\n⚠️  ${warnings.length} warning(s):`);
    warnings.forEach(w => console.log(`  ${w}`));
  }
  if (errors.length > 0) {
    console.log(`\n❌ ${errors.length} error(s):`);
    errors.forEach(e => console.log(`  ${e}`));
    console.log('\n🛑 Pipeline validation FAILED.');
    process.exit(1);
  } else {
    console.log('\n✅ Passed with warnings.');
    process.exit(0);
  }
}
