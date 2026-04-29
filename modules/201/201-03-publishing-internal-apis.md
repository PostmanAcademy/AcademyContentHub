---
id: 201-03
title: "Publishing and Managing Internal APIs"
program: 201
owner: Marcus Kidan
change_sensitivity: medium
status: current
last_updated: 2026-04-28
last_audited: 2026-04-28

postman_features:
  - Private API Network
  - Workspaces
  - Collections
  - Environments
  - Role-Based Access Control

update_triggers:
  - "Private API Network UI changes"
  - "Role or permission changes"
  - "Publishing workflow changes"
  - "Folder management updates"
---

## Overview

Covers publishing APIs to the Private API Network for internal discoverability, managing folder structures and permissions, using role-based access control (API Network Manager, Folder Manager roles), handling publish/approval workflows, and sharing API resources across the organization. These are v11 materials; the hub monitors for v12 changes.

## Learning Objectives

- Publish collections and environments to the Private API Network with proper folder organization
- Understand the roles and permissions model for the API Network (Super Admin, API Network Manager, Folder Manager)
- Navigate the approval workflow for publishing to restricted network folders
- Broadcast API updates to the team using workspace update announcements

## Key Elements

### Private API Network: The Internal API Catalog

The Private API Network is Postman's internal marketplace for APIs. It serves as a central catalog where teams can publish, discover, and consume APIs within the organization. Unlike the public API Network, the Private API Network is visible only to members of your Postman team.

Think of it as the company intranet for APIs. Without it, discovering internal APIs requires asking around on Slack, searching Confluence, or hoping someone documented it somewhere. With the Private API Network, there is one place to look. If it is not in the network, it does not exist (or at least, it has not been shared yet).

The network supports collections, APIs, workspaces, and environments. When you publish a collection to the network, consumers can fork it directly into their own workspace and start making requests immediately. No email, no file sharing, no "can you send me the Postman export?"

### Publishing Workflow

Publishing to the Private API Network follows a specific sequence:

1. **Navigate to the collection overview** — Open the collection you want to publish and go to its overview page.
2. **Click "Publish to API Network"** — This opens the publishing dialog.
3. **Select the target folder** — Choose which folder in the network hierarchy this API should live in (e.g., "PostVehicle / Account APIs").
4. **Add environments** — Include any environments that consumers will need (e.g., "PostVehicle Dev" with base URLs and non-secret variables).
5. **Add metadata** — Title, description, and any relevant tags for discoverability.
6. **Submit** — If the target folder is open, the API is published immediately. If the folder is restricted, a publish request is sent to the Folder Manager for approval.

The key insight is that publishing is not just "making something visible." It is a deliberate act of sharing a curated, documented resource with the organization. The folder structure, metadata, and included environments all contribute to whether the published API is actually usable by consumers.

### Role-Based Access Control

The Private API Network uses a layered permissions model with three key roles:

**Super Admin**
- Has full control over the entire Private API Network
- Can create and delete any folder
- Can approve or deny any publish request
- Can assign API Network Manager and Folder Manager roles
- Typically held by platform team leads or API governance owners

**API Network Manager**
- Can create top-level folders and organize the network structure
- Can approve or deny publish requests to any folder they manage
- Can assign Folder Manager roles to specific folders
- Cannot delete the entire network or change Super Admin settings
- Typically held by team leads or senior architects

**Folder Manager**
- Can manage a specific folder (and its subfolders)
- Can approve or deny publish requests to their folder
- Can create subfolders within their folder
- Cannot affect other parts of the network
- Typically held by team members responsible for a specific API domain (e.g., "Account APIs," "Payment APIs")

This layered model enables decentralized governance. The Super Admin sets up the top-level structure. API Network Managers organize their domains. Folder Managers handle day-to-day publishing approvals within their area. No single person is a bottleneck.

### Approval Workflow

When a team member submits a publish request to a restricted folder, the following workflow begins:

1. **Request submitted** — The publisher selects a folder and clicks publish. If the folder requires approval, the request enters a pending state.
2. **Folder Manager notified** — The Folder Manager receives a notification that a publish request is waiting.
3. **Review** — The Folder Manager reviews the collection, environments, and metadata. They check for completeness, naming conventions, and documentation quality.
4. **Approve or Deny** — If approved, the API appears in the folder immediately. If denied, the publisher receives feedback on what needs to change.
5. **Resubmit** — The publisher addresses feedback, updates the collection, and submits a new publish request.

This workflow prevents the network from becoming a dumping ground of half-documented, poorly named APIs. It ensures quality and consistency — the network is a curated catalog, not a file share.

The approval workflow also creates a lightweight governance process. Folder Managers can enforce naming conventions, require documentation completeness, and reject collections that do not include environments. This is governance without bureaucracy.

### Workspace Updates and Announcements

Publishing to the network makes an API discoverable, but teams also need to know when updates happen. Workspace updates and announcements serve this purpose:

- **Workspace changelog** — Every change to a collection, environment, or API in a workspace is logged. Team members can see what changed, when, and by whom.
- **Comments** — Add comments to collections or specific requests to explain changes, flag breaking updates, or provide migration guidance.
- **Update announcements** — When a significant change is made (new version, breaking change, deprecation), publish a workspace update that notifies all workspace members.

The combination of the Private API Network (for discovery) and workspace updates (for change awareness) creates a complete communication loop. Teams discover APIs in the network and stay informed about changes through workspace notifications.

### Folder Management

The folder structure of the Private API Network determines how consumers browse and discover APIs. A well-organized structure mirrors the organization's API landscape:

```
PostVehicle/
  Account APIs/
    Account Management
    Authentication
  Vehicle APIs/
    Vehicle Registration
    Remote Services
  Billing APIs/
    Subscriptions
    Payments
```

**Creating nested folders** — API Network Managers and Folder Managers can create subfolders to add granularity. Start broad (by product or domain) and add depth as the catalog grows.

**Assigning Folder Managers** — Each folder can have its own Folder Manager. This distributes governance — the Account team manages the Account APIs folder, the Vehicle team manages Vehicle APIs, and so on.

**Naming conventions** — Establish and enforce consistent naming. "Account Management API" is better than "acct-mgmt-v2-final." The network is a public-facing catalog (internal public), and naming matters for discoverability.

## Activities

### PostVehicle Scenario: Publish and Organize the API Network

**Setup:** Participants have completed 201-01 (prototyping) and 201-02 (workflows). They now have a workflow collection and an Account API prototype that need to be published to the Private API Network for the broader PostVehicle organization.

**Phase 1: Create the Folder Structure (10 min)**
- As the API Network Manager, create the following folder structure in the Private API Network:
  - `PostVehicle/` (top-level folder)
    - `Account APIs/` (subfolder)
    - `Workflows/` (subfolder)
    - `Vehicle APIs/` (subfolder — empty for now)
- Discuss why this structure was chosen: organized by domain, with a separate folder for cross-API workflows.

**Phase 2: Assign Roles (10 min)**
- Assign a Folder Manager to the "Account APIs" folder (one participant plays this role)
- Assign a different Folder Manager to the "Workflows" folder
- Discuss the responsibility: Folder Managers approve what goes into their folder and maintain quality
- Demonstrate that a Folder Manager for "Account APIs" cannot approve or manage "Workflows"

**Phase 3: Publish the Workflow Collection (15 min)**
- One participant publishes the "Register and Subscribe Workflow" collection (from 201-02) to the Workflows folder
- Include the "PostVehicle Dev" environment
- Add a description: "End-to-end workflow for user registration and service subscription"
- If the folder requires approval, the Folder Manager reviews and approves

**Phase 4: Walk Through Approve/Deny/Resubmit (15 min)**
- A second participant publishes the Account API prototype (from 201-01) to the "Account APIs" folder
- The Folder Manager intentionally denies the request with feedback: "Missing endpoint documentation — please add descriptions to all requests"
- The publisher updates the collection (adds descriptions using Postbot) and resubmits
- The Folder Manager approves on the second submission
- Discuss what happened: this is governance in action. The deny-and-resubmit cycle ensures quality.

**Phase 5: Demonstrate Role-Based Restrictions (10 min)**
- A participant who is not a Folder Manager or API Network Manager tries to create a new folder — they cannot
- A Folder Manager for "Account APIs" tries to approve a request in "Workflows" — they cannot
- Discuss: these restrictions prevent chaos. As the network grows to hundreds of APIs, role boundaries keep it manageable.

**Phase 6: Broadcast Updates (10 min)**
- Add a comment to the published workflow collection explaining a design decision
- Publish a workspace update announcing: "Account API and Registration Workflow now available in the Private API Network"
- Show how workspace members see the notification

**Expected Outcome:** A structured Private API Network with published collections, demonstrated role-based governance, and a completed approve/deny/resubmit cycle.

## Postman Features in This Module

### Private API Network
The central feature of this module. Participants learn to publish collections and environments, navigate the folder structure, and understand how the network serves as the organization's internal API catalog. The emphasis is on curation — the network is only valuable if what is published there is complete, documented, and discoverable.

### Workspaces
Workspaces are the source of what gets published. The relationship between workspace (where work happens) and network (where work is shared) is a key concept. Teams build in workspaces and publish to the network. Updates flow through workspace notifications.

### Collections
Collections are the primary artifact published to the network. The quality of the published collection — documentation, naming, examples, included environments — determines whether consumers can actually use it.

### Environments
Environments published alongside collections give consumers the configuration they need to start making requests immediately. Without the environment, a consumer has to figure out base URLs, variable names, and configuration on their own.

### Role-Based Access Control
The roles model (Super Admin, API Network Manager, Folder Manager) distributes governance across the organization. This module demonstrates how roles work in practice — who can create folders, who can approve publications, and where the boundaries are.

## Facilitator Notes

**Timing:** 70-80 minutes total (10 min folder setup, 10 min roles, 15 min publishing, 15 min approve/deny cycle, 10 min role restrictions, 10 min announcements, 10 min discussion).

**Prerequisites:** Participants should have collections and environments ready from 201-01 and 201-02. If running this module standalone, provide pre-built collections for publishing.

**Team Plan Required:** The Private API Network and role-based access control require a Postman Team plan or higher. Verify participants have appropriate access before the session.

**Tips:**
- The approve/deny/resubmit cycle is the most engaging part. Make it theatrical — the Folder Manager should be visibly critical ("Where are the endpoint descriptions? I can't approve this."). This makes the governance process feel real and memorable.
- If participants ask "Why not just share the workspace URL?" — explain that the network is a curated catalog. Sharing a workspace URL gives someone access to everything in that workspace, including drafts and experiments. The network lets you publish only what is ready for consumption.
- The folder structure discussion can generate strong opinions. Some teams prefer organizing by product, others by team, others by API type. There is no single right answer — the point is that some structure is better than no structure.
- Role assignment can feel abstract until participants actually hit a permission boundary. The "try to do something you can't" exercise in Phase 5 makes the roles concrete.

**Common Questions:**
- "Can I unpublish something?" — Yes, you can remove a collection from the network. It stays in the workspace but is no longer discoverable in the network.
- "What happens if the source collection changes?" — The network listing reflects the current state of the collection. Updates are automatic — there is no separate "republish" step for content changes (but significant updates should be announced).
- "Can external partners see the Private API Network?" — No. The Private API Network is visible only to your Postman team members. External sharing requires Partner Workspaces or the public API Network.
- "How many Folder Managers can a folder have?" — Multiple. This allows for redundancy and coverage across time zones.

**v11 Note:** These materials reflect v11 Private API Network UI and role definitions. The hub monitors for v12 changes that may affect the publishing workflow, role names or permissions, or folder management capabilities.

## Pain Points Addressed

**Internal APIs Are Scattered Across Workspaces with No Central Catalog**
- Problem: Teams build APIs in their own workspaces, but no one outside the team knows the APIs exist. Discovery relies on word of mouth, Slack messages, or outdated wiki pages.
- Solution: The Private API Network provides a single, browsable catalog of all internal APIs. If it is published to the network, anyone on the team can find it, fork it, and start using it.
- Postman Feature: Private API Network, Collections

**No Governance Over What Gets Published to the Internal API Network**
- Problem: Without approval workflows, the network fills up with incomplete collections, duplicate APIs, and undocumented endpoints. Consumers lose trust in the catalog.
- Solution: Folder Managers review and approve publish requests. The deny-and-resubmit cycle enforces quality standards. Role-based access control prevents unauthorized folder creation and keeps the structure clean.
- Postman Feature: Role-Based Access Control, Private API Network

**Teams Don't Know When New APIs or Updates Are Available**
- Problem: An API is published, but no one is told. Or an API is updated with a breaking change, and consumers find out when their integration breaks.
- Solution: Workspace updates and comments notify team members of changes. Publishing announcements proactively inform the organization about new APIs. The combination of discoverability (network) and awareness (notifications) keeps everyone informed.
- Postman Feature: Workspaces, Private API Network
