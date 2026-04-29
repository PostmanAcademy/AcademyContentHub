---
name: review-product-updates
description: "Weekly review of Postman product updates for the Academy Hub. Reads sources.yaml for all configured Slack channels, scans ALL training programs for affected modules, detects coverage gaps, and produces a structured review document for human approval. Use this skill whenever someone says: review product updates, check what shipped, weekly review, what changed this week, audit bootcamp content, check for outdated modules, or any variation of checking Postman product changes against training content. Also use when scheduled tasks need to produce a review digest."
---

# Review Product Updates

This skill reads Postman's product update channels and produces a **review document** for human approval. Nothing gets changed in the hub or playbooks until the human approves.

## What This Skill Does

1. Reads `sources.yaml` to discover all configured Slack channels and training programs
2. Scans each Slack channel for the configured lookback period
3. Extracts each product update with metadata (feature name, stage, plan tiers, description, demo links)
4. Reads ALL module files across ALL active programs listed in `sources.yaml`
5. Maps each update against every module's `postman_features` frontmatter list
6. **Detects coverage gaps** — features in updates that no module in any program covers
7. Produces a structured review document with proposed changes
8. Saves the review document to the outputs folder

## Step-by-Step

### 0. Read the sources registry

**Before anything else**, read the `sources.yaml` file in the workspace root. This file lists:
- All Slack channels to scan (under `slack_channels`) — each with channel ID, lookback period, and feature domains
- All training programs (under `programs`) — each with module directory and ID prefix
- Coverage settings (under `coverage_settings`) — gap report output path and alert threshold

If `sources.yaml` doesn't exist, fall back to channel `C08SPKCGZQ8` (#product-updates), bootcamp only.

### 1. Read all Slack channels

For each channel in `sources.yaml` → `slack_channels`:
- Use the Slack `read_channel` tool with the channel's `channel_id`
- Pull the last 20-30 messages, filter to `lookback_days` (default 7)
- Read threads for full context
- Tag each update with its source channel
- De-duplicate across channels

### 2. Extract update metadata

For each product update, capture: feature name, stage (2=beta, 7=GA), plan availability, description (2-3 sentences), demo link, author, date, source channel. Skip bot-generated replies.

### 3. Read ALL module files across ALL programs

For each program in `sources.yaml` → `programs` where `active: true`:
- Read all `.md` files in the program's `module_dir`
- Parse YAML frontmatter for `postman_features` and `update_triggers`
- Build a master feature-to-module mapping across ALL programs

**If a program directory is empty or has no .md files:**
This means the program is registered in `sources.yaml` but hasn't been scaffolded yet. **Do not silently skip it.** Instead:
1. Flag it as an **Unscaffolded Program** in the review document (see template below)
2. If the program has `drive_sources`, read those Drive files to understand what the program covers
3. Still attempt to map product updates against the program's likely feature surface based on the Drive content
4. Recommend running `/scaffold-program` to generate the module files

This ensures no program registered in sources.yaml is invisible to the review process.

**Key change: scan ALL programs, not just bootcamp.**

### 4. Map updates to modules

Compare updates against the master mapping. Include program name: "M08 (Bootcamp)" or "101-03 (API 101)".

### 5. Verify against Drive source materials

If a program in `sources.yaml` has `drive_sources`, use the Google Drive `read_file_content` tool to pull the actual training content for any module flagged as affected. Compare what the slides or facilitator guide currently say against the product update. This lets you tell the reviewer: "The slides already cover this" or "The slides still reference the old workflow — needs revision."

Only read Drive docs for **High** or **Medium** impact updates. Skip for Low/None.

### 6. Detect coverage gaps

For each update, check if its feature appears in ANY module's `postman_features` across ALL programs. If not → coverage gap. Flag prominently.

### 7. Classify impact

- **High** — Changes how we teach a concept. Requires revision.
- **Medium** — Worth mentioning but no restructuring needed.
- **Low** — Informational only.
- **None** — Not relevant to training.

### 8. Produce the review document

```markdown
# Weekly Product Update Review — [Date Range]

**Generated:** [timestamp]
**Sources scanned:** [channels from sources.yaml]
**Programs checked:** [active programs from sources.yaml]
**Updates found:** [count]
**Unscaffolded programs:** [count or "none"]
**Coverage gaps detected:** [count]

---

## Unscaffolded Programs

> Programs registered in `sources.yaml` with `drive_sources` but no module .md files.
> These programs are NOT being monitored for product updates until scaffolded.

- **[Program Name]** — [module_dir] is empty. Has [N] Drive sources. Run `/scaffold-program` to generate modules.

---

## Coverage Gaps (Features Not Taught Anywhere)

> Features in product updates NOT in any module's `postman_features`.

- **[Feature]** — [Description]. Consider: [suggested modules]

---

## Proposed Changes (Needs Your Approval)

### [Feature Name] — Impact: [High/Medium/Low]
**Date:** [date] | **Stage:** [stage] | **Plans:** [plans] | **Source:** [channel]
**Summary:** [2-3 sentences]
**Demo:** [link if available]

**Affected Modules (all programs):**
- [ ] **M08 — AI & Agents (Bootcamp):** [What should change]
  - _Drive check:_ [Slides already cover this / Slides reference old workflow — needs update]

**Proposed hub data change:** [JSON for MONTHLY_DIGEST]
**Your decision:** Approve / Modify / Skip

---

## No Action Needed
[Low/None items]

## Summary Stats
```

### 9. Update coverage gaps file

Append new gaps to `summaries/coverage-gaps.md`. Don't overwrite existing gaps.

### 10. Save and present

Save as `Product Update Review - [date].md`. Highlight coverage gaps first. Suggest `apply-approved-updates`.

## Guidelines

- Always read `sources.yaml` first
- Scan ALL active programs
- Coverage gaps are top priority
- Focus on teaching-relevant changes; skip internal tooling
- Flag UI changes for hands-on lab modules
- Stage 2 (beta): flag for awareness, don't update modules
- Include demo links when available
- De-duplicate across channels
