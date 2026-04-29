# Training System Operations Guide

> **Purpose:** How the modular training system works — the update workflow, audit cadence, automation, and how to add new content.
>
> **Owner:** Marcus Kidan | **Last Updated:** April 28, 2026

---

## How the System Works

The training content lives in individual markdown files, one per module. Each file has YAML frontmatter with machine-readable metadata (feature dependencies, change sensitivity, status) and a markdown body with the teaching content.

Four things keep it current:

1. **The module files** — Each module declares the Postman features it depends on and what product changes should trigger a review.
2. **sources.yaml** — Single config listing every Slack channel, training program, and Google Drive source doc. Add a source = add a YAML block.
3. **Automated monitoring** — Scheduled tasks scan Slack for product updates, map them against every module's feature list, verify against actual slides/guides in Google Drive, and produce a review document with coverage gap detection.
4. **This hub** — Displays module status, freshness, and feature dependencies so teammates can check weekly without touching any files.

---

## Directory Structure

```
TechnicalTrainer/
  index.html                              ← The hub UI (published via GitHub Pages)
  sources.yaml                            ← Data sources registry (Slack, Drive, programs)
  sync.py                                 ← Generates hub data from module .md files

  modules/
    SCHEMA.md                             ← Module file format specification
    SYSTEM.md                             ← This file — operational guide
    bootcamp/
      M01-welcome.md                      ← 12 bootcamp modules
      M02-internet-apis.md
      ...
      M12-wrap-up.md
    101/                                  ← Future: API 101 course modules
    201/                                  ← Future: API 201 advanced modules

  skill-updates/                          ← Updated skill instructions (pending reinstall)
  Bootcamp Modular System Playbook.md
  Product Update Review - YYYY-MM-DD.md   ← Weekly review documents
```

---

## The Sources Registry

**`sources.yaml`** is the single configuration file that controls what the system monitors. It has four sections:

1. **`slack_channels`** — Which Slack channels to scan, how often, and how far back to look.
2. **`programs`** — Every training program (bootcamp, 101, 201, etc). Each declares its module directory, ID prefix, and `drive_sources` — Google Drive slides/docs the review skill can read to verify actual training content.
3. **`reference_docs`** — Links to design documents and wikis for human reference (not scanned automatically).
4. **`coverage_settings`** — Controls for coverage gap detection thresholds.

### Adding a New Data Source

To add a Slack channel, Google Drive folder, or wiki page, edit `sources.yaml` and add a block under the appropriate section. No skill editing required — the skills read `sources.yaml` at runtime.

### Adding a New Training Program

1. Create the folder under `modules/` (e.g., `modules/101/`)
2. Add module `.md` files following `SCHEMA.md`
3. Add a `programs` entry in `sources.yaml` (include `drive_sources` if the program has slides/docs in Google Drive)
4. Run `python3 sync.py --write` to regenerate the hub's CLASSES data from the .md files
5. The skills and hub will pick it up automatically

---

## The Update Workflow

### How Product Changes Flow Through the System

```
sources.yaml lists all data sources and programs
  → Cowork scans all Slack channels in sources.yaml
    → Compares each update against ALL modules in ALL programs
      → Maps features to modules via postman_features frontmatter
        → For high-impact changes, reads actual Drive content to verify
          → Detects coverage gaps (features not taught anywhere)
            → Produces a Product Update Review document
              → Human reviews, approves/modifies/skips
                → apply-approved-updates skill writes changes
                  → Module files updated → sync.py → hub reflects new state
```

### What Automation Does

1. **Scans Slack** — Reads every channel listed in `sources.yaml`
2. **Maps to ALL modules** — Each update is compared against every module's `postman_features` list across all programs
3. **Classifies impact** — High (direct feature change), Medium (related capability), Low (tangential), None
4. **Verifies against Drive** — For high/medium impact, reads actual slides and facilitator guides to check if content already covers the change
5. **Detects coverage gaps** — Identifies features in product updates that no module in any program covers
6. **Produces review document** — Structured markdown with recommended actions, Drive verification notes, and gap warnings
7. **Applies approved changes** — After human review, updates module frontmatter and body content

### What Humans Do

1. **Review the Product Update Review** — Check flagged modules and recommended changes for accuracy
2. **Review coverage gaps** — Decide if uncovered features need a new module or belong in an existing one
3. **Approve, modify, or skip** — Accept automation's suggestions or adjust based on pedagogical judgment
4. **Test in delivery** — Run updated modules in the next session
5. **Capture field notes** — Update facilitator notes in the module file

---

## Audit Cadence

| Change Sensitivity | Audit Frequency | Modules |
|-------------------|----------------|---------|
| 🔴 High | Weekly | M06 (Git), M08 (AI), M09 (Platform), M10 (Hands-On Lab) |
| 🟡 Medium | Bi-weekly | M04 (Design), M05 (Security), M07 (Dev Experience), M11 (Lifecycle) |
| 🟢 Low | Monthly | M01 (Welcome), M02 (Internet & APIs), M03 (How APIs Work), M12 (Wrap-Up) |

As new programs are added (101, 201), their modules follow the same cadence rules based on their `change_sensitivity` frontmatter field.

---

## Adding a New Module

Whether it's a new bootcamp module, a 101 class, or a 201 class:

1. **Choose the right directory** — `bootcamp/` for bootcamp modules, `101/` for 101 classes, `201/` for 201 classes, etc.
2. **Follow the schema** — Copy the structure from `SCHEMA.md`. Every field in the frontmatter is required.
3. **Name the file** — Pattern: `{ID}-{slug}.md` (e.g., `M13-advanced-testing.md` or `101-01-what-are-apis.md`)
4. **Declare feature dependencies** — The `postman_features` list is what connects your module to the monitoring system. Be specific. "Collections" is better than "Postman features."
5. **Set change sensitivity** — How often will product changes affect this content? This determines audit frequency.
6. **Write update triggers** — Plain-language descriptions of what kinds of product changes should flag this module for review.
7. **Ensure the program is registered** — The program must have an entry in `sources.yaml` under `programs` and a `CLASSES` entry in `index.html`.
8. **The system picks it up** — Once the file exists with valid frontmatter and the program is registered, the skills and hub include it automatically.

---

## Module Status Lifecycle

```
current → needs_review → update_in_progress → current
                      → not relevant (no change needed) → current
                      → outdated (if unaddressed too long)
```

| Status | Meaning | Action |
|--------|---------|--------|
| `current` | Content matches the current product | None — module is healthy |
| `needs_review` | A product update may affect this module | Review flagged changes, decide if content needs updating |
| `update_in_progress` | Approved changes are being applied | Complete the update, test in delivery, mark current |
| `outdated` | Module has unaddressed changes for 2+ audit cycles | Prioritize for immediate update |

---

## Coverage Gap Detection

The safety net. When a product update mentions a feature that **no module in any program** lists in its `postman_features` frontmatter, the system flags it in the Product Update Review document.

This prevents the scenario where Postman ships a feature, no module declares it as a dependency, and the update silently passes through without being flagged. The `coverage_settings` in `sources.yaml` controls the alert threshold.

---

## Source Materials

Source materials are listed in `sources.yaml` — either as `drive_sources` per program (for automated verification) or as `reference_docs` (for human reference). The canonical references:

| Document | Purpose |
|----------|---------|
| `sources.yaml` | Master registry of all data sources and programs |
| API Fundamentals Field Guide (api-city-explainer-2.html) | Master metaphor reference — the City Metaphor system |
| V11 Bootcamp Flow ([Google Doc](https://docs.google.com/document/d/1D7o7IYvkrQm2FeCgbh7SisnzF4Xlbc6pA1QJInGh-y4/edit)) | Original facilitator flow |
| Bootcamp Review ([Google Doc](https://docs.google.com/document/d/1D14mLqe-BIz3dseLtvF9IVgUClZmfCICfFERnfStnog/edit)) | Analysis of what needed restructuring |
| Refresh Guide ([Google Doc](https://docs.google.com/document/d/1Uo1oHwETRLwxCRA40Hc1am5toD1TrI3QmUQSuCZ7Y_8/edit)) | Digital Grocery Store hands-on modules |
| Postman V12 Wiki ([Confluence](https://postmanlabs.atlassian.net/wiki/spaces/v12/pages/7131791735/Postman+v12)) | Internal V12 product documentation |

---

## Design Principles

These principles govern how modules are written and maintained:

**Interleaved, not lecture-then-lab.** Every module weaves concept → metaphor → activity → reflection. No "theory block then practice block."

**One metaphor system.** The City Metaphor is the backbone. The internet is a city, APIs are buildings, requests are forms, Postman is the city management platform.

**Each module is self-contained.** A module can be delivered independently without breaking the narrative. Modules 1–12 have a natural flow but aren't hard dependencies.

**Pain points are threaded, not siloed.** Each module surfaces the relevant real-world problem in context rather than collecting all pain points in one place.

**Feature dependencies are explicit.** Every module declares exactly which Postman product features it references. This is the linkage that makes automated monitoring work.

**Config-driven, not code-driven.** Adding sources, programs, or modules requires editing config files (YAML/markdown), not modifying skills or the hub code.
