# Weekly Product Update Review — Apr 3–10, 2026

**Generated:** April 10, 2026
**Source:** #product-updates (Slack)
**Updates found:** 4

---

## Proposed Changes (Needs Your Approval)

### CLI Generator — Impact: High
**Date:** Apr 8 | **Stage:** 7 (GA) | **Plans:** Team, Enterprise
**Summary:** Generate a CLI for your APIs in one click — usable by both AI agents and humans. Each CLI includes built-in skills for accessing APIs, supports multiple auth methods, retries, error handling, and compiles into a binary for all major OSes. Powered by the Go SDK under the hood.
**Demo:** https://www.loom.com/share/ed9f6766fba64962ba6573a4e83f6c67
**Author:** Sagiv Ofek

**Affected Modules:**
- [ ] **M08 — AI & Agents:** Add CLI Generator as a key example of making APIs "AI-ready." This is a concrete demo of how Postman bridges human and agent workflows — worth adding to speaker notes and potentially the hands-on activity.
- [ ] **M09 — The Postman Platform:** Add as a significant new platform capability. Reinforces the "API-first development platform" narrative.

**Proposed hub data change:**
```json
{ "date": "Apr 8", "feature": "CLI Generator", "description": "Generate a CLI for your APIs in one click — usable by AI agents and humans. Built-in skills, multi-auth, Go SDK under the hood.", "plans": "Team, Enterprise", "modules": ["M08", "M09"] }
```

**Your decision:** Approve / Modify / Skip

---

### Secrets Resolution & Shared Vault — Impact: High
**Date:** Apr 7 | **Stage:** 2 (Beta/Internal) | **Plans:** Free, Solo, Team, Enterprise
**Summary:** Secrets are now a first-class concept in Postman. Just-in-time resolution means secrets are never stored in plain text. Variables can be marked as "Secure" and sourced from local/shared vaults or external providers (e.g., AWS Secrets Manager). Shared Vault enables team-wide secure credential management. Backward compatible with existing `{{vault:` references.
**Demo:** https://www.loom.com/share/fff6a85a48c74088a07b917a509465e3
**Author:** Hitesh Sharma

**Affected Modules:**
- [ ] **M05 — Security & Authentication:** Major update. Secrets Resolution replaces the old "variables store credentials in plain text" narrative. The Shared Vault changes how we teach team credential management. *Note: Stage 2 — flag as "coming soon" in speaker notes but don't restructure yet.*
- [ ] **M09 — The Postman Platform:** Significant security posture improvement worth noting at the platform level.
- [ ] **M10 — Hands-On Labs:** When this hits GA, the labs that involve API keys and auth will need updating to use the new Secure variable flow instead of plain-text environment variables.

**Proposed hub data change:**
```json
{ "date": "Apr 7", "feature": "Secrets Resolution & Shared Vault", "description": "Secrets as first-class concept. Just-in-time resolution, never stored in plain text. Shared Vault for teams.", "plans": "All plans", "modules": ["M05", "M09", "M10"] }
```

**Your decision:** Approve / Modify / Skip

---

### Postman Reports — Hourly Updates & New Visualizations — Impact: Medium
**Date:** Apr 3 | **Stage:** 7 (GA) | **Plans:** Enterprise
**Summary:** Reports now update every hour instead of monthly. Current-month data is included. Top-level metrics show last 30 days. Partner Workspaces Analytics now use Sankey charts instead of bar charts. All changes also available via the `/analytics` API endpoint.
**Author:** Ramji Enamuthu

**Affected Modules:**
- [ ] **M11 — API Lifecycle & Governance:** Update the "Reports" reference to reflect near-real-time data. The shift from monthly to hourly is meaningful for enterprise governance conversations.

**Proposed hub data change:**
```json
{ "date": "Apr 3", "feature": "Reports — Hourly Updates", "description": "Reports now update hourly instead of monthly. New Sankey chart visualizations for partner analytics. Available via /analytics API.", "plans": "Enterprise", "modules": ["M11"] }
```

**Your decision:** Approve / Modify / Skip

---

## No Action Needed

### Publisher Self-Serve Verification — Impact: Low
**Date:** Apr 7 | **Stage:** 7 (GA) | **Plans:** All plans
**Summary:** API publishers now verify domain ownership via DNS record or "Run in Postman" button. Simplified from the previous multi-step flow.
**Why no action:** This is an API Network publishing workflow change. It doesn't affect how we teach any bootcamp concepts or training topics. M11 (API Lifecycle) has a tangential connection, but the verification simplification doesn't change any training content. Good to know, no action required.

---

## Summary Stats
- **Total updates this week:** 4
- **High impact:** 2 (CLI Generator, Secrets Resolution)
- **Medium impact:** 1 (Reports Hourly Updates)
- **Low/None:** 1 (Publisher Verification)
- **Modules affected:** M05, M08, M09, M10, M11
- **Stage 2 (beta) items:** 1 — Secrets Resolution (flag but don't restructure yet)
- **Enterprise-only features:** 1 — Reports (relevant for Solutions/Sales training)

---

*Review generated by the review-product-updates skill. After reviewing, tell me which items to approve, modify, or skip, and I'll use the apply-approved-updates skill to push changes to the hub and playbooks.*
