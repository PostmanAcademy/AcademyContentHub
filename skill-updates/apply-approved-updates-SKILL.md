---
name: apply-approved-updates
description: "Apply human-approved product updates to the Postman Academy Hub and playbooks. Reads sources.yaml to find all active programs and module directories. Use this skill after the user has reviewed a Product Update Review document and indicated which changes to approve. Triggers: apply updates, approve changes, update the hub, push approved changes, apply review, update academy hub, commit changes to hub."
---

# Apply Approved Updates

This skill takes human-approved changes from a product update review and applies them to the Academy Hub's data layer, module markdown files, and playbooks. It only acts on what the user has explicitly approved.

## Prerequisites

The user must have already reviewed a "Product Update Review" document (produced by `review-product-updates`) and indicated which changes to approve.

## Step-by-Step

### 1. Read sources.yaml

Read `sources.yaml` to discover all active programs and their module directories. This ensures approved changes are applied to the correct program's module files.

### 2. Confirm what's approved

Ask the user which items to apply. Get explicit confirmation before making changes.

### 3. Read the current hub file

Read `index.html`. The data layer is in the JavaScript section:
- `CLASSES` — program definitions with module arrays (one entry per program)
- `MONTHLY_DIGEST` — product update digest entries
- `PRODUCT_UPDATES` — detailed update entries

### 4. Apply changes to MONTHLY_DIGEST

For each approved update, add a new entry at the **top** of `MONTHLY_DIGEST`:

```javascript
{
  id: "dN",
  date: "Apr 28",
  feature: "Feature Name",
  stage: "GA",
  plans: "Enterprise",
  summary: "What it does in plain English.",
  whyItMatters: "How it affects training content.",
  affectedModules: ["M08", "M09"],
  affectedSessions: ["MCP & AI Agents", "What's New in V12"],
  author: "Author Name"
},
```

### 5. Apply changes to module data in CLASSES

For each approved module change, update the corresponding module object in the appropriate `CLASSES[n].modules` entry:
- Add features to the `features` array
- Update `keyElements` with new bullet points
- Update `overview` if scope expanded
- Set `lastAffected` to the update date
- Preserve existing content unless explicitly approved for removal

**Important:** Match the module to the correct program in `CLASSES`. Multiple programs may have modules affected by the same update.

### 6. Apply changes to module markdown files

For each affected module, update the corresponding `.md` file in the program's `module_dir` (from `sources.yaml`):
- Update `postman_features` in YAML frontmatter if a new feature should be tracked
- Update `status` to `current` (or `needs_review` if partial update)
- Update `last_updated` and `last_audited` dates
- Add content to the markdown body sections as approved

### 7. Resolve coverage gaps

If the review included coverage gaps, and the user approved adding features to specific modules:
- Add the feature to the module's `postman_features` frontmatter
- Remove the resolved gap from `summaries/coverage-gaps.md`

### 8. Update playbooks (if applicable)

Edit Bootcamp Modular System Playbook if approved.

### 9. Show summary

```
Changes Applied:
- Added [n] entries to Monthly Digest
- Updated modules: [list with program names]
- Coverage gaps resolved: [list if any]
- Playbooks updated: [yes/no]

Files modified:
- index.html
- modules/bootcamp/M08-ai-agents.md
- [other files]
```

### 10. Suggest next steps

- If high-impact module changes and the program has `drive_sources` in `sources.yaml`: remind the user to also update the actual slides or facilitator guide in Google Drive (link to the doc)
- If coverage gaps remain: note which features still need homes

## Guidelines

- Never modify files without explicit approval
- Preserve existing content — add, don't replace
- Use the Edit tool for surgical changes
- Match existing formatting exactly
- Always include program context when referencing modules
- Read `sources.yaml` to find module file locations
