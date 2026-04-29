---
id: 101-01
title: "Discovering and Evaluating APIs"
program: 101
owner: Marcus Kidan
change_sensitivity: medium
status: current
last_updated: 2026-04-28
last_audited: 2026-04-28

postman_features:
  - Public API Network
  - Private API Network
  - Workspaces
  - Collections
  - Forking
  - Variables
  - Environments
  - Secret Variables

update_triggers:
  - "API Network UI changes"
  - "Workspace type changes"
  - "Variable scope changes"
  - "Forking workflow changes"
  - "Environment management updates"
---

## Overview

Hands-on workshop where participants join a fictional company (PostVehicle Enterprises) and learn to discover APIs through the Public API Network, evaluate them by forking collections, set up workspaces for team collaboration, and manage variables and environments for secure API access. These are v11 materials; the hub monitors for v12 changes.

## Learning Objectives

- Navigate the Postman API Network to discover and evaluate public APIs
- Fork collections into workspaces and use watches to track changes
- Set up environments with variables (including secret variables) to manage API credentials
- Understand workspace types (private, internal, team) and when to use each

## Key Elements

### The Public API Network: Your Starting Point

The Public API Network is Postman's marketplace for APIs. Think of it as an app store, but instead of downloading apps, you're discovering APIs you can integrate into your projects. The network lets you:

- **Browse by category** — Find APIs organized by domain (payments, weather, logistics, social media)
- **Search by keyword** — Look for specific functionality ("vehicle tracking," "customer management")
- **Evaluate before committing** — Read documentation, inspect request/response examples, and see usage statistics before you fork anything
- **Share your own APIs** — Publish collections to the network so other teams or the public can discover them

The key insight: you don't need to build everything from scratch. Thousands of production-ready APIs are already documented and ready to fork. The skill is knowing how to find, evaluate, and integrate them.

### Workspaces: Where Collaboration Happens

Workspaces in Postman are like project rooms. Each workspace has its own collections, environments, and team members. The type of workspace you choose determines who can see and access the work inside it.

**Private Workspace:**
- Only you can see it
- Use for: personal experimentation, testing credentials, exploring APIs before sharing with the team
- Analogy: Your personal desk — messy notes, half-finished ideas, no one watching

**Team Workspace:**
- Visible to everyone on your Postman team
- Use for: active projects, shared collections, team collaboration
- Analogy: The team conference room — everyone contributes, everyone sees the whiteboard

**Internal Workspace:**
- Visible to your entire organization (all teams)
- Use for: cross-team APIs, shared utilities, organization-wide standards
- Analogy: The company intranet — anyone in the company can browse and use what's published here

Choosing the wrong workspace type is a common mistake. A team workspace with sensitive credentials should not be internal. A reusable utility API buried in a private workspace helps no one.

### Collections: Executable Documentation

Collections are groups of API requests organized together. They serve as both documentation and runnable test suites. A well-structured collection tells a story:

- **Grouped by resource** — All `/customers` endpoints together, all `/orders` together
- **Ordered by workflow** — Create a customer, then retrieve the customer, then update, then delete
- **Documented inline** — Each request has descriptions, example responses, and parameter explanations

Collections are not static documentation files. They are live, executable artifacts. When someone forks your collection, they can immediately send requests and see real responses.

### Forking: Safe Experimentation

Forking creates your own copy of a collection. The original stays untouched, and you get a version you can modify, test against, and extend. Key behaviors:

- **Fork preserves lineage** — Postman tracks that your fork came from the original, so you can pull updates later
- **Watch for changes** — Enable watches on the source collection to get notified when the publisher updates it
- **Pull updates** — When the source changes, you can pull those changes into your fork (like a git pull)
- **Create pull requests** — If you improve the collection, you can submit a pull request back to the original owner

This workflow mirrors how open-source software development works. You don't modify someone else's code directly — you fork it, improve it, and offer your changes back.

### Variables: Managing Dynamic Values

Variables let you avoid hardcoding values into requests. Instead of typing `https://api.example.com` in every request URL, you store it in a variable called `{{base_url}}` and reference it everywhere.

**Variable Types and Scope Resolution:**

Postman resolves variables in a specific order (narrowest scope wins):

1. **Local variables** — Set in pre-request scripts, exist only for that single request execution
2. **Data variables** — Supplied by external data files during collection runs
3. **Environment variables** — Tied to a specific environment (dev, staging, prod)
4. **Collection variables** — Scoped to a single collection
5. **Global variables** — Available everywhere, across all collections and environments

If the same variable name exists at multiple levels, the narrowest scope wins. An environment variable named `api_key` overrides a global variable with the same name.

**Initial vs. Current Values:**

Every variable has two values:
- **Initial value** — Shared with your team when you share the environment. Safe to commit.
- **Current value** — Your local override. Never synced to the cloud. Use this for sensitive data.

This distinction is critical for security. You set the initial value to a placeholder (`your-api-key-here`) and put the real key in the current value. Your teammates do the same with their own keys.

### Secret Variables: Protecting Credentials

Secret variables add a layer of protection beyond current values. When a variable is marked as secret:

- The value is masked in the Postman UI (shown as dots)
- It cannot be exported with the environment
- It is not visible in shared workspace views
- Scripts can use it, but cannot log it to the console

Use secret variables for API keys, tokens, passwords, and any credential that should never appear in plaintext in the UI.

### Private API Network: Your Internal API Catalog

While the Public API Network is for discovering external APIs, the Private API Network is your organization's internal catalog. It answers the question every new team member asks: "What APIs do we have?"

- **Centralized discovery** — All internal APIs in one searchable place
- **Governed access** — Admins control what gets published and who can see it
- **Standardized documentation** — Every API follows the same format, making evaluation consistent
- **Reduced duplication** — Teams discover existing APIs instead of building redundant ones

## Activities

### PostVehicle Scenario

You've just joined PostVehicle Enterprises, a fictional vehicle fleet management company. Your team manages a fleet of delivery vehicles and needs to integrate with several vendor APIs for tracking, maintenance, and customer management.

**Phase 1: Discover and Fork the Customer API**

Your first task is finding and evaluating a vendor's Customer API:

1. Navigate to the Public API Network
2. Search for the Customer API collection (pre-published for the workshop)
3. Review the collection documentation — endpoints, authentication requirements, example responses
4. Fork the collection into your team workspace
5. Enable a watch on the source collection to track future changes

**Phase 2: Set Up Secure Authentication**

The Customer API requires an API key. Your team lead has given you credentials, but you need to store them securely:

1. Create a new environment called "PostVehicle - Dev"
2. Add a variable `base_url` with the API's base URL
3. Add a variable `api_key` — set the initial value to `your-key-here` and the current value to the actual key provided
4. Mark the `api_key` variable as a secret variable
5. Update the collection's authorization to use `{{api_key}}`
6. Send a test request to verify authentication works

**Phase 3: Collaborate Through Workspace Sharing**

Your teammate needs access to the same collection and environment:

1. Invite a teammate to your workspace (assign Editor role)
2. Have them fork the collection into their own workspace for experimentation
3. Add a comment to a request explaining a quirk you discovered ("Note: the /customers endpoint requires pagination — max 50 per page")
4. Your teammate replies to the comment with their own findings

**Phase 4: Publish to the Private API Network**

Now that the Customer API integration is validated, publish it for the rest of PostVehicle:

1. Add metadata and descriptions to the collection
2. Publish the collection to the Private API Network
3. Categorize it under "Vendor Integrations"
4. Verify that other teams can discover it by searching the Private API Network

### Expected Outcome

By the end of this activity, each participant has:
- A workspace with a forked and configured collection
- An environment with properly scoped variables (including secrets)
- Experience collaborating through comments and workspace sharing
- An API published to the Private API Network

## Postman Features in This Module

### Public API Network
Used as the primary discovery mechanism. Participants search for, evaluate, and fork APIs from the network. The network serves as the entry point for the entire PostVehicle scenario — without it, finding the vendor API would require documentation hunting across wikis and Slack channels.

### Private API Network
Used at the end of the module to publish the validated integration internally. Demonstrates the full lifecycle: discover externally, validate, then catalog internally so other teams don't repeat the same evaluation work.

### Workspaces
Participants create and configure workspaces, choosing appropriate types for their use case. The module emphasizes that workspace type is a deliberate decision — private for experimentation, team for collaboration, internal for cross-team sharing.

### Collections
The Customer API collection is the central artifact. Participants interact with it as executable documentation — sending requests, reading inline descriptions, and understanding how grouped requests tell a workflow story.

### Forking
Forking is the mechanism for safe adoption. Participants fork the vendor collection, preserving lineage and enabling watches. The fork-watch-pull workflow is positioned as the standard way to consume shared collections.

### Variables
Variables are introduced as the solution to hardcoded values and credential management. Participants set up collection variables, environment variables, and learn scope resolution through hands-on configuration.

### Environments
Environments are the container for deployment-specific variables. The "PostVehicle - Dev" environment demonstrates how the same collection works across different contexts by swapping environments.

### Secret Variables
Secret variables are introduced specifically for API key protection. Participants see the difference between regular and secret variables in the UI and understand when to use each.

## Facilitator Notes

**Timing:** 90 minutes total (20 for teaching key concepts, 50 for hands-on activities, 20 for discussion and wrap-up).

**Setup Requirements:**
- Pre-publish the Customer API collection to the Public API Network (or use a team workspace as a stand-in)
- Ensure all participants have Postman accounts with team-level access
- Prepare API keys for distribution (one per participant or shared test key)
- Test the full activity flow beforehand — UI button locations and flows may shift between Postman versions

**Tips:**
- The variable scope resolution order is the concept most participants struggle with. Use a visual diagram showing the layers (global at the bottom, local at the top) and emphasize "narrowest wins."
- The initial vs. current value distinction is unintuitive at first. Ask participants: "If you share this environment with a new hire, what should they see?" That clarifies why initial values should be safe placeholders.
- Workspace type selection often sparks good discussion. Ask: "What happens if you put production API keys in a team workspace? What about an internal workspace?" Let them reason through the security implications.
- If time is short, Phase 4 (Private API Network publishing) can be demonstrated rather than hands-on.

**Common Questions:**
- "Can I have multiple environments active?" — No, only one environment is active at a time, but you can switch quickly using the environment dropdown.
- "What happens if I delete a forked collection?" — The source collection is unaffected. Your fork is gone, but you can re-fork.
- "Can I make a variable secret after creating it?" — Yes, you can toggle the secret flag on existing variables at any time.
- "Who can see my current values?" — No one. Current values are local to your Postman instance and never synced to the cloud.

## Pain Points Addressed

**API Discovery Is Hard Without a Central Catalog**
Teams waste hours searching Slack threads, wikis, and email chains to find existing APIs. The Public API Network provides a searchable, browsable catalog with live documentation. For internal APIs, the Private API Network eliminates the "I didn't know that API existed" problem that causes teams to build duplicate integrations.

**Credential Sharing via Slack/Email Is Insecure**
Pasting API keys into Slack messages or email creates a permanent, searchable record of sensitive credentials. Environment variables with the secret flag keep credentials local to each user's Postman instance. The initial/current value split means shared environments contain safe placeholders, not real keys.

**Onboarding New Team Members to Existing APIs Takes Too Long**
A new hire joining a project with 15 API integrations faces days of "where do I find the docs for X?" With workspaces, forked collections, and environments already configured, onboarding becomes: join the workspace, clone the environment, fill in your credentials, send a request. Minutes instead of days.
