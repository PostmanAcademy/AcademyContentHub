---
name: scaffold-program
description: "Generate or refresh module .md files for a training program by reading its Google Drive source materials. Use this skill whenever someone says: add a program, scaffold modules, bootstrap from Drive, generate modules from slides, set up a new class, sync from Drive, refresh modules from Drive, onboard a program, create module files, or any variation of turning Drive content into the module files the hub needs. Also use when a user adds drive_sources to sources.yaml and wants to populate the module directory. This is the bridge between 'I have slides in Drive' and 'the hub tracks my program.'"
---

# Scaffold Program from Drive

This skill reads Google Drive source materials for a training program and generates structured module `.md` files that the Academy Hub can track. It's the bridge between "I have slides in a Drive folder" and "the hub monitors my program."

## How It Fits in the Pipeline

This skill is one of three that keep the training system current:

1. **scaffold-program** (this skill) — Creates module `.md` files from Drive content. Run when adding a new program or refreshing an existing one.
2. **review-product-updates** — Scans Slack for product changes, maps against all modules. If it finds a program with no modules, it flags it and recommends running this skill.
3. **apply-approved-updates** — Applies human-approved changes to module files and the hub.

The review skill depends on module files existing. Without them, a program is invisible to the monitoring system. That's why this skill must run before the first review after adding a new program.

## When to Use

- A new program is added to `sources.yaml` with `drive_sources` but has no module `.md` files yet
- An existing program's Drive content has changed and you want to regenerate or refresh module files
- The review-product-updates skill flagged an unscaffolded program
- Someone says "add 101" or "set up the 201 program" or "sync modules from Drive"

## Step-by-Step

### 1. Read sources.yaml

Read the `sources.yaml` file in the workspace root. Identify which programs to scaffold:
- If the user named a specific program (e.g., "set up 101"), find that program's entry
- If the user said "all" or didn't specify, find all programs that have `drive_sources` but an empty or missing `module_dir`
- Each program entry has: `id`, `name`, `module_dir`, `module_prefix`, `drive_sources[]`

If the program doesn't have `drive_sources`, tell the user they need to add Drive file IDs to `sources.yaml` first and show the format.

### 2. Read Drive source materials

For each file listed in the program's `drive_sources`:
- Use the Google Drive `read_file_content` tool with the file's `id`
- Presentations (type: presentation) contain slide content — these define module structure and topics
- Documents (type: document) contain instructor guides — these have deeper context, activities, and facilitator notes

Read ALL drive_sources for the program. The slides define what each module teaches; the instructor guides fill in the learning objectives, activities, and pain points.

### 3. Identify modules

From the Drive content, identify distinct modules/sessions. Typically each numbered course (101, 102, 103...) is one module. Look for:
- Clear topic boundaries in slide decks
- Separate files per module (e.g., `v11_101_Topic.pptx`, `v11_102_Topic.pptx`)
- Section breaks within a single deck

For each module, extract:
- **Title** — the module's topic (e.g., "Discovering and Evaluating APIs")
- **Overview** — 2-4 sentences on what it covers and why
- **Learning objectives** — what learners will understand or be able to do (2-4 bullets)
- **Key elements** — the main concepts, tools, or techniques taught (3-6 items)
- **Activities** — hands-on exercises described in the slides or instructor guide
- **Pain points addressed** — what real-world problems this module helps solve
- **Postman features** — specific product features referenced (Collections, Mock Servers, etc.)
- **Update triggers** — what kinds of product changes should flag this module for review

### 4. Determine postman_features carefully

This is the most important field — it's what connects the module to the automated monitoring system. Be specific and accurate:

**Good:** `Collections`, `Mock Servers`, `API Documentation`, `Collection Runner`, `Test Scripts`, `Environments`
**Bad:** `Postman features`, `API tools`, `testing`

Cross-reference against the features used in other programs (read a few existing module files from `modules/bootcamp/` to see the naming conventions). Use consistent feature names across programs.

### 5. Determine change_sensitivity

Based on the module content:
- **high** — References rapidly changing features (Git integration, AI, Agent Mode, new UI elements)
- **medium** — References stable but evolving features (Collections, Mock Servers, API documentation)
- **low** — Conceptual content that rarely changes (what are APIs, why testing matters)

### 6. Write module .md files

For each module, create a `.md` file in the program's `module_dir` following the schema in `modules/SCHEMA.md`. The file naming pattern is `{prefix}-{number}-{slug}.md`:
- 101 program: `101-01-discovering-evaluating-apis.md`
- 201 program: `201-01-prototyping-apis.md`

Use today's date for both `last_updated` and `last_audited`.

Set `status: current` for all new modules.

Each module file must include ALL required sections from SCHEMA.md:
- **Overview** — 2-4 sentences
- **Learning Objectives** — 3-4 bullets
- **Key Elements** — With subheadings and descriptions (the core teaching content)
- **Activities** — Hands-on exercises with setup and expected outcomes
- **Postman Features in This Module** — How each feature is used or demonstrated

And these optional but recommended sections:
- **Facilitator Notes** — Timing, setup requirements, common questions, tips
- **Pain Points Addressed** — Real-world problems this module helps solve

### 7. Register the program in sources.yaml (if not already there)

If the program entry is commented out in `sources.yaml`, uncomment it and fill in the details. If it's missing entirely, add it following the existing pattern.

Make sure `active: true` is set.

### 8. Run sync.py

Run `python3 sync.py --write` to regenerate the hub's CLASSES data from all module files. This updates `index.html` so the new program appears in the hub immediately.

Verify with `python3 sync.py --check` that there's no drift.

### 9. Present summary

Show the user what was created:

```
Program scaffolded: API 101
  Modules created: 4
  - 101-01: Discovering and Evaluating APIs (medium sensitivity)
  - 101-02: Documenting APIs (medium sensitivity)
  - 101-03: Testing APIs (high sensitivity)
  - 101-04: Prototyping APIs (medium sensitivity)
  Features tracked: [list]
  Drive sources linked: [list]
  Hub updated: yes

Next steps:
  - Review the generated .md files and adjust if needed
  - The review-product-updates skill will now monitor this program
  - To refresh from Drive later: "scaffold 101 from Drive"
```

### 10. Offer to scaffold the next program

If there are other programs in `sources.yaml` with `drive_sources` that haven't been scaffolded yet, offer to do them.

## Guidelines

- Always read `modules/SCHEMA.md` first to ensure you follow the exact format
- Always read a few existing bootcamp module files to match the naming conventions for `postman_features`
- Be thorough with `postman_features` — missing a feature means the monitoring system won't catch updates to it
- Set `owner` to the user's name (from context) or "TBD" if unknown
- If a Drive file can't be read, skip it and note the failure — don't block the whole program
- These are v11 materials — note this in the overview when relevant, since the hub monitors for v12 changes
- The skill is idempotent: running it again overwrites existing module files with fresh content from Drive
- After scaffolding, the daily product update review will automatically include the new program
