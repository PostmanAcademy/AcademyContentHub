---
id: 101-02
title: "Documenting APIs"
program: 101
owner: Marcus Kidan
change_sensitivity: medium
status: current
last_updated: 2026-04-28
last_audited: 2026-04-28

postman_features:
  - Collections
  - API Documentation
  - Examples
  - Pull Requests
  - Partner Workspaces
  - Forking

update_triggers:
  - "Documentation UI changes"
  - "Pull request feature updates"
  - "Partner Workspace changes"
  - "Example management updates"
---

## Overview

Covers API documentation best practices and how Postman streamlines the documentation lifecycle. Participants learn to migrate legacy API docs into Postman collections, create examples for different response scenarios, use pull requests for collaborative documentation review, and share APIs securely with external partners through Partner Workspaces. These are v11 materials; the hub monitors for v12 changes.

## Learning Objectives

- Understand different types of API documentation and who is responsible for each
- Create and manage request/response examples in collections
- Use pull requests to collaborate on documentation changes
- Set up Partner Workspaces with multi-partner mode for secure external sharing

## Key Elements

### Types of API Documentation

Not all documentation is the same, and not all of it is written by the same person. Understanding the different types helps you identify gaps in your own API documentation.

**Reference Documentation:**
- The complete technical specification of every endpoint, parameter, header, and response code
- Written by: developers who build the API
- Format: auto-generated from specs or collections
- Audience: developers integrating with the API
- Example: "GET /users/{id} — Returns a User object. Parameters: id (string, required). Responses: 200 (User), 404 (Not Found)."

**Tutorials and Getting Started Guides:**
- Step-by-step walkthroughs for common use cases
- Written by: developer advocates, technical writers, or senior developers
- Format: narrative prose with code examples
- Audience: developers new to the API
- Example: "How to authenticate and retrieve your first customer record in 5 minutes"

**Code Samples:**
- Copy-paste-ready code in multiple languages showing how to call the API
- Written by: developer advocates or community contributors
- Format: language-specific code blocks
- Audience: developers who learn by example

**Release Notes and Changelogs:**
- What changed, when, and why — including breaking changes, deprecations, and new features
- Written by: product managers or engineering leads
- Format: dated entries with version numbers
- Audience: existing integrators who need to know if their code will break

**Workflow Guides:**
- End-to-end scenarios that chain multiple API calls together to accomplish a business goal
- Written by: solutions engineers, technical writers
- Format: narrative with sequence diagrams
- Audience: architects and senior developers planning integrations

### Writing Effective Documentation

Good API documentation answers three questions for every endpoint:
1. **What does it do?** — A one-sentence description in plain language
2. **How do I call it?** — Method, URL, headers, parameters, request body
3. **What will I get back?** — Response codes, response body structure, error formats

Common mistakes:
- **Assuming context** — Don't write "Returns the resource." Write "Returns the user profile including name, email, and account status."
- **Missing error documentation** — A 200 response is obvious. Document the 400, 401, 403, 404, and 500 responses too. Developers spend more time debugging errors than reading success responses.
- **Stale examples** — An example showing a response field that no longer exists is worse than no example at all. It creates false confidence.

### Postman Documentation Features

Postman turns collections into live, auto-generated documentation. This bridges the gap between "the API works" and "someone can understand how to use it."

**Auto-Generation:**
- Every collection automatically generates a documentation page
- Endpoint names, descriptions, parameters, and examples are pulled directly from the collection
- When you update the collection, the docs update automatically — no separate publishing step

**Keeping Docs Up-to-Date:**
- Because the documentation lives inside the collection, there's no drift between what the API does and what the docs say
- Compare this to a wiki page: the API changes, but nobody updates the wiki. Six months later, the wiki is a liability.

**Enhancing with Descriptions:**
- Add markdown descriptions to collections, folders, requests, parameters, and response bodies
- Use tables for parameter reference, images for architecture diagrams, and links to related resources
- Descriptions support full markdown: headers, bold, italic, code blocks, tables, and images

### Examples: Showing What Real Requests and Responses Look Like

Examples are saved request/response pairs attached to a request. They serve as concrete illustrations of how the API behaves in different scenarios.

**Why Multiple Examples Per Request:**
A single endpoint can behave differently depending on input. Consider `GET /users/{id}`:
- **Success case:** ID exists, returns user object with 200
- **Not found case:** ID doesn't exist, returns error message with 404
- **Unauthorized case:** Missing or invalid auth token, returns 401

Each scenario deserves its own example. Without them, a developer integrating your API has to guess what errors look like.

**Creating Effective Examples:**
- Use realistic data (not "test123" or "foo bar")
- Include all response headers that matter (Content-Type, pagination headers)
- Name examples descriptively: "Success - Active User" not "Example 1"
- Show edge cases: empty arrays, null fields, maximum pagination

### Pull Requests: Collaborative Documentation Review

When multiple people contribute to a collection, changes need review before they go live. Postman's pull request feature brings the code review workflow to API documentation.

**The Workflow:**
1. Fork the collection into your workspace
2. Make changes (add descriptions, update examples, restructure folders)
3. Create a pull request back to the source collection
4. Reviewers comment, request changes, or approve
5. The pull request is merged, updating the source collection

**Conflict Resolution:**
When two people edit the same request, Postman detects the conflict during merge. The reviewer can choose which version to keep or manually reconcile the differences. This is similar to git merge conflicts but scoped to individual requests and folders.

**Why This Matters:**
Without pull requests, documentation changes are a free-for-all. Anyone with editor access can modify any request. Pull requests add accountability — every change has an author, a reviewer, and a reason.

### Partner Workspaces: Secure External Sharing

Partner Workspaces let you share API collections with external organizations without giving them access to your internal workspace.

**Multi-Partner Mode:**
- Create one Partner Workspace per external partner, or use multi-partner mode to host multiple partners in a single workspace
- Each partner sees only the collections and environments you've explicitly shared
- Partners cannot see each other's activity or data

**Workspace Themes:**
- Customize the Partner Workspace appearance with your brand colors and logo
- This creates a professional, branded experience for external partners

**Visibility Controls:**
- Choose which collections, environments, and APIs are visible to partners
- Revoke access instantly when a partnership ends
- Audit trail tracks what partners accessed and when

**Use Cases:**
- Sharing API documentation with a contractor building an integration
- Giving a vendor read-only access to your API specs for compatibility testing
- Providing sandbox environments to potential API consumers during evaluation

## Activities

### PostVehicle Scenario

Continuing from Module 101-01, PostVehicle Enterprises has legacy API documentation for their User API scattered across a Confluence wiki, a Google Doc, and a README file in a GitHub repo. Your task is to consolidate, modernize, and share this documentation.

**Phase 1: Migrate Legacy User API Docs to a Postman Collection**

The User API has the following endpoints, currently documented only in a wiki page:
1. Review the legacy documentation (provided as a handout)
2. Create a new collection called "PostVehicle User API"
3. Add requests for each endpoint: GET /users, GET /users/{id}, POST /users, PUT /users/{id}, DELETE /users/{id}
4. Add markdown descriptions to the collection, each folder, and each request
5. Include parameter descriptions — what each query parameter and path parameter means, its type, and whether it's required

**Phase 2: Add Examples for Different Response Scenarios**

Each endpoint needs multiple examples to cover real-world scenarios:
1. For GET /users/{id}: add examples for "Success - Active User," "Success - Deactivated User," and "Not Found"
2. For POST /users: add examples for "Success - Created," "Validation Error - Missing Email," and "Conflict - Duplicate Email"
3. For DELETE /users/{id}: add examples for "Success - Deleted" and "Forbidden - Insufficient Permissions"
4. Name each example descriptively and use realistic data

**Phase 3: Create and Review Pull Requests**

Practice the collaborative review workflow:
1. Pair up with a teammate
2. Fork each other's User API collection
3. Each person adds or improves documentation on two endpoints
4. Create a pull request back to the source collection
5. Review your partner's pull request — leave at least one comment and one approval
6. Merge the approved pull request

**Phase 4: Set Up a Partner Workspace**

PostVehicle needs to share the User API with an external logistics partner:
1. Create a Partner Workspace called "PostVehicle - Logistics Partner"
2. Enable multi-partner mode
3. Share the User API collection (read-only)
4. Create a partner-specific environment with sandbox credentials
5. Verify the partner view — confirm they can see the collection but not internal workspace content

### Expected Outcome

By the end of this activity, each participant has:
- A fully documented collection with descriptions and multiple examples per endpoint
- Experience creating and reviewing pull requests on collections
- A Partner Workspace configured for secure external sharing

## Postman Features in This Module

### Collections
Collections serve as the documentation container. Participants learn that a well-structured collection is itself documentation — the folder hierarchy, request names, descriptions, and examples collectively tell the API's story without needing a separate docs site.

### API Documentation
Postman's auto-generated documentation view is the primary output. Participants see how descriptions, parameters, and examples render into a browsable documentation page. The key lesson: if you maintain the collection, the documentation maintains itself.

### Examples
Examples are the most hands-on feature in this module. Participants create multiple examples per request, learning to cover success cases, error cases, and edge cases. They see how examples appear in the documentation view and understand that examples are the most consumed part of any API documentation.

### Pull Requests
Pull requests introduce a review workflow for collection changes. Participants experience the full lifecycle: fork, edit, submit PR, review, merge. This feature is positioned as the answer to "who changed this endpoint and why?"

### Partner Workspaces
Partner Workspaces are the secure sharing mechanism for external parties. Participants configure multi-partner mode, set visibility controls, and verify the partner experience. This replaces the insecure alternative of emailing JSON files or creating shared Google Docs.

### Forking
Forking is used twice in this module: once for the pull request workflow (fork, edit, PR back) and once for partners who may need their own working copy of the collection. The dual use reinforces that forking is a general-purpose collaboration primitive.

## Facilitator Notes

**Timing:** 90 minutes total (20 for teaching documentation concepts, 50 for hands-on activities, 20 for review and discussion).

**Setup Requirements:**
- Prepare the legacy documentation handout (a deliberately messy wiki page with missing descriptions, outdated examples, and inconsistent formatting)
- Ensure participants are in pairs for the pull request activity
- Pre-create a Partner Workspace or have admin credentials ready to create one live
- Test the pull request merge flow — conflict resolution can be confusing on first encounter

**Tips:**
- The legacy documentation handout should be intentionally bad. Include a field that no longer exists, an endpoint with the wrong HTTP method, and a description that says "TODO: document this." This creates a visceral "aha" moment when participants see how easy it is for docs to rot.
- During the examples phase, push participants to go beyond "happy path" examples. Ask: "What happens when the user sends an empty body? What happens with an expired token?" These edge cases are where good documentation earns its keep.
- The pull request activity works best when pairs actually disagree on something. Encourage one person to restructure a folder while the other edits request descriptions — this increases the chance of a merge discussion, which is the learning moment.
- Partner Workspaces can feel abstract if participants don't have real external partners. Frame it as: "Your VP of Sales just signed a deal with a logistics company. They need API access by Friday. How do you give it to them without exposing your internal workspace?"

**Common Questions:**
- "Can partners edit the collection?" — Only if you give them Editor access. Read-only is the default and recommended starting point.
- "What's the difference between a comment and a pull request review?" — Comments are informal notes on any request. PR reviews are structured approvals/rejections tied to a specific set of changes.
- "Can I generate documentation from an OpenAPI spec?" — Yes, import the spec into Postman and it generates a collection with documentation automatically.
- "How do I know if my documentation is good?" — Ask someone who has never used the API to complete a task using only your docs. If they get stuck, the docs need work.

## Pain Points Addressed

**Legacy API Documentation Becomes Outdated Quickly**
Wiki pages, Google Docs, and README files are disconnected from the actual API. When an endpoint changes, someone has to remember to update every place the docs live. With Postman, the documentation is generated from the collection itself. Update the collection, and the docs update automatically. There is exactly one source of truth, and it is the same artifact developers use to test the API.

**No Collaborative Review Process for Documentation Changes**
Without pull requests, documentation changes happen unilaterally. A junior developer deletes a description, renames a folder, or changes an example — and no one notices until a partner complains. Pull requests add review gates: every change has an author, a reviewer, and a merge decision. This is the same workflow developers use for code, applied to API documentation.

**Sharing API Access with External Partners Requires Complex Access Control**
The traditional approach to sharing APIs with partners involves VPN access, shared credentials, emailed Postman collections, or public documentation sites with API key management. Partner Workspaces consolidate this into a single, governed mechanism: create a workspace, share specific collections, provide sandbox environments, and revoke access when needed. Multi-partner mode means you don't need a separate workspace for every external relationship.
