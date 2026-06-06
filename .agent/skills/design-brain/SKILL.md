---
name: design-brain
description: >
  A structured design research protocol that activates whenever the AI is
  about to build, rebuild, change, make, or create any UI/UX. It forces the AI
  to research themes, components, and animations BEFORE writing a single line
  of code, then presents a clear plan for user approval. This is the MAIN
  research path for all design work in the LockIn project.

triggers:
  - keywords: ["rebuild", "redesign", "create", "make", "build", "change", "design", "ui", "ux", "component", "page", "screen", "animate", "animation"]
  - conditions:
      - User requests any visual or UI change
      - AI is about to write or modify any TSX/CSS/HTML component
      - Any slash command: /design-research, /build, /rebuild, /make

context_budget:
  components_max: 10        # Maximum 10 component references collected
  animations_max: 10        # Maximum 10 animation references collected
  extras_max: 5             # Maximum 5 "other" references (3D, scroll effects, etc.)
  total_cap: 25             # Hard cap: never exceed 25 total references
---

# SKILL: Design Brain — Pre-Build Research Protocol

> **CRITICAL RULE:** The AI has absolutely NO right to start writing any UI code before completing ALL phases of this protocol. Every phase must be executed in order. Skipping phases = guaranteed bad design.

---

## 📖 How to Read This Skill

This skill is a **step-by-step playbook**. Read it from top to bottom. Each phase has:
- A clear **GOAL** (what we're trying to figure out)
- **ACTIONS** (what the AI must do)
- A **GATE** (what must be confirmed before moving to the next phase)

---

## PHASE 0 — Context Snapshot (Auto, < 30 seconds)

**GOAL:** Understand what already exists so we don't redesign things that are already good.

**ACTIONS:**
1. Read the project's `design-system.md` (located at `D:\lockincapstone\lockin\design-system.md` or the `.agent` root)
2. Read `RULES.md` to confirm the tech stack, forbidden libraries, and coding conventions
3. Identify the current component that needs changing (read the file if applicable)
4. Note the existing color tokens, font families, and border-radius system

**OUTPUT:** A mental snapshot of:
- Current theme (light? dark? mixed?)
- What's already working vs. what's broken
- What the user's goal is (make it clear in simple language)

**GATE:** ✅ AI knows the existing state before doing anything else

---

## PHASE 1 — Theme & Color Decision

**GOAL:** Lock in the visual direction (palette, mood, vibe) BEFORE looking at components.

**ACTIONS:**

### Step 1A — Ask the User (ALWAYS DO THIS FIRST)
Ask the user the following in simple, non-technical language:

```
🎨 Before I start designing, I need to know a few things:

1. **Light or Dark theme?**
   - Light = clean, minimal, Notion-like (white backgrounds, dark text)
   - Dark = premium, dramatic, Vercel-like (dark backgrounds, glowing accents)
   
2. **Vibe / Mood?** Pick the closest one:
   - 💼 Professional & Clean (corporate, trust-building)
   - 🚀 Bold & Energetic (startup, fast-moving)
   - 🎨 Creative & Expressive (portfolio, artsy)
   - 🧘 Calm & Focused (productivity tool, Notion-like)
   
3. **Accent color?**
   - Keep the current pink (#FF4B72)?
   - Try something new? (tell me what color or mood, e.g. "electric blue", "warm orange")
   - Let AI decide based on vibe?

If you're not sure about any of these, just say "you decide" and I'll make the best call!
```

### Step 1B — AI Decision (If user says "you decide" or doesn't respond)
If the user delegates the decision, the AI must make a concrete choice based on:
- The project's existing `design-system.md` color palette
- The type of content on the screen (dashboard = calm/professional, landing = bold/energetic)
- 2026 SaaS design trends

**Document the decision like this:**
```
🎨 THEME DECISION:
- Canvas: [color + reason]
- Card Surface: [color + reason]  
- Primary Text: [color + reason]
- Muted Text: [color + reason]
- Accent Color: [color + reason]
- Border: [color + reason]
- Shadow Style: [soft/medium/none + reason]
```

**GATE:** ✅ Theme is locked and documented. User has confirmed or AI has made a clear decision.

---

## PHASE 2 — Component & Animation Research

**GOAL:** Gather the best possible references from real design systems BEFORE deciding what to build.

> ⚠️ **IMPORTANT & CRITICAL:** The AI visits these websites ACTUALLY (using the browser tool, not just mentioning them). The AI reads the page, picks specific components, and saves the direct link to each one.
>
> ❌ **CRITICAL: NEVER HALLUCINATE OR GUESS LINKS.** The AI has NO right to output any showcase link to the user unless it has first successfully visited, loaded, and verified that exact URL inside its active browser session. If a link returns a 404 or redirects to a generic index/home page, the AI must search for the correct URL or declare that it is unavailable. Hallucinating unverified links violates the core design research protocol.

### Research Websites (visit IN ORDER):

#### 🌐 SITE 1 — 21st.dev Community Components
```
URL: https://21st.dev/community/components
Purpose: Modern React/Next.js UI components with live demos
What to collect: Any component that matches the user's requirement (buttons, cards, hero sections, inputs, modals, etc.)
Limit: Max 10 components from this site
```

**For each component found:**
- Save the component name
- Save the direct link to the component demo
- Note what it's good for (e.g., "great for KPI metric cards")
- Rate fit: ⭐ (okay) / ⭐⭐ (good) / ⭐⭐⭐ (perfect)

#### 🌐 SITE 2 — SuperDesign UI Library
```
URL: https://app.superdesign.dev/library?category=ui-components
Purpose: Polished, premium UI component library
What to collect: High-quality components that feel premium and Awwwards-worthy
Limit: Max 10 components from this site
```

#### 🌐 SITE 3 — UIverse
```
URL: https://uiverse.io/
Purpose: CSS animations, micro-interactions, creative effects
What to collect: Hover effects, loading states, button animations, card interactions
Limit: Max 10 animations/effects from this site
```

#### 🌐 SITE 4 — ShiftNudge Mosaic Lab (ONLY if user needs interactive background)
```
URL: https://shiftnudge.com/lab/mosaic?mcp_token=eyJwaWQiOjE2NzYxODcsInNpZCI6MTM5Mzg2NTIyLCJheCI6IjZmOTI0YzVjZjYzYmE4N Dc1OWRmNTUyNjRlOTBjZDFmIiwidHMiOjE3NjgxODUzMjcsImV4cCI6MTc3MDYwNDUyN30.V9KhQwQgnDLmQEeDfgf8wL-5YHNdxbyU8ynLkVE4C1E
Purpose: Interactive mosaic/grid background generators from images
When to use: ONLY if user asks for "interactive background", "mosaic effect", "image-based bg", etc.
```

### Research Collection Template

After visiting all relevant sites, organize findings like this:

```
📦 COMPONENT COLLECTION (max 10 per category)

🧩 COMPONENTS:
[1] Component Name — Source: 21st.dev — Link: [URL] — Fit: ⭐⭐⭐ — Use for: [specific placement]
[2] Component Name — Source: SuperDesign — Link: [URL] — Fit: ⭐⭐ — Use for: [specific placement]
... (up to 10)

✨ ANIMATIONS / MICRO-INTERACTIONS:
[1] Animation Name — Source: UIverse — Link: [URL] — Fit: ⭐⭐⭐ — Use for: [specific placement]
[2] Animation Name — Source: UIverse — Link: [URL] — Fit: ⭐⭐ — Use for: [specific placement]
... (up to 10)

🎯 EXTRAS (3D, scroll effects, special FX):
[1] Effect Name — Source: [site] — Link: [URL] — Use for: [specific placement]
... (up to 5)
```

**GATE:** ✅ At least 5 components and 3 animations have been collected with real links

---

## PHASE 3 — Knowledge Preservation & NotebookLM Dump

**GOAL:** Preserve the COMPLETE, FULL research output in external memory — NO information is lost, compressed, or summarized away. The AI runs at FULL performance with complete knowledge retained.

> ⚠️ **CRITICAL RULE — NO COMPRESSION:**
> There is no compression and AI provides complete knowledge at all times to maintain consistency and to prevent wrong answers. The AI itself must dictate and self-regulate its research results. The AI is the authority over what it has found — it does NOT reduce its own knowledge to fit a smaller box.

**ACTIONS:**

### Step 3A — Dump EVERYTHING to NotebookLM (no omissions)
The AI will navigate to:
```
https://notebooklm.google.com/notebook/43be46ed-beaf-4341-b61e-c45d3802b87f?addSource=true
```

And add a new source note containing the **complete, unabridged** research:
```
=== DESIGN BRAIN FULL DUMP ===
Date: [current date]
Project: [project name]
User Goal: [exact user requirement in plain English]

THEME DECISION (full):
[complete Phase 1 output — every color, every reason]

COMPONENT COLLECTION (full — all entries, no limit):
[EVERY component found with source, link, fit rating, and placement note]

ANIMATION COLLECTION (full — all entries, no limit):
[EVERY animation found with source, link, and description]

EXTRAS COLLECTION (full):
[All 3D effects, scroll behaviors, special FX found]

PLACEMENT PLAN (full draft):
[Detailed initial thoughts on where EACH component and animation goes]

CONSTRAINTS & RULES NOTED:
[All forbidden libraries, project-specific rules from RULES.md]
==============================
```

### Step 3B — Self-Dictation (AI asserts its own conclusions)
After dumping to NotebookLM, the AI must dictate its own research conclusions:
- The AI reviews ALL collected data and forms an **authoritative recommendation**
- The AI states clearly: "Based on full research, I conclude that [X components] are the best fit because [reasons]"
- The AI does NOT reduce or hide any findings — every collected item remains accessible
- If there are competing options, the AI presents them ALL, then makes a clear recommendation with reasoning
- NotebookLM acts as the persistent external memory that can be referenced at any time

**GATE:** ✅ Everything is dumped to NotebookLM. AI has stated its full authoritative conclusions. Nothing has been discarded or compressed.

---

## PHASE 4 — Design Blueprint (Built from BOTH Research + CORE Design Pipeline)

**GOAL:** Present the user with a crystal-clear, non-technical explanation of EXACTLY what will be built and where everything goes. This blueprint is constructed from TWO simultaneous sources: (1) the Phase 2 research collection, AND (2) the CORE design pipeline output.

> ### ⚡ CORE Pipeline Integration Rule
> **BEFORE Phase 4 can be written**, the following MUST have happened in parallel:
> 1. Phases 0–3 of this skill run first (Design Brain research)
> 2. **Simultaneously** (at the same time as Phases 0–3), the CORE design pipeline begins:
>    - `CORE-00-INTENT-MATRIX.md` → Intent classification
>    - `CORE-01-BOOTLOADER.md` → Brain loading
>    - `CORE-02-MUTATOR.md` → Context mutation
>    - `CORE-03-DISCOVERY.md` → Library + animation pre-determination
>    - `CORE-04-UI-MATHEMATICS.md` → Visual math (φ ratio, spacing, atomic breakdown)
> 3. **Phase 4 only begins AFTER the CORE pipeline has fully completed**
> 4. The Design Blueprint in Phase 4 is then synthesized from **BOTH**:
>    - The component/animation research from Phase 2 (live web research)
>    - The mathematical, structural, and visual output from the CORE pipeline
> 5. If the CORE pipeline produces a conclusion that contradicts the Phase 2 research, the AI must present both options to the user and ask which to use — NOT silently pick one.

**ACTIONS:**

Create a formatted blueprint that includes ALL of the following (synthesized from research + CORE output):

```
🏗️ DESIGN BLUEPRINT
====================

📐 LAYOUT STRUCTURE:
[Simple diagram using ASCII or text showing where sections go]
Example:
  ┌─────────────────────────────┐
  │ HEADER (greeting + actions) │
  ├──────────────┬──────────────┤
  │  KPI CARDS   │  CHART       │
  └──────────────┴──────────────┘

🎨 COLORS WE'LL USE:
• Background: [hex] — looks like [plain description, e.g. "clean off-white, like a blank notebook"]
• Cards: [hex] — looks like [plain description]
• Text: [hex] — looks like [plain description]
• Accent: [hex] — used ONLY for [specific elements]

🧩 COMPONENTS (with showcase links):
[1] [Component Name]
    → WHERE: [exact location on page, e.g. "the 4 metric boxes at the top"]  
    → WHY: [1 sentence plain reason]
    → SHOWCASE: [direct link so user can see it before approving]
    → SOURCE: [21st.dev / SuperDesign / UIverse]

[2] [Component Name]
    → WHERE: [exact location]
    → WHY: [1 sentence plain reason]
    → SHOWCASE: [direct link]
    → SOURCE: [site]

... (list ALL selected components)

✨ ANIMATIONS (with showcase links):
[1] [Animation Name]
    → WHERE: [exact element — e.g. "KPI cards when hovered", "metric number when it changes"]
    → WHAT IT LOOKS LIKE: [plain language — e.g. "the card gently lifts up and gets a soft glow"]
    → SHOWCASE: [direct link so user can see it]
    → SOURCE: [UIverse / etc.]

[2] [Animation Name]
    → WHERE: [exact element]
    → WHAT IT LOOKS LIKE: [plain language]
    → SHOWCASE: [direct link]
    → SOURCE: [site]

⚠️ WHAT WE WON'T USE (and why):
• Framer Motion — FORBIDDEN by project rules (performance)
• [anything else user said no to or that contradicts RULES.md]

📋 BUILD PHASES (execution order):
Phase 1: [first thing to build] — estimated time: [X minutes]
Phase 2: [second thing] — estimated time: [X minutes]
Phase 3: [polish + animations] — estimated time: [X minutes]
```

**GATE:** ✅ Blueprint is written. User can see every single component, animation, and color choice WITH direct preview links before any code is written.

---

## PHASE 5 — User Approval Gate 🚦

**GOAL:** Get explicit user sign-off before writing a SINGLE LINE of code.

**ACTIONS:**

Ask the user this exact question (in plain language):

```
✋ STOP — Before I build anything, I need your OK!

Here's what I'm planning (see the blueprint above):
[paste the 3-5 bullet compressed summary]

🔗 Quick Preview Links:
• [Component 1 name]: [showcase link]
• [Animation 1 name]: [showcase link]
• [Component 2 name]: [showcase link]
... (list top 5)

📝 My questions for you:
1. Does the COLOR theme look right to you? (light/dark/accent color)
2. Are you happy with the components chosen? Any you want swapped out?
3. Any animations you want removed or added?
4. Anything I missed?

👇 Just reply with:
• "GO" = I'm happy with everything, build it!
• "Change [item]" = swap out a specific component or color
• "Skip [item]" = remove something from the plan
• "Add [thing]" = add something new to the plan
```

**GATE:** 
* **Design-only Track (Track A):** ✅ User has explicitly responded with "GO" or confirmed adjustments before writing code.
* **Fullstack Track (Track D):** ✅ Bypassed/Merged. The standalone "GO" gate is erased and handled under the overall Fullstack planning and approval step in CORE-05.

---

## PHASE 6 — Phased Execution 🏗️

**GOAL:** Build the design in clean, testable phases — NO marathon code dumps.

**RULES FOR EXECUTION:**
1. **ONE phase at a time** — Never write Phase 2 code until Phase 1 is visually confirmed
2. **Screenshot after each phase** — Use the browser tool to capture the result
3. **Awwwards standard execution exception:** Under Awwwards/Premium standards, the AI will make the design perfect without caring about 60FPS! Basically, the AI will make it as good and perfect as possible without paying attention to 60FPS. Focus entirely on achieving ultimate visual perfection during this execution phase.
4. **Never guess** — If unsure about a color, spacing, or component behavior, ask the user first
5. **No forbidden libraries** — Check RULES.md before using any new dependency
6. **Match the blueprint** — If code diverges from the approved blueprint, STOP and flag it

**Phase execution format:**
```
🏗️ EXECUTING PHASE [N]: [Phase Name]
Files being modified:
- [filename]

Changes being made:
- [change 1]
- [change 2]

Screenshot after this phase: [will use browser tool]
Self-critique score: [1-10] — [reason]
```

**After EACH phase:**
1. Take a screenshot via browser tool
2. Run 3-question self-critique:
   - Does it match the approved blueprint? (Y/N)
   - Does it look premium / Awwwards-worthy? (Y/N)
   - Is it responsive on mobile? (Y/N)
3. If any answer is N → FIX IT before moving to next phase

**GATE:** ✅ All phases complete. Final screenshot taken. 3-question self-critique passed.

---

## PHASE 7 — Final Review & Handoff

**GOAL:** Deliver a clean summary of what was built, ask for design feedback, and perform performance tuning if needed.

**Actions:**
1. **Take screenshots that cover EACH change made** — every modified section of the UI must have its own dedicated screenshot. There is no fixed number — the AI takes as many screenshots as there are distinct changes.
2. Write a short plain-language summary for the user explaining what changed and why.
3. **The Design Satisfaction & Optimization Gate:** Ask the user:
   * *"Are you satisfied with the design? Should I continue making it or upgrading it so that the FPS is not too heavy, or do we need to redesign it?"*
4. **Performance Tuning:** If the user approves the layout but wants optimization, proceed to refactor the code (migrating animations to GPU-safe properties `transform`/`opacity` and removing layout reflows) to upgrade the FPS performance so it is not too heavy.
5. Update the `walkthrough.md` artifact with the final results and all screenshots embedded.
6. Ask the user for final handoff sign-off.

---

## ⛔ HARD RULES (Never break these)

| Rule | What it means |
|------|---------------|
| **No code before Phase 5 approval** | Don't write a single `<div>` until the user says GO |
| **No dark theme on light canvas** | ALWAYS check the global CSS before deciding theme |
| **No forbidden libraries** | Check RULES.md — Framer Motion is banned in this project |
| **No hallucinated component links** | Every link must be a real page you actually visited |
| **No one-size-fits-all designs** | Every component choice must be justified for THIS specific user request |
| **Ask, don't assume** | If unsure about user preference, always ask in plain language |
| **Screenshot every phase** | Never declare a phase "done" without visual proof |
| **Self-critique every phase** | Never show a design you wouldn't rate 8+/10 yourself |

---

## 🆘 Fallback: If AI Cannot Access Browser/Websites

If the AI is unable to visit the research websites (network error, browser tool unavailable, etc.):

1. **Notify the user immediately** — "I can't access the design research sites right now. Here's my fallback plan:"
2. **Use known design knowledge** — Reference components from the design system already in the project
3. **Use placeholder links** — Clearly mark them as `[PLACEHOLDER — verify before building]`
4. **Ask the user for component references** — "Can you share any component or design you like? (dribbble link, screenshot, website URL, etc.)"
5. **Document the fallback** — Note that Phase 2 was done from memory, not live research

---

*This skill was created to solve the recurring problem of AI building UIs based on assumptions instead of research, leading to designs that don't match user expectations and requiring multiple costly rebuilds.*
