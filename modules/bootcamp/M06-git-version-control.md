---
id: M06
title: "Git & Version Control"
program: bootcamp
owner: Marcus Kidan
change_sensitivity: high
status: current
last_updated: 2026-04-10
last_audited: 2026-04-10

postman_features:
  - Native Git integration
  - Branching
  - Pull requests for API changes
  - Version history

update_triggers:
  - "Any Git-related feature release"
  - "Branching workflow changes"
  - "Pull request feature updates"
  - "Version history UI changes"
---

## Overview

Version control isn't just for code. Your APIs change just as frequently—and with just as much risk. In this module, you'll learn why Postman adopted native Git integration and how it connects API development to the versioning workflows your engineering teams already use. We'll explore Git fundamentals, then dive into how Postman lets you collaborate, branch, and review API changes with the same rigor as code reviews.

## Learning Objectives

- Explain core Git concepts (repo, branch, commit, pull request, merge)
- Understand why Postman adopted native Git integration
- Connect version control to the API development lifecycle
- Apply branching and PR workflows to collaborative API design

## Key Elements

### Why Version Control Matters for APIs

APIs are living systems. They evolve:
- New endpoints are added
- Request/response schemas change
- Authentication flows get updated
- Documentation improves

Without version control, teams lose visibility into **who changed what and when**, making it impossible to troubleshoot, audit, or roll back changes.

### Core Git Concepts

**Repository (Repo)**
- A project's complete history of changes
- Metaphor: City blueprints archive—every design and renovation is stored
- In Postman: Your Postman collections and environments live in a Git repo

**Branch**
- A parallel version of your project
- Metaphor: A separate blueprint room where architects can experiment without affecting the master blueprint
- Common branches: `main` (production-ready), `develop` (integration), `feature/new-endpoint` (experimental)

**Commit**
- A snapshot of changes with a message explaining why
- Metaphor: A dated, signed note in the blueprint archive: "Added payment endpoint, implements PR #42"
- Good commits are small, focused, and well-described

**Pull Request (PR)**
- A proposal to merge changes from one branch into another
- Metaphor: Architect proposes a design change to the review board—they ask questions, request revisions, then approve
- Forces review and discussion before integration

**Merge**
- Combining changes from two branches
- Metaphor: Integrating approved renovations into the master blueprint
- Can be automatic (if no conflicts) or require manual resolution

### Why Postman Went Native Git

**V12 Insight**: Git is native. Postman now lives in the branching workflow engineers already use. No context switching.

Before native Git integration, API teams and code teams had different workflows:
- Engineers used Git for code
- API designers used Postman in isolation
- Changes to APIs happened outside version control
- Deployments became chaotic because API changes weren't tracked alongside code changes

With native Git integration, Postman collections live *in* your Git repo, treated like code:
- API changes are version-controlled
- Pull requests can include both code and API changes
- Code review and API review happen together
- The "single source of truth" includes both

**City Connection**: Git is the city's version control system. Every blueprint change is tracked, every renovation is proposed and reviewed before construction begins. When the city adopts native Git integration, all blueprints—buildings, streets, utilities—live in the same system with the same approval process.

## Activities

### Conceptual Exercise: Git Workflow Mapping

Divide the class into small groups. Assign each group a real-world API change scenario:

1. **New Endpoint**: Your team needs to add a `/users/search` endpoint
2. **Breaking Change**: Update request schema for `/payments` to require a new field
3. **Bug Fix**: Fix incorrect response example in `/orders/{id}` docs
4. **Security Update**: Change OAuth scope requirements

For each scenario, teams answer:
- Which branch would you create?
- What would your commit message say?
- Why would you open a pull request vs. committing directly?
- What questions would a reviewer ask?

*Facilitation tip: This exercise grounds abstract Git concepts in real API work. Call on groups to present; use their answers to highlight the value of peer review.*

## Postman Features in This Module

- **Native Git Integration**: Connect Postman workspaces directly to GitHub, GitLab, or other Git providers
- **Branching**: Create, switch, and manage branches within Postman
- **Pull Requests**: Link Postman changes to PRs; see diffs of endpoint changes
- **Version History**: View a complete timeline of collection changes with diffs and revert capability
- **Conflict Resolution**: When merges conflict, Postman surfaces conflicts and guides resolution

## Facilitator Notes

- Start with the "city blueprints" metaphor to make Git feel intuitive—most developers understand that blueprints should be versioned
- Avoid Git jargon at first; use the metaphors, then introduce the terms
- In live demos, show a real Git repository with a `.postman_collection.json` file—make it concrete
- Highlight the contrast: "Before, Postman lived separately from Git. Now it's a first-class citizen in your repo."
- If the class has junior developers unfamiliar with Git, pre-teach basic Git (not specific to Postman) in an optional pre-session

## Pain Points Addressed

**Lack of Visibility**: Teams don't know when or why API contracts changed. Git provides a complete audit trail with commit messages explaining the "why."

**Context Switching**: API designers had to leave Git-based workflows to manage APIs in Postman. Native integration keeps everyone in one place.

**Conflicting Changes**: When multiple teams change the same collection offline, merges are chaotic. Git-native workflows enforce review and prevent silent conflicts.

**Deployment Mismatches**: Code changes and API changes were deployed separately, causing integration bugs. Version controlling APIs alongside code ensures they move in sync.
