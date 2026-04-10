# Academy Hub Dashboard — Redesign Proposal

## Design Principles

1. **Every element earns its space.** If it doesn't help you triage, reference, or prep, it goes.
2. **Show state, not structure.** The dashboard should reflect what's happening now — not explain how the system works.
3. **Stakeholder-legible without narration.** A clean layout and clear labels orient a visitor. Prose descriptions of the interface do not.

---

## Proposed Structure: 3 Views

### 1. Home (replaces Overview + Recent Updates + Workflow)

The landing page answers: **"What needs my attention, and what's current?"**

**What's on it:**

- **Header:** "Postman Academy" with tagline. No paragraph explaining the two programs — the nav labels do that.

- **Recent Product Updates (top of page, prominent):** The update feed from #product-updates, displayed as a compact table. Each row shows date, feature name, description, affected module tags. This is the most operationally useful content in the entire dashboard — it moves from last nav item to the first thing you see.

- **Module Impact Summary (inline with updates):** A small sidebar or row of chips showing which modules have been touched by recent updates, color-coded by sensitivity. Replaces the static "12 modules / 3 high sensitivity" stat cards with something that actually changes and means something. Think: "M08 ×3, M09 ×2, M05 ×1" — a glanceable heatmap of where churn is concentrated.

- **How This Stays Current (collapsed section, bottom):** A lightweight, collapsible section with the 6-step workflow and the two automated task statuses. Closed by default. There for onboarding someone to the system, but not taking daily screen real estate.

**What's removed:**
- The three big stat cards (12, 10, 12) — static counts with no operational value
- The sensitivity distribution bar chart — it visualizes 3 numbers that never change
- The "Automated Systems" panel with hardcoded "Active" badges
- All descriptive prose that narrates the interface

---

### 2. Bootcamp Modules (refined)

The reference view answers: **"What does this module cover, and is it current?"**

**What changes:**

- **Remove the subheading** "12 topic-based modules, each self-contained with slides, speaker notes, activities, and tracked feature dependencies." — the cards demonstrate this.

- **Keep** the sensitivity filter pills and the "Open Bootcamp Slides" link. These are useful.

- **Add a subtle "recently affected" indicator** on module cards that were touched by product updates in the last 2 weeks. A small dot or timestamp like "Updated: Apr 8" connects the home view's update feed to this reference view.

- **Module detail view stays mostly as-is** — it's the strongest part of the current dashboard. Minor cleanup: tighten the V11/V12 slides grid (does V11 still need equal billing?), and consider whether "When to Update" is useful per-module or if the sensitivity badge already communicates that.

**What's removed:**
- The descriptive paragraph under the page title

---

### 3. P4P Sessions (refined)

The catalog view answers: **"What sessions exist and how do people book them?"**

**What changes:**

- **Keep** the session cards, category badges, "NEW" tags, and the "Book a P4P Session" link. All useful.

- **Remove the subheading** "Just-in-time upskilling sessions employees can book anytime..." — the booking link communicates this.

- **Announcement Cadence → collapsed section** at the bottom, similar to the workflow section on Home. Label it "Promotion & Cadence" — useful reference for how sessions get announced, but not daily-use.

**What's removed:**
- Descriptive paragraph under page title
- Announcement Cadence as a prominent grid (moves to collapsed section)

---

## What Gets Cut Entirely

| Current Element | Why It Goes |
|---|---|
| Overview stat cards (12, 10, 12) | Static numbers with no signal |
| Sensitivity distribution bar chart | Visualizes 3 unchanging values |
| Automated Systems "Active" badges | Hardcoded, not connected to real state |
| Workflow page (as standalone) | Becomes a collapsed section on Home |
| Announcement Cadence grid (as prominent) | Becomes a collapsed section on P4P |
| All "here's what you're looking at" prose | The interface should speak for itself |

---

## What Gets Added

| New Element | Why It Earns Space |
|---|---|
| Module impact chips/heatmap on Home | Shows where product churn is concentrated — the key triage signal |
| "Recently affected" indicators on module cards | Connects updates to content without requiring you to cross-reference pages |
| Collapsible "How This Stays Current" on Home | Preserves workflow info for onboarding without daily clutter |
| Collapsible "Promotion & Cadence" on P4P | Preserves announcement schedule as reference |

---

## Navigation Change

**Before (5 items):**
Overview → Bootcamp Modules (12) → Postman for Postmanauts (10) → Update Workflow → Recent Product Updates (12)

**After (3 items):**
Home → Bootcamp Modules (12) → P4P Sessions (10)

Cleaner, and every page has a clear job. The counts next to Modules and Sessions are still useful — they tell a stakeholder the scope at a glance.

---

## Open Questions

1. **V11 references** — The module detail view gives V11 and V12 slides equal billing in a 3-column grid. Is V11 still actively used, or should it be de-emphasized/removed?

2. **"When to Update" field** — Each module has a text field explaining when it needs updating. With the sensitivity badge and the new "recently affected" indicators, is this still pulling its weight in the detail view?

3. **Search** — With 12 modules and 10 sessions, search isn't critical yet. But if the catalog grows, should we plan for a filter/search input?
