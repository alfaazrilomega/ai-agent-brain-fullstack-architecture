# 🧠 THE LOCKIN AI WORKFLOW BRAIN BLUEPRINT

This document serves as the authoritative, step-by-step blueprint of the **LockIn AI Workflow Brain**. It maps out the exact sequence from **Phase 00 (Intent)** to **Final Validation (QA)**, highlighting the division between **Design** and **Fullstack** tasks, detailing what the AI analyzes, and specifying the exact questions the AI must ask the user at each gate.

---

## 🗺️ The Core Tracks (The 4-Track System)

Every incoming task must be locked into one of four rigid execution tracks to prevent context drift and focus the Persona Council:

```
Track A: Frontend / UI Only  ──> Cores 00 ──> 01 ──> 02 ──> 03 ──> 04 ──> 05 ──> Visual QA
Track B: Backend / Logical   ──> Cores 00 ──> 01 ──> 02 ──> 03 ─────────> 05 ──> Unit/API QA
Track C: Micro-Surgical Fix  ──> Cores 00 ──> Immediate Code Modification ───────> Quick Lint
Track D: Fullstack Feature   ──> Cores 00 ──> 01 ──> 02 ──> 03 ──> 04 ──> 05 ──> Double QA
```

*   **Track A (Frontend/UI Only):** Visual adjustments, component redesigns. Requires strict UI math validation (**CORE-04**).
*   **Track B (Pure Backend/Logical):** Database, APIs, auth, email, cron jobs. **CORE-04** is strictly locked out.
*   **Track C (Micro-Edit):** Quick typos, trivial CSS color changes, or single-line fixes. Bypasses the cores for direct execution.
*   **Track D (Fullstack):** Features requiring both new schemas and new UI components. Integrates both Frontend and Backend specialist councils.

---

## ⏱️ Step-by-Step Execution Timeline: Cores & Questions

Below is the chronological breakdown of what the AI does behind the scenes, and the **Exact Prompts/Questions** it must output at each gate.

```
┌───────────────┐     ┌───────────────┐     ┌───────────────┐     ┌───────────────┐
│    CORE-00    │ ──> │    CORE-01    │ ──> │    CORE-02    │ ──> │    CORE-03    │
│ Intent/Baton  │     │ Boot/Registry │     │ ERD & Mutator │     │ Stack Discovery│
└───────────────┘     └───────────────┘     └───────────────┘     └───────────────┘
                                                                          │
 ┌────────────────────────────────────────────────────────────────────────┘
 │
 │  [Track A & D Only]
 ▼
┌───────────────┐     ┌───────────────┐     ┌───────────────┐
│    CORE-04    │ ──> │    CORE-05    │ ──> │   VISUAL QA   │
│ UI Math Gate  │     │ TDD/Execution │     │ Browser Verification
└───────────────┘     └───────────────┘     └───────────────┘
```

---

### Phase 00: Intent Matrix & Reference Capture (CORE-00)
**What the AI Analyzes/Does:**
1. Drops its persona as an "AI Agent" and adopts the perspective of the human user.
2. Scans the prompt for keywords to recruit a **Specialist Council** (e.g., DnD, animations, DB, design).
3. Evaluates attached images and links into 4 types: **Type 1** (Clone Target), **Type 2** (Inspiration Gallery), **Type 3** (Asset Source), or **Type 4** (Screenshot + URL Clone Target).
4. Runs `browser_subagent` to capture visual details (colors, computed CSS variables, and timing functions).

**What the AI MUST Ask the User:**
> [!IMPORTANT]
> *   **If a Type 2 Link (Gallery/Discovery site) is detected:** 
>     *"You linked [platform] as inspiration. Could you: (a) link a specific design, or (b) describe the style?"*
> *   **Fidelity Gate (Only if no Type 4 screenshot is provided):**
>     *"Should the UI be **100% pixel-perfect identical** to the reference (I will extract exact hex codes, border radii, font weights, and all animations/scroll effects), or should I use it as **structural inspiration** while applying your own design system?"*

---

### Phase 01: Global Registry Bootloader (CORE-01)
**What the AI Analyzes/Does:**
1. Ingests `.agent/MASTER-INDEX.md` to map available files, rules, and instincts.
2. Ingests all dot-folder rules (`.clinerules`, `.cursorrules`, etc.).
3. Performs a template placeholder validation check (stops if `FEATURES.md` or `ERD/` are unpopulated templates).
4. Runs deep conflict resolution (resolves contradictions between local configurations).

**What the AI MUST Ask the User:**
> [!WARNING]
> *   **If template files are unpopulated:**
>     *"Your `FEATURES.md` [or `ERD/` folder] is still in a template state. Should I generate the features list from your active project files, or will you write it manually?"*
> *   **If rules conflict without clear prompt tiebreakers:**
>     *"Rule A says Tailwind, Rule B says Vanilla CSS. Which one should I follow for this specific task?"*

---

### Phase 02: Context Mutation & Database Modeling (CORE-02)
**What the AI Analyzes/Does:**
1. Deduces database tables (ERD) from explicit requirements + supplementary inferences.
2. Cross-references database changes with environmental constraints.
3. Locks the draft Prisma/PostgreSQL schema.

**What the AI MUST Ask the User:**
> [!CAUTION]
> *   **The Autonomy & Environment Proposal:**
>     *"Based on scale, I recommend [e.g. Supabase + Prisma]. However, what are your hosting and budget constraints? Do you approve this stack, or would you prefer a lighter alternative (e.g. SQLite/cPanel path)?"*
> *   **The Mislead Prevention Warning:**
>     *"I have dynamically generated this database schema (ERD) based on minimal context. Is this aligned with your vision, or should we pivot?"*

---

### Phase 03: Stack & Product Discovery (CORE-03)
**What the AI Analyzes/Does:**
1. Proposes a section-by-section breakdown of every page requested.
2. Verifies capability limits by running the **Proof of Knowledge (PoK) Protocol** (sanitizes if the AI possesses the physical `.md` instruction files locally to execute).
3. Performs a dry-run to catch Next.js Server vs. Client Component collisions (e.g., GSAP/Canvas inside Server Component).

**What the AI MUST Ask the User:**
> [!NOTE]
> *   **Section Layout Proposal:**
>     *"For the [X] page, I propose: [Section 1, Section 2, Section 3, ... (no limit)]. Do you like this breakdown, or should we adjust?"*
> *   **Scale Check:**
>     *"Will this data list have 10 items or 10,000? Do we need pagination or infinite scroll?"*
>     *(Note: If you explicitly request Framer Motion, GSAP, or heavy animation libraries, or we execute under the Awwwards standard, the AI will make the design perfect without caring about 60FPS! Basically, the AI will make it as good and perfect as possible without paying attention to 60FPS. After that, the AI will ask if you are satisfied with the design and then continue making it or upgrading it so that the FPS is not too heavy, or if we need to redesign it.)*

---

### Phase 04: Visual & UI Mathematics (CORE-04) — [DESIGN OR FULLSTACK] (TRUE)
**What the AI Analyzes/Does:**
1. Enforces typographic scales (Scale A Golden Ratio vs. Scale B Minor Third).
2. Sets spacing scales according to the **Riz Ratio (2:3:5)**:
   * `gap-2` (8px) for atom bonds (icon + label)
   * `gap-3` (12px) for molecules (headers)
   * `p-6` (24px) for organisms (cards)
3. Maps W3C standard 3-layer design tokens (Primitive -> Semantic -> Component).
4. Generates layout composition checking the 62/38 split (Golden Ratio layout law).
5. Prepares the official **Atomic Component Breakdown** listing `WHITE_SPACE_RATIO` and `CONTRAST_CHECK`.

**What the AI MUST Ask the User:**
> [!IMPORTANT]
> *   The AI displays the detailed JSON/Markdown Atomic Breakdown of all molecules and atoms, and asks:
>     *"Do you approve this styling and atomic specification, or should we tweak any layout/typography ratios?"*
>
> **Gate Conditions:**
> *   **Design Track:** The AI must wait for the user to explicitly say "GO" before starting code execution.
>   *   **Fullstack Track:** The separate "GO" gate is erased. The AI will wait until all layers (database, api, UI) are covered, or when the fullstack plan is finalized and approved as a whole.

---

### Phase 05: Implementation & Execution (CORE-05)
**What the AI Analyzes/Does:**
1. Converts the approved Atomic Breakdown into high-performance TypeScript components.
2. Applies strict typing (no `any` types).
3. Implements **TDD (Test-Driven Development)**: scaffolds interfaces, writes tests first, and implements minimal code to pass.
4. Executes compile-time validations (`npx tsc --noEmit` and `npm run build` checks).

**What the AI MUST Ask the User:**
*   Normally, the AI runs autonomously in this phase unless a compilation blocker is hit.

---

### Phase 06: Localhost Visual QA & Verification
**What the AI Analyzes/Does:**
1. Launches the browser subagent and navigates to the page on `http://localhost:3001`.
2. Scrolls slowly to test the staggered cascade reveals.
3. Captures 3 distinct screenshots (Above fold, Middle, Bottom grid).
4. Inspects elements in devtools to verify WCAG AA color contrast.
5. Runs `npm run lint`, `npm run build`, and checks for 60fps frame drops in timeline.

**What the AI MUST Ask the User:**
*   Presents the walkthrough document alongside the verified visual proof (screenshots/video) and asks:
    *"Here is the visual proof. The layout is pixel-perfect, passes all contrast checks, lint and build are green. Does this meet your expectations?"*

---

## 🔄 Track-Specific Workflow Routing

### THE DESIGN-FOCUSED WORKFLOW (Tracks A & D)
Whenever a task is classified as **Design-heavy** (visual changes, animations):
1. **Visual QA Priority:** The AI *cannot* report the task as done without uploading real screenshot artifacts of the local site.
2. **Mathematical Layout Enforced:** The UI Mathematics Gate (**CORE-04**) must be passed. Every layout split is validated for φ (Golden Ratio) and Riz spacing rules.
3. **GPU-Safe Animation Guard:** AI is blocked from writing `Framer Motion` elements. Transition curves must be locked to cubic-bezier easing values (`cubic-bezier(0.16, 1, 0.3, 1)`) running only on `transform` and `opacity`.

### THE FULLSTACK/BACKEND WORKFLOW (Tracks B & D)
Whenever a task is classified as **Data-heavy** (database, APIs, data flows):
1. **Pipeline Trace (UI -> API -> DB):** The AI must document the exact path data takes before coding. For example:
   `Prisma Schema (User Table) ──> Route API Handler (api/user/route.ts) ──> React Client Component`
2. **Domain Context Interview:** The AI triggers `INSTINCT-001` to define domain models and constraints.
3. **DB-First Guard:** No frontend UI inputs are built until the database tables, Prisma schema, and migrations are successfully run and tested.
4. **CORE-04 Activation:** Triggered to handle visual alignment of fullstack components. The visual approval is merged with the overall fullstack planning gate.

---

## 👑 The Awwwards-Winning Design Standard (Optional Override)

When the user specifies an **Awwwards standard** or requests a premium redesign, the following strict modifiers override standard design rules:

1. **Expressive Typography Scale:** Enforces **Scale A (Golden Ratio ×1.618)** for highly expressive, editorial layout hierarchies. Large headings are wrapped in fluid CSS `clamp()` calls to ensure perfect scaling across all display viewports.
2. **Enhanced Animation Scope:** 
   - Bypasses the strict 60FPS lock during initial execution! The AI will make the design perfect without caring about 60FPS. Basically, the AI will make it as good and perfect as possible without paying attention to 60FPS. After that, the AI will ask if the user is satisfied with the design and whether to continue making it or upgrading it so that the FPS is not too heavy (optimizing it), or if a redesign is needed.
   - Transition easings must use premium Apple-style curves (`cubic-bezier(0.16, 1, 0.3, 1)`) running strictly on GPU-safe properties (`transform` and `opacity` only).
3. **Increased Breathing Room:** Spacing calculations are adjusted to enforce a negative space ratio of **≥25%** (instead of 20%) to create standard-compliant visual elegance.
4. **W3C Design Token Integration:** Maps bespoke, curated HSL color tokens to local custom variables (avoiding raw Tailwind hex codes) to ensure layout cohesion.
5. **Post-Execution QA:** Forces the verification of `INSTINCT-010-awwwards-design-system` checklist on localhost screenshots, ensuring all buttons bounce softly, layout alignment is mathematically perfect, and there is zero layout thrashing.
