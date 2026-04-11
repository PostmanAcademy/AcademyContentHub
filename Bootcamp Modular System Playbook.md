# Postman Fundamentals Bootcamp: Modular System Playbook

> **Purpose:** A living system for keeping the Postman new-hire bootcamp current, modular, scalable, and reproducible — even as Postman ships daily and weekly releases.
>
> **Owner:** Marcus Kidan | **Last Updated:** April 10, 2026

---

## How This System Works

The bootcamp is no longer a single monolithic slide deck. It's a **set of independent, topic-based modules** — each one owns a specific slice of content, references specific Postman features, and can be updated without touching anything else.

Three things keep it alive:

1. **The Module Architecture** — 12 topic modules, each self-contained with slides, speaker notes, activities, and a list of Postman features it depends on.
2. **The Module Registry** — An Airtable tracker that records each module's status, last update, feature dependencies, and change sensitivity.
3. **The Update Workflow** — A scheduled Cowork task that monitors Postman's changelog, flags which modules are affected, and drafts updated content.

---

## The Module Architecture

### Design Principles

These principles emerged from synthesizing the V11 deck, your V12 plans, the Bootcamp Review doc, the Refresh Guide, and your API Fundamentals Field Guide.

**Interleaved, not lecture-then-lab.** Every module weaves concept → metaphor → activity → reflection. No more "theory block then practice block." This was the core insight from your Bootcamp Review: reduce cognitive load, increase aha moments.

**One metaphor system, used everywhere.** The City Metaphor from your Field Guide is the backbone. The internet is a city, APIs are buildings, requests are forms, Postman is the city management platform. Every module speaks this language. The restaurant metaphor from V11 can still appear as a "familiar on-ramp" in Module 2, but the city is the system of record.

**Each module is a self-contained unit** with: a topic scope, learning objectives, slide content, speaker notes, at least one activity or discussion prompt, a list of Postman product features it references, and a "change sensitivity" rating.

**Pain points are threaded, not siloed.** Rather than a single "Pain Points" section (as in V11 slide 22), each module surfaces the relevant pain point in context — discovery pain lives in the module about APIs, testing pain lives in the module about how APIs work, etc. This was a key V12 insight.

---

### The 12 Modules

Each module maps to one or more layers from your Field Guide, content from V11/V12, and hands-on activities from the Refresh Guide.

---

#### Module 1: Welcome & Psychological Safety
**Field Guide Layers:** None (facilitation)
**V11 Slides:** 1-4 | **V12 Slides:** 1-3
**Change Sensitivity:** 🟢 Low — Rarely needs product updates

**Content scope:** Establishing safety, introductions, the "future tech" icebreaker, setting expectations. This isn't a coding class — it's about shared vocabulary and collaboration.

**Key elements:**
- "This is a collaboration class" framing
- Go-around: name, role, where you flew in from
- Icebreaker: "What technology made you feel like you were in the future?"
- Agenda overview: what we'll cover and why

**V12 addition:** Frame the day's arc: "Postman has evolved from a collaboration-focused tool to an AI-native development platform. Today is about understanding that shift and what it means for the people you'll work alongside."

**Postman features referenced:** None
**When to update:** Only when the bootcamp's strategic framing changes (e.g., a major company pivot)

---

#### Module 2: The Internet & APIs
**Field Guide Layers:** 01 (The Internet as a City), 02 (APIs as Buildings)
**V11 Slides:** 5-8 | **V12 Slides:** 4-6
**Change Sensitivity:** 🟢 Low — Foundational concepts

**Content scope:** What the internet is, what APIs are, the City Metaphor foundation. Two definitions of API (technical + human). The Bezos Mandate story. "Apps use more than one building."

**Key elements:**
- City Metaphor introduction: internet = city, HTTP = roads, URLs = addresses, browser = vehicle
- Two definitions: technical ("a defined contract between two pieces of software") and human ("the apps your apps use")
- The Bezos Mandate as origin story for why APIs matter at scale
- Netflix example: authentication, catalog, streaming, recommendations, billing = 5 buildings
- The building types from Field Guide Layer 02 (Bank = Stripe, Hospital = EHR, Library = Wikipedia, etc.)

**Activity:** "What APIs (buildings) would you need for a weather app?" — gets the class thinking like city planners.

**Pain point threaded:** Discovery — "How do you even find the right building in a city of millions?"

**Postman features referenced:** None directly (conceptual module)
**When to update:** If Postman's company narrative about APIs fundamentally shifts

---

#### Module 3: How APIs Work
**Field Guide Layers:** 03 (Requests as Forms & Receptionists)
**V11 Slides:** 9-10, 14-17 | **V12 Slides:** 10, 12-14
**Change Sensitivity:** 🟢 Low — Foundational concepts

**Content scope:** Client-server model, CRUD, HTTP methods, request/response anatomy, URLs, status codes. The "you're already using all of this" reveal.

**Key elements:**
- The receptionist metaphor: every building has a front desk, you fill out forms (requests), receptionist processes them
- CRUD: the four things you can do with data (Create, Read, Update, Delete)
- HTTP methods: GET, POST, PUT, PATCH, DELETE — mapped to receptionist interactions
- Request anatomy from Field Guide: body = filled-out form, headers = envelope, query params = sticky notes
- Status codes: 200 (approved), 404 (room doesn't exist), 401 (no badge), 500 (building on fire)
- "You're already using this": scrolling social media = CRUD, visiting a URL = GET request
- URL anatomy: youtube.com/results?search_query=postman → server/endpoint/query

**Activity:** "What HTTP method is liking a post? What about unliking?" — multiple right answers, reinforces design choices.

**Pain point threaded:** Testing — "How do you know the receptionist is giving you the right response?"

**Postman features referenced:** None directly
**When to update:** If new HTTP methods or API patterns become mainstream

---

#### Module 4: API Design & Architecture
**Field Guide Layers:** 02 (Inside the Building — endpoints, versioning, monolith vs. microservices), 05 (Documentation)
**V11 Slides:** 13-14 | **V12 Slides:** 8-10
**Change Sensitivity:** 🟡 Medium — Postman design features evolve

**Content scope:** REST as a design choice (not hard science), the fork analogy, API-first vs. code-first (two restaurants activity), specs vs. documentation, monolith vs. microservices.

**Key elements:**
- "Design choices, not hard science" — the fork-in-the-drawer analogy
- REST as "the sit-down restaurant" of API styles (with awareness of SOAP, gRPC, GraphQL)
- Two Restaurants activity: Menu First vs. Sell Tomorrow → reveals API-first vs. code-first
- Specs vs. Docs from Field Guide: "A spec is the architectural blueprint filed with the city. Docs are the brochure in the lobby."
- Monolith vs. microservices: department store vs. specialist district
- API versioning: "building renovations" — /v1/ stays open while /v2/ is built

**Activity:** Two Restaurants — class builds pros/cons for Menu First and Sell Tomorrow, then reveals the connection to API development approaches.

**Pain points threaded:** Design — "Design decisions must happen before committing to development." Documentation — "Classic hard-coded docs vs. living documentation."

**Postman features referenced:** API Builder/Editor, Mock Servers, OpenAPI spec support
**When to update:** When Postman ships new design or spec-related features (e.g., new spec formats, design tooling changes)

---

#### Module 5: Security & Authentication
**Field Guide Layers:** 04 (Security)
**V11 Slides:** (implicit in hands-on) | **V12 Slides:** (not yet explicit)
**Change Sensitivity:** 🟡 Medium — Auth features change periodically

**Content scope:** Why APIs need security, API keys, OAuth, authentication vs. authorization.

**Key elements:**
- From Field Guide: API keys = building access badge, OAuth = valet parking ticket, JWT = time-stamped visitor pass
- Auth vs. authz: "The badge gets you in the building (authentication). Your clearance level determines which floors you can access (authorization)."
- Rate limiting: "The building has a maximum occupancy"
- CORS: "Some buildings only accept visitors from approved neighborhoods"
- Practical: "When you call an API and get a 401, you forgot your badge"

**Pain point threaded:** Security governance at scale — "How does an organization ensure every building has proper security?"

**Postman features referenced:** Auth tab, API key management, OAuth 2.0 flows, Vault integration
**When to update:** When Postman adds new auth types, changes auth UI, or adds security governance features

---

#### Module 6: Git & Version Control
**Field Guide Layers:** 08 (Dev Tools — partial)
**V11 Slides:** N/A (new) | **V12 Slides:** 15-16
**Change Sensitivity:** 🔴 High — Native Git is a V12 flagship feature

**Content scope:** What Git is and why it matters, core Git concepts, why Postman went Git-native.

**Key elements:**
- Architects-on-blueprints metaphor: Git lets every engineer work on their own copy, tracks every change, provides structured process for combining work
- Core terms: repo, branch, commit, pull request, merge
- Why this matters for Postman: "In V12, Git is native. Postman now lives in the branching workflow engineers already use. No context switching."
- Connect to the city: "Git is the city's version control system — every blueprint change is tracked, every renovation is proposed and reviewed before construction begins"

**Postman features referenced:** Native Git integration, branching, pull requests for API changes, version history
**When to update:** Every time Postman ships Git-related features (high frequency in V12 era)

---

#### Module 7: The Developer Experience
**Field Guide Layers:** 08 (Dev Tools), 10 (Personas)
**V11 Slides:** N/A (new) | **V12 Slides:** 17-19
**Change Sensitivity:** 🟡 Medium — Evolves as Postman's dev tooling changes

**Content scope:** A day in the life of a software engineer, inner vs. outer dev loop, what engineers care about, the five personas.

**Key elements:**
- Day in the life: reading code, writing code, testing, debugging, code review, meetings, documentation
- Inner dev loop (architect at drafting table): write → run → test → fix → repeat. Must be fast. Every tool-switch costs flow.
- Outer dev loop (review board): code review, CI/CD, staging, QA, releases. Where collaboration and process live.
- What engineers care about: speed of feedback, reducing context switching, not breaking things, ownership, trust in tooling
- Five personas from Field Guide Layer 10: API Developer, API Consumer, Platform/Architect, QA/Test Engineer, Technical Writer

**Activity:** "Connect these engineering activities to Postman features" — class maps each day-in-the-life moment to a Postman capability.

**Postman features referenced:** Postman CLI, CI/CD integration, workspace collaboration, environments
**When to update:** When Postman adds features targeting developer workflow (CLI changes, IDE integrations, etc.)

---

#### Module 8: AI & Agents
**Field Guide Layers:** 06 (MCP Servers — Underground Highway)
**V11 Slides:** N/A (new) | **V12 Slides:** 20
**Change Sensitivity:** 🔴 High — Fastest-moving area of the product

**Content scope:** What LLMs are (briefly), what makes something "agentic," MCP servers, Postman's AI capabilities.

**Key elements:**
- LLMs in plain terms: pattern recognition at massive scale, probabilistic not deterministic
- Agentic capabilities: when AI can use tools, not just generate text
- MCP from Field Guide Layer 06: "The underground highway system. MCP servers allow AI agents to directly access tools, data sources, and services through a standardized protocol — without needing to surface through the regular front door."
- Postman AI: Agent mode reads code, writes tests, generates stubs, debugs failures, creates mocks, generates documentation

**Postman features referenced:** Agent mode, AI test generation, AI debugging, AI documentation generation, MCP server support
**When to update:** With virtually every release — this is the highest-velocity area. Flag any AI/agent/MCP changelog entries.

---

#### Module 9: The Postman Platform
**Field Guide Layers:** 07 (Postman — City Management Platform)
**V11 Slides:** 18-23 | **V12 Slides:** 21-22
**Change Sensitivity:** 🔴 High — Core product capabilities

**Content scope:** What Postman is (official definition + "architectural design software for a digital world"), the full product surface, customer stories.

**Key elements:**
- Official definition: "An AI-native, collaborative platform for development, testing, monitoring, management, and distribution of APIs and Services"
- The architecture analogy: "Postman is like architectural design software for a digital world — it helps visualize something that either already exists or will exist, and allows people from all disciplines to engage"
- Product surface from V12: AI + Agent Mode, Native Git, Local Mock Servers, Postman CLI, API Catalog, Insights, SDK Distribution (LibLab)
- PayPal case study video: reduced time-to-first-call to one minute
- From Field Guide: "Postman is the shared city management layer — Platform uses it for governance, QA uses it for testing, Developers use it for building, Writers use it for documentation"

**Pain points consolidated:** Documentation (AI-generated docs from code), Discovery (API Catalog + Insights), Testing (AI test generation + CLI in CI), Design (local mock servers + AI stubs)

**Postman features referenced:** All major product areas — this is the "everything" module
**When to update:** With any major product launch, rebrand, or capability addition

---

#### Module 10: Hands-On Lab — The Grocery Store
**Field Guide Layers:** Practical application of all
**Source:** Postman New Hire Bootcamp Refresh Guide
**Change Sensitivity:** 🔴 High — Depends on live Postman UI and features

**Content scope:** The Digital Grocery Store project — a narrative-driven, hands-on sequence where the class helps a fictional grocery store modernize through APIs.

**Sub-modules (can be run together or independently):**

- **Lab 10a: The Consumer** — Find and use an existing API. Send GET/POST requests, learn the Postman UI, authenticate with an API key. Story: "The store needs a digital customer list."
- **Lab 10b: The Teammate** — Create a workspace, fork a collection, invite collaborators, navigate Postman. Story: "Customers need to buy things — bring in a friend to help."
- **Lab 10c: The Designer** — Use Agent mode to generate an API collection from natural language. Story: "The store wants a Loyalty Program — time to design one."
- **Lab 10d: The Prototyper** — Create a mock server, use environments and variables. Story: "The design looks great — now make it feel real before spending money on developers."
- **Lab 10e: The Publisher** — Explore the API Network, publish to Private API Network, hand off to dev team. Story: "The owner approved the project — hand it off."

**Postman features referenced:** Collections, Workspaces, Forking, Auth, Agent Mode, Mock Servers, Environments, Variables, API Network, Partner Workspaces
**When to update:** Whenever the Postman UI changes (button locations, naming, flows), when workspace types change, when Agent mode capabilities change

---

#### Module 11: API Lifecycle & Governance
**Field Guide Layers:** 11 (Example API Lifecycle)
**V11 Slides:** 23 | **V12 Slides:** (implicit)
**Change Sensitivity:** 🟡 Medium

**Content scope:** The six-phase API lifecycle, who's involved at each phase, how Postman supports each phase.

**Key elements:**
- Six phases: Use Case & Ideation → Design & Definition → Development → Testing & QA → Deployment & Integration → Publish & Discover
- Roles at each phase (from V11 slide 23): Product Managers, Architects, Developers, QA Engineers, DevOps, Tech Writers
- Postman capabilities at each phase
- Governance: API Catalog, Insights, security rules

**Postman features referenced:** Full lifecycle tooling, API Catalog, Insights, Governance rules, Workspaces
**When to update:** When Postman adds governance features, changes lifecycle positioning, or adds new persona-targeted capabilities

---

#### Module 12: Wrap-Up & Bridge to Postman for Postmanauts
**Field Guide Layers:** Quick Translations
**Change Sensitivity:** 🟢 Low

**Content scope:** Recap, Q&A, connecting the bootcamp to ongoing learning.

**Key elements:**
- Quick Translations from Field Guide: a rapid-fire reference card mapping city metaphors to technical terms
- "What to do next": how to stay current with Postman for Postmanauts (the just-in-time program for all employees)
- Resources: Field Guide link, Postman Learning Center, internal Slack channels
- Feedback collection

**Postman features referenced:** None directly
**When to update:** When Postman for Postmanauts program changes, or when new learning resources are available

---

## Module Registry (Airtable)

Each module is tracked in an Airtable base with the following fields:

| Field | Purpose |
|-------|---------|
| **Module ID** | M01 through M12 |
| **Module Name** | Human-readable name |
| **Change Sensitivity** | 🟢 Low / 🟡 Medium / 🔴 High |
| **Postman Features Referenced** | List of specific product features this module teaches |
| **Last Content Update** | Date the slides/notes were last revised |
| **Last Audit Date** | Date someone last checked this module against current product |
| **Status** | ✅ Current / ⚠️ Needs Review / 🔄 Update In Progress / ❌ Outdated |
| **Flagged Changes** | Specific changelog items that triggered a review |
| **Owner** | Who's responsible for this module |
| **Notes** | Free-text for context |

---

## The Update Workflow

### How Changes Flow Through the System

```
Postman Release (changelog / Slack / internal docs)
        ↓
  Cowork Scheduled Task (weekly)
  - Fetches latest changelog entries
  - Compares against module feature dependencies
  - Flags affected modules
        ↓
  Module Registry Updated
  - Affected modules marked "⚠️ Needs Review"
  - Flagged changes noted with specific changelog items
        ↓
  Content Review (human + Cowork)
  - Review flagged modules
  - Cowork drafts updated slide content, speaker notes, activities
  - Human reviews and approves
        ↓
  Module Updated
  - Slides revised
  - Registry updated with new date and status
  - Change log entry added
```

### Audit Cadence

| Sensitivity | Audit Frequency | Rationale |
|------------|----------------|-----------|
| 🔴 High | Weekly | AI, Git, Platform modules change with nearly every release |
| 🟡 Medium | Bi-weekly | Design, Security, Dev Experience shift periodically |
| 🟢 Low | Monthly | Foundational concepts and facilitation rarely need updates |

### What Cowork Does Automatically

1. **Monitors changelog** — Scheduled task fetches Postman release notes weekly
2. **Flags modules** — Compares changelog against each module's "Postman Features Referenced" list
3. **Drafts updates** — For flagged modules, generates draft slide content and speaker note revisions
4. **Updates registry** — Marks affected modules in Airtable as "Needs Review"

### What Humans Do

1. **Review flags** — Check Cowork's flags and drafts for accuracy
2. **Approve or revise** — Accept drafts or adjust based on pedagogical judgment
3. **Test in delivery** — Run updated modules in the next bootcamp session
4. **Capture field notes** — Add observations to the registry for continuous improvement

---

## Reproducibility Guide

### For a New Facilitator Running the Bootcamp

1. **Read this playbook** — Understand the modular structure and city metaphor system
2. **Check the Module Registry** — See which modules are ✅ Current vs. ⚠️ flagged
3. **Review the Field Guide** — The API Fundamentals Field Guide (api-city-explainer-2.html) is the metaphor reference. Every analogy in the slides traces back to a layer in this guide.
4. **Run the modules in order (1-12)** but know that each one is self-contained. If time is short, you can drop Module 6 (Git), Module 7 (Dev Experience), or Module 11 (Lifecycle) without breaking the narrative.
5. **Use speaker notes religiously** — They contain the pedagogical intent, not just talking points. The "why" behind each slide matters as much as the "what."

### For Someone Updating a Module

1. **Check the Flagged Changes** in the registry — what specifically changed?
2. **Read the module's "Postman Features Referenced"** — which features are affected?
3. **Open the current slides for that module** — what needs to change?
4. **Draft updates** — Cowork can generate draft content; review for tone and accuracy
5. **Update the Field Guide** if the metaphor needs to evolve (rare)
6. **Update the Registry** — new date, clear the flag, add notes

### For Someone Adding a Completely New Module

1. **Define the topic scope** — what specific subject does this module own?
2. **Map to the City Metaphor** — every concept needs a city analogy
3. **Write learning objectives** — 2-3 specific things learners will understand or do
4. **List Postman features referenced** — this is critical for the update system
5. **Assign a change sensitivity** — how often will this module need updates?
6. **Add to the Module Registry** in Airtable
7. **Add to this playbook** with the standard module format

---

## Source Materials Reference

| Document | Location | Purpose |
|----------|----------|---------|
| Postman Fundamentals Bootcamp (V11 slides) | Google Drive / uploaded .pptx | Current production slide deck |
| Bootcamp V12 | Google Drive / uploaded .pptx | Marcus's V12 update plans |
| V11 Bootcamp Flow | [Google Doc](https://docs.google.com/document/d/1D7o7IYvkrQm2FeCgbh7SisnzF4Xlbc6pA1QJInGh-y4/edit) | Detailed facilitator flow for V11 |
| Bootcamp Review | [Google Doc](https://docs.google.com/document/d/1D14mLqe-BIz3dseLtvF9IVgUClZmfCICfFERnfStnog/edit) | Analysis of what needs restructuring |
| New Hire Bootcamp Refresh Guide | [Google Doc](https://docs.google.com/document/d/1Uo1oHwETRLwxCRA40Hc1am5toD1TrI3QmUQSuCZ7Y_8/edit) | Digital Grocery Store hands-on modules |
| API Fundamentals Field Guide | api-city-explainer-2.html | Master metaphor reference (11 layers) |
| Pedagogy Bootcamp Doc | [Google Doc](https://docs.google.com/document/d/1Yr3GmfQK8k5K1KfIDmwFwdLiXN1ZtyiNPQqj7v0IBHU/edit) | Pedagogical framework |
| Postman V12 Wiki | [Confluence](https://postmanlabs.atlassian.net/wiki/spaces/v12/pages/7131791735/Postman+v12) | Internal V12 product documentation |

---

## Airtable Setup Guide

When you're ready to create the module registry in Airtable, here's the structure to build:

### Base: "Bootcamp Module Registry"

**Table 1: Modules**

| Field Name | Field Type | Notes |
|-----------|-----------|-------|
| Module ID | Single line text | M01 through M12 |
| Module Name | Single line text | e.g., "Welcome & Psychological Safety" |
| Change Sensitivity | Single select | Options: 🟢 Low, 🟡 Medium, 🔴 High |
| Status | Single select | Options: ✅ Current, ⚠️ Needs Review, 🔄 Update In Progress, ❌ Outdated |
| Postman Features Referenced | Long text | Comma-separated list of specific features |
| Last Content Update | Date | When slides/notes were last revised |
| Last Audit Date | Date | When someone last checked against current product |
| Flagged Changes | Long text | Specific changelog items that triggered review |
| Owner | Single line text | Who's responsible |
| Field Guide Layers | Single line text | Which layers from the Field Guide this maps to |
| V11 Slides | Single line text | Slide numbers from current deck |
| V12 Slides | Single line text | Slide numbers from V12 draft |
| Notes | Long text | Free-text context |

**Table 2: Changelog Tracking**

| Field Name | Field Type | Notes |
|-----------|-----------|-------|
| Date | Date | Release date |
| Feature/Change | Single line text | What changed |
| Description | Long text | Details |
| Affected Modules | Link to Modules | Which modules this impacts |
| Reviewed | Checkbox | Whether someone has reviewed the impact |
| Action Taken | Long text | What was updated as a result |

**Initial Data — Pre-populate Modules table with:**

| Module ID | Name | Sensitivity | Features Referenced |
|----------|------|-------------|-------------------|
| M01 | Welcome & Psychological Safety | 🟢 Low | None |
| M02 | The Internet & APIs | 🟢 Low | None (conceptual) |
| M03 | How APIs Work | 🟢 Low | None (conceptual) |
| M04 | API Design & Architecture | 🟡 Medium | API Builder, Mock Servers, OpenAPI support |
| M05 | Security & Authentication | 🟡 Medium | Auth tab, API keys, OAuth flows, Vault |
| M06 | Git & Version Control | 🔴 High | Native Git, branching, pull requests, version history |
| M07 | The Developer Experience | 🟡 Medium | Postman CLI, CI/CD, workspaces, environments |
| M08 | AI & Agents | 🔴 High | Agent mode, AI testing, AI debugging, AI docs, MCP |
| M09 | The Postman Platform | 🔴 High | All major product areas |
| M10 | Hands-On Lab (Grocery Store) | 🔴 High | Collections, Workspaces, Forking, Agent Mode, Mocks, API Network |
| M11 | API Lifecycle & Governance | 🟡 Medium | API Catalog, Insights, Governance |
| M12 | Wrap-Up & Bridge to P4P | 🟢 Low | None |

Cowork can create this Airtable structure for you anytime — just say the word.

---

## Next Steps

1. **Airtable Module Registry** — Structure documented above; ready to create when you want
2. **Scheduled Monitoring Task** — Cowork task running weekly to check Postman changelog against module dependencies
3. **Slack Integration (future)** — When connected, add product update channels as an additional signal source
4. **V12 Slide Production** — Use this modular architecture to produce the actual V12 slide deck, one module at a time
