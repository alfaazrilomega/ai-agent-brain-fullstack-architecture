---
name: design-research
slash: /design-research
description: >
  Triggers the Design Brain pre-build research protocol. Run this BEFORE any
  build/rebuild/make/change task. Forces AI to research themes, collect real
  component and animation references, present a blueprint with live showcase
  links, get user approval, then execute in clean phases.

aliases:
  - /build
  - /rebuild  
  - /make
  - /design

auto-trigger:
  keywords:
    - "rebuild"
    - "redesign"
    - "create a"
    - "make a"
    - "build a"
    - "change the design"
    - "new design"
    - "design the"
    - "animate"
    - "add animation"
---

# Workflow: /design-research

## When to Use This Workflow

Run this workflow **AUTOMATICALLY** (without user explicitly typing `/design-research`) whenever any of the following happen:

- User says: "rebuild", "redesign", "change the UI", "create a page", "make a component", "build a dashboard", "animate this"
- AI is about to modify ANY `.tsx`, `.css`, or `.html` file that affects visual output
- AI is about to write any new UI component from scratch

> ⚠️ **If you skip this workflow and write code first, you are violating the Design Brain protocol. Stop immediately and restart from Phase 0.**

---

## Step 1 — Load the Design Brain Skill

Read and internalize the full SKILL before doing ANYTHING else:

```
SKILL Location: ./.agent/skills/design-brain/SKILL.md
```

Follow the skill's 7 phases in order, with this critical timing rule:

```
Phase 0:  Context Snapshot (read existing design system)
Phase 1:  Theme & Color Decision → ask user
Phase 2:  Component & Animation Research → visit live sites
Phase 3:  Full Knowledge Dump to NotebookLM → NO compression, AI self-dictates
          ↕ [SIMULTANEOUSLY during Phases 0–3, begin the CORE pipeline below]
          ↕  CORE-00 → CORE-01 → CORE-02 → CORE-03 → CORE-04
          ↓ [Phase 4 can ONLY start after BOTH Phase 3 AND CORE-04 are done]
Phase 4:  Design Blueprint → synthesized from Phase 2 research + CORE pipeline output
Phase 5:  ✋ User Approval Gate → HARD STOP, wait for "GO"
Phase 6:  Phased Execution → one phase at a time, screenshot after EACH change
Phase 7:  Final Review → screenshots for EVERY individual change made
```

> **Key Rules:**
> - AI runs at FULL performance — no knowledge compression at any point
> - CORE pipeline and Design Brain Phases 0–3 run in parallel (simultaneously)
> - Phase 4 blueprint is built from BOTH sources combined
> - Screenshots in Phase 7 cover EACH change, not a fixed count

---

## Step 2 — Research Sites Cheat Sheet

```
🌐 Components:
  - 21st.dev:       https://21st.dev/community/components
  - SuperDesign:    https://app.superdesign.dev/library?category=ui-components

🎭 Animations:
  - UIverse:        https://uiverse.io/

🖼️ Interactive Backgrounds (only if needed):
  - ShiftNudge:     https://shiftnudge.com/lab/mosaic?mcp_token=eyJwaWQiOjE2NzYxODcsInNpZCI6MTM5Mzg2NTIyLCJheCI6IjZmOTI0YzVjZjYzYmE4N Dc1OWRmNTUyNjRlOTBjZDFmIiwidHMiOjE3NjgxODUzMjcsImV4cCI6MTc3MDYwNDUyN30.V9KhQwQgnDLmQEeDfgf8wL-5YHNdxbyU8ynLkVE4C1E

📓 NotebookLM (external memory dump):
  - https://notebooklm.google.com/notebook/43be46ed-beaf-4341-b61e-c45d3802b87f?addSource=true
```

---

## Step 3 — Context Budget Limits

```
🧩 Components collected:   MAX 10
✨ Animations collected:   MAX 10
🎯 Extras collected:       MAX 5
────────────────────────────────
📦 TOTAL CAP:              MAX 25
```

Do NOT go over these limits. Quality over quantity — only collect what you will actually use.

---

## Step 4 — Hard Gates (cannot skip)

| Gate | What blocks progress |
|------|----------------------|
| Phase 1 → Phase 2 | Theme must be confirmed (by user or AI decision) |
| Phase 2 → Phase 3 | At least 5 components + 3 animations collected with real links |
| Phase 3 → Phase 4 | Context has been refreshed (compressed to 3-5 bullets) |
| Phase 4 → Phase 5 | Blueprint written with ALL showcase links included |
| Phase 5 → Phase 6 | **User has explicitly said "GO" or confirmed adjustments** |
| Phase 6 → Phase 7 | All execution phases done with screenshots taken |

---

## Step 5 — Output Format for User

When presenting the plan to the user (Phase 4 + 5), always use this structure:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧠 DESIGN BRAIN RESEARCH COMPLETE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 What you asked for (plain English):
[user request restated simply]

🎨 Theme Decision:
[colors with plain language descriptions]

🧩 Components I'll use:
[numbered list with showcase links]

✨ Animations I'll use:
[numbered list with showcase links + plain descriptions]

📐 Layout Plan:
[ASCII diagram]

✋ DO YOU APPROVE THIS PLAN?
Reply: "GO" to build / "Change [thing]" to swap something
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Fallback Protocol

If browser/internet access is unavailable:
1. Say so clearly to the user
2. Ask user to share reference links, screenshots, or design inspiration
3. Use existing project design system as fallback reference
4. Mark all decisions as `[from-memory — verify]` so user knows
5. Continue with Phases 4-7 as normal, just with memory-based references

---

*Created: 2026-06-03 — LockIn Project Design Brain System*
*Skill: ./.agent/skills/design-brain/SKILL.md*
