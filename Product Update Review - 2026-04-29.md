# Weekly Product Update Review — 2026-04-22 to 2026-04-29

**Generated:** 2026-04-29
**Sources scanned:** #product-updates (C08SPKCGZQ8)
**Programs checked:** Fundamentals Bootcamp (12 modules), API 101 (4 modules), API 201 — Advanced (4 modules)
**Updates found:** 10 product updates in the 7-day lookback
**Unscaffolded programs:** none
**Coverage gaps detected:** 6

---

## Coverage Gaps (Features Not Taught Anywhere)

> Features mentioned in this week's updates that are **not** listed in any module's `postman_features` across any program.

- **Datasets** — New first-class data layer for collection runs, mocks, scripts, and automation (Stage 2 beta, internal-only this week). No module mentions Datasets. The closest signal is the `"Data file handling updates"` trigger in **201-04 (Integration Testing)**, but no module's `postman_features` list contains "Datasets". → **Suggested home: 201-04 (Integration Testing)** as a hands-on data-driven runs section, or a new dedicated module once GA.
- **SpecHub / Specification Version Tagging** — Pinning meaningful versions of OpenAPI/AsyncAPI/GraphQL/Protobuf/Smithy specs from the changelog. No module lists "SpecHub" — **M04 (API Design)** lists `"OpenAPI spec support"` which is the closest, and the V12 facilitator guide (Drive) covers Specs editing and governance but not version tagging. → **Suggested home: M04**.
- **Performance Testing / System Metrics** — Stage 2 beta capabilities for performance runs (CPU/memory tracking on the load generator, persisted historical debug data). No module covers performance testing at all. → **Suggested home: 201-04 (Integration Testing and CI/CD)** as an optional advanced section, or a future 201-05 module.
- **Components (Common Components)** — Permissions for Common Components changed this week (Developer role → view-only; edits require Governance Manager). No module lists "Components" in `postman_features`. **M11 (Lifecycle & Governance)** has `"Governance rules"` and `"Full lifecycle tooling"` but Components are never named. → **Suggested home: M11**.
- **Monitors** — Multiple modules list `"Scheduled Runs"` (101-03, 201-04) but **none list "Monitors" by name**. This week's "Monitor Published Reports" GA exposes a customer-facing artifact (public status-page URL) that is squarely in our teaching scope. → **Suggested home: 101-03 (Testing APIs) or 201-04 (Integration Testing)**.
- **Libraries (top-level construct)** — Stage 2 beta; brand-new umbrella for shared assets (packages, components, etc.). 101-03 and 201-04 list `"Package Library"` but not "Libraries" as a top-level concept. → **Watch-list — do not teach until GA.**

> Six gaps — above the `alert_threshold: 3` configured in `sources.yaml`. Recommend a coverage-planning conversation before next sync.

---

## Proposed Changes (Needs Your Approval)

### 1. Update to Component Library Access — Impact: Medium
**Date:** 2026-04-29 | **Stage:** GA (release post; "stage" field reads "Not relevant in this context") | **Plans:** Enterprise | **Source:** #product-updates
**Summary:** Developers (`TEAM_USER`) now have **view-only** access to Common Components. Creating, editing, publishing, and deleting components now requires the `TEAM_API_GOVERNANCE_MANAGER` role. Postman is tightening control over centrally-curated shared components.
**Demo:** _(no demo link in original post)_

**Affected Modules (all programs):**

- [ ] **M11 — API Lifecycle & Governance (Bootcamp):** Add a beat under Governance rules explaining that Common Components have a dedicated permission boundary now: who can publish vs. who can consume. Reinforces the "centrally curated" framing.
  - _Drive check:_ Not deeply checked — M11 doesn't currently teach Components by name; this is more of a coverage-gap fill than a correction.
- [ ] **201-03 — Publishing and Managing Internal APIs (201):** Touches Role-Based Access Control. Worth a one-line callout that a new role surface (`TEAM_API_GOVERNANCE_MANAGER`) gates component edits.
  - _Drive check:_ Not checked — module postman_features lists RBAC but not Components.

**Proposed hub data change:** Add to `MONTHLY_DIGEST` for May 2026 — "Common Components permission tightening (Apr 29)."
**Your decision:** Approve / Modify / Skip

---

### 2. Slack Channel Integration for Partner Workspaces — Impact: Medium
**Date:** 2026-04-28 | **Stage:** 7 (GA) | **Plans:** Enterprise, Team | **Source:** #product-updates
**Summary:** Partner Workspaces can now be connected to Slack channels by an admin/editor. External Slack users invited to that channel see workspace updates. Useful for partner-facing API portals where external developers want a feed of changes.
**Demo:** https://www.loom.com/share/8333182089c740e88e57f03bcb7c0999

**Affected Modules (all programs):**

- [ ] **M10 — Hands-On Lab — The Grocery Store (Bootcamp):** Lists `"Partner Workspaces"` in postman_features. One-line addition under the Partner Workspaces beat: "External partners can also subscribe to workspace updates via a connected Slack channel."
  - _Drive check:_ Not pulled (M10 has no `drive_sources` — it's the New Hire Refresh Guide referenced in `reference_docs`).
- [ ] **101-02 — Documenting APIs (101):** Lists `"Partner Workspaces"` and is the natural place for partner-portal teaching. Add a sentence in the Partner Workspaces section noting the Slack channel option for external visibility.
  - _Drive check:_ Not pulled this run; recommend reading IG `1S0Wq0dGYvNOCieZFUBL7jsRjx-E9j-ae` before applying.

**Proposed hub data change:** Add `MONTHLY_DIGEST` entry for May 2026 — "Slack channel integration for Partner Workspaces (Apr 28)."
**Your decision:** Approve / Modify / Skip

---

### 3. Invite Git Collaborators to Workspaces (Local Mode) — Impact: Medium
**Date:** 2026-04-27 | **Stage:** 7 (GA) | **Plans:** Free, Solo, Team, Enterprise | **Source:** #product-updates
**Summary:** When working in a Local Mode workspace backed by a Git repo, Postman now surfaces existing Git collaborators as suggested invites — both in the Files Setup Guide and the Invite to Workspace modal ("Suggested from Git" section). Cuts out the manual "find their email" step.
**Demo:** _(no demo link in original post)_

**Affected Modules (all programs):**

- [ ] **M06 — Git & Version Control (Bootcamp):** Lists `"Native Git integration"`. Add a one-liner where we set up the local-mode workspace: "Postman suggests your Git collaborators when you go to invite teammates — fewer Slack DMs asking for email addresses."
  - _Drive check:_ ✅ Read **"What's New in Postman V12 (Facilitator Guide)"**. The guide walks through creating a Git-backed Local Mode workspace and pushing/pulling but **does not currently demo the "Suggested from Git" invite flow**. Slides reference the old workflow — needs a small addition during the Git Integration / Cloud Sync section.
- [ ] **M07 — Developer Experience (Bootcamp):** Lists `"Workspace collaboration"`. Optional mention; lower priority than M06.
- [ ] **M09 — Postman Platform (Bootcamp):** Lists `"Native Git"` and `"Local Mock Servers"` (Local Mode adjacent). One-line awareness mention.

**Proposed hub data change:** Add `MONTHLY_DIGEST` entry for May 2026 — "Git-suggested invites in Local Mode workspaces (Apr 27)."
**Your decision:** Approve / Modify / Skip

---

### 4. Specification Version Tagging in SpecHub — Impact: Medium
**Date:** 2026-04-27 | **Stage:** GA (release post; "stage" field reads "Not relevant in this context") | **Plans:** Free, Solo, Team, Enterprise | **Source:** #product-updates
**Summary:** Pin meaningful versions of API specs from the SpecHub changelog (e.g. `v1.0.0`, `v2.0-beta`). Tagged versions show as labeled badges, snapshot views are shareable URLs, and outline navigation reflects the tagged version. Public APIs allow programmatic create/list/fetch of tags. Supports OAS 2.0/3.0/3.1, AsyncAPI 2.0, GraphQL, Protobuf, Smithy.
**Demo:** _(no demo link in original post)_

**Affected Modules (all programs):**

- [ ] **M04 — API Design & Architecture (Bootcamp):** Lists `"OpenAPI spec support"`. Add a beat under spec management: "SpecHub now lets you pin tagged versions like `v1.0.0` and revisit the snapshot — useful before a breaking change."
  - _Drive check:_ ✅ Read **"What's New in Postman V12 (Facilitator Guide)"**. Covers Spec editing and governance violations but **does not mention version tagging at all**. Slides reference the old workflow — needs a new short beat in the Spec Editing section.

**Proposed hub data change:** Add `MONTHLY_DIGEST` entry for May 2026 — "Specification Version Tagging in SpecHub (Apr 27)." Consider adding "SpecHub" to M04's `postman_features` list.
**Your decision:** Approve / Modify / Skip

---

### 5. Monitor Published Reports (Stage 7 / GA) — Impact: Medium
**Date:** 2026-04-24 | **Stage:** 7 (GA) | **Plans:** Solo, Team, Enterprise | **Source:** #product-updates
**Summary:** Publish a monitor report to a public, read-only URL — like a lightweight status page. Includes success rates, recent execution history, failure insights, and request-level perf metrics. Stage 7 brings standardized URLs, Postman branding, EU domain parity, and Enterprise approval workflows.
**Demo:** https://www.loom.com/share/d37b22f36c364ee889027e7ef03f3e9d

**Affected Modules (all programs):**

- [ ] **101-03 — Testing APIs (101):** Lists `"Scheduled Runs"`. Could extend the scheduled-runs section with a 30-second mention of publishing the report externally.
  - _Drive check:_ ✅ Read IG (Drive ID `1YleLx6XFSe7uE5yZdPKOO4PgvJ3DRnHf`). Currently ends with "Schedule a run with the Collection Runner" — **does not cover monitors or published reports**. Slides reference old workflow.
- [ ] **201-04 — Integration Testing and CI/CD (201):** Lists `"Scheduled Runs"`. The natural home for "communicate API reliability with external stakeholders." Add a section on monitor reports + public sharing.
  - _Drive check:_ Not pulled this run; recommend reading IG `1YxtAB0IV5a2EiLyeEGJ74Q-p3egKsBLA` before applying.
- [ ] **M11 — API Lifecycle & Governance (Bootcamp):** Lists `"Insights"`. Light awareness mention — published monitor reports tie into the broader observability story.

**Proposed hub data change:** Add `MONTHLY_DIGEST` entry for May 2026 — "Monitor Published Reports GA (Apr 24)." Consider adding `"Monitors"` to 101-03 and 201-04 `postman_features` lists.
**Your decision:** Approve / Modify / Skip

---

## No Action Needed

These updates are either informational, admin-only, or beta features we shouldn't teach yet.

- **Partner Manager Support for User Groups** (2026-04-28, GA, Enterprise) — Admin permission management. Not teaching-relevant. Skip.
- **New SDK languages: Rust, Kotlin, Ruby** (2026-04-23, GA, Team/Enterprise) — SDK-Gen now covers 10 languages. **M09 already lists `"SDK Distribution"`** — content remains accurate, no edit required. Optional one-line update if M09 ever enumerates languages.
- **Library Menu added to status bar** (2026-04-22, **Stage 2 beta**, Free/Solo/Team) — New "Libraries" top-level construct. Coverage-gap candidate, but **flag for awareness only — do not update modules until GA**.
- **System Metrics & Historical Debug Data Persistence for Performance Runs** (2026-04-22, **Stage 2 beta**, Solo/Team/Enterprise) — Performance testing observability. Coverage gap (no module covers performance testing), but **don't add until GA**.
- **Datasets in Local Mode** (2026-04-22, **Stage 2 beta**, Solo/Team — internal-only) — New first-class data layer. Coverage gap, but **don't add until GA / external availability**.

---

## Drive Verification Notes

| Update | Drive doc read | Verdict |
|---|---|---|
| Git Collaborators (Local Mode) | What's New in Postman V12 (Facilitator Guide) — `1GFnZXgZZhTFRVn5UnHvhCvkz_zQGgYDbGc9ZyHsdqts` | Slides reference old workflow — needs update |
| Specification Version Tagging | What's New in Postman V12 (Facilitator Guide) — same doc as above | Slides reference old workflow — needs new beat |
| Monitor Published Reports | 103 — Testing APIs (IG) — `1YleLx6XFSe7uE5yZdPKOO4PgvJ3DRnHf` | Slides cover Scheduled Runs only — Monitors / publishing missing |

Other Medium-impact updates were not deep-verified against Drive this run (Slack-for-Partner-Workspaces, Components permissions). Recommend pulling the relevant IGs before applying changes.

---

## Summary Stats

- 10 product updates scanned over 7 days
- 5 medium-impact items proposed for module updates
- 5 items in "no action needed"
- 6 coverage gaps detected (above `alert_threshold: 3`)
- 3 modules touched by 2+ proposed changes: M04, M06, 101-02 / 101-03 / 201-04

---

## Next Step

After Marcus reviews and ticks the Approve/Modify/Skip boxes above, run the **`apply-approved-updates`** skill to push the approved changes into the module .md files, the hub's `MONTHLY_DIGEST`, and `summaries/coverage-gaps.md`.

No changes have been made to module files or `index.html` by this review.
