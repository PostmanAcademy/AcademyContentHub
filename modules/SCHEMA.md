# Module Markdown Schema

> **Purpose:** Defines the standard format for all training module files. Every module — bootcamp, P4P class, or future program — follows this schema so the hub can parse, display, and monitor it for product update impacts.

---

## Frontmatter (YAML)

Every module file starts with YAML frontmatter between `---` fences. This is the machine-readable layer that the hub and automation skills consume.

```yaml
---
id: M04                              # Unique identifier
title: "API Design & Architecture"   # Display name
program: bootcamp                    # Program this belongs to (bootcamp, p4p, etc.)
owner: Marcus Kidan                  # Who maintains this module
change_sensitivity: medium           # low | medium | high
status: current                      # current | needs_review | update_in_progress | outdated
last_updated: 2026-04-10            # Date content was last revised
last_audited: 2026-04-10            # Date someone last checked against current product

postman_features:                    # Product features this module depends on
  - API Builder
  - Mock Servers
  - OpenAPI spec support

update_triggers:                     # What kinds of product changes should flag this module
  - "New spec format support"
  - "Design tooling UI changes"
  - "Mock server feature updates"
---
```

### Field Reference

| Field | Required | Type | Purpose |
|-------|----------|------|---------|
| `id` | Yes | string | Unique module ID (M01, P4P-101, etc.) |
| `title` | Yes | string | Human-readable name |
| `program` | Yes | string | Which program this belongs to |
| `owner` | Yes | string | Content owner |
| `change_sensitivity` | Yes | enum | How often this needs product-driven updates |
| `status` | Yes | enum | Current content freshness |
| `last_updated` | Yes | date | When content was last revised |
| `last_audited` | Yes | date | When last checked against current product |
| `postman_features` | Yes | list | Specific features referenced — the linkage for update monitoring |
| `update_triggers` | Yes | list | Plain-language descriptions of what product changes affect this module |

---

## Body Sections (Markdown)

After the frontmatter, the body uses standard markdown headings. These are the sections the hub renders.

### Required Sections

**`## Overview`** — What this module covers and why it matters. 2–4 sentences.

**`## Learning Objectives`** — What learners will understand or be able to do after this module. Bulleted list, 2–4 items.

**`## Key Elements`** — The core teaching content. This is the substance of the module — concepts, frameworks, examples, metaphors. Use subheadings as needed.

**`## Activities`** — Hands-on exercises, discussion prompts, or group work. Each activity should have a clear setup and expected outcome.

**`## Postman Features in This Module`** — How specific Postman product capabilities are used or demonstrated. This section exists so the hub can show *what* about each feature is taught, not just *that* it's referenced.

### Optional Sections

**`## Facilitator Notes`** — Guidance for whoever is delivering this module. Timing, common questions, what to emphasize.

**`## Pain Points Addressed`** — Which real-world problems this module surfaces and contextualizes.

---

## File Naming Convention

```
modules/
  bootcamp/
    M01-welcome.md
    M02-internet-apis.md
    ...
  p4p/                    # Future
    P4P-101-api-basics.md
    P4P-201-advanced.md
```

Pattern: `{ID}-{slug}.md` where the slug is a lowercase, hyphenated short name.

---

## How the Hub Uses This

1. **Parsing:** The hub reads frontmatter YAML to populate module cards, status indicators, and the feature dependency map.
2. **Monitoring:** The `postman_features` list is compared against incoming product updates. A match flags the module for review.
3. **Display:** The markdown body sections are rendered in the module detail view.
4. **Audit trail:** `last_updated` and `last_audited` dates drive the "freshness" indicators on the dashboard.
