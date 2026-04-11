---
id: M10
title: "Hands-On Lab — The Grocery Store"
program: bootcamp
owner: Marcus Kidan
change_sensitivity: high
status: current
last_updated: 2026-04-10
last_audited: 2026-04-10

postman_features:
  - Collections
  - Workspaces
  - Forking
  - Authentication
  - Agent Mode
  - Mock Servers
  - Environments
  - Variables
  - API Network
  - Partner Workspaces

update_triggers:
  - "Postman UI changes (button locations, naming, flows)"
  - "Workspace type changes"
  - "Agent mode capability changes"
  - "Collections or forking workflow changes"
  - "Mock server UI changes"
  - "API Network changes"
---

## Overview

This module is a narrative-driven, hands-on sequence where participants help a fictional grocery store modernize through APIs. The **Digital Grocery Store** is a multi-phase project that mirrors a real API development lifecycle:

1. **Lab 10a: The Consumer** — Find and use an existing API
2. **Lab 10b: The Teammate** — Collaborate in a workspace
3. **Lab 10c: The Designer** — Design an API with Agent Mode
4. **Lab 10d: The Prototyper** — Build a mock server and test
5. **Lab 10e: The Publisher** — Share and hand off to the dev team

Each sub-module can run independently or as a sequence. The narrative creates context and meaning for technical actions—participants aren't just "learning Collections," they're "building a store's customer loyalty system."

## Learning Objectives

By the end of this module, participants will be able to:

1. **Navigate the Postman interface** confidently (create requests, manage collections, browse workspaces)
2. **Complete an end-to-end API workflow** from consuming an existing API to publishing a new one
3. **Apply concepts from previous modules** in a hands-on, practical context
4. **Understand how different Postman features** fit together in a realistic project

## Key Elements

### The Scenario: Digital Grocery Store

Your fictional client is **Green Valley Market**, a local grocery store chain looking to modernize. The store has:
- A customer loyalty program (cards, points, discounts)
- Inventory management (stock tracking, reorder)
- Online ordering (delivery, pickup)
- Staff management (shifts, payroll)

All of this is currently managed in spreadsheets and paper systems. Your job is to bring it into the 21st century with APIs.

---

## Lab 10a: The Consumer — "The Store Needs a Digital Customer List"

**Scenario:** Green Valley's owner says, "I need to know who my customers are—get me a list." You decide to use an existing customer API instead of building from scratch.

**Duration:** 30–45 minutes

### Steps

1. **Create a Workspace**
   - Sign into Postman
   - Create a new workspace called "Green Valley Market"
   - Add a description: "APIs for Green Valley Market modernization"

2. **Find an Existing API**
   - Browse the API Network or use a public API (e.g., JSONPlaceholder Users API, a public ecommerce API)
   - Fork the collection into your workspace
   - Review the requests (GET, POST, etc.)

3. **Make Your First Request**
   - Open a GET request (e.g., `GET /users`)
   - Click Send
   - Inspect the response, understand the structure

4. **Authenticate (if needed)**
   - Add API Key or Bearer token to the request
   - Update the Authorization type in Postman
   - Re-send the request

5. **Parse the Response**
   - Look at the JSON response
   - Identify customer fields (name, email, address, phone)
   - Note any fields you'll need to map to Green Valley's system

### Learning Outcomes

- Understand how requests and responses work
- Navigate the Postman UI (tabs, buttons, panels)
- Authenticate with an API
- Read and interpret API responses

### Pain Point Addressed

**Discovery is hard.** In the past, you'd ask a colleague, search internal docs, or ask Slack. With Postman, you can browse the API Network, fork a collection, and start consuming it in minutes.

---

## Lab 10b: The Teammate — "Customers Need to Buy Things — Bring in a Friend"

**Scenario:** The loyalty program is live, but your boss says, "We need help building the shopping cart feature. Invite a team member to the project."

**Duration:** 20–30 minutes

### Steps

1. **Create a New Collection**
   - In your workspace, create a collection called "Shopping Cart API"
   - Add a description of what the collection does

2. **Add Requests to the Collection**
   - Create a POST request: `POST /cart/add-item` (add product to cart)
   - Create a GET request: `GET /cart/{cart_id}` (view cart)
   - Create a DELETE request: `DELETE /cart/{item_id}` (remove item)
   - Add request bodies and parameters as appropriate

3. **Invite a Collaborator**
   - Share the workspace with a teammate
   - Assign them a role (Editor or Viewer)
   - They accept the invite and join

4. **Fork the Collection (Alternative)**
   - Show how a colleague can fork your collection to create their own version
   - Explain the benefit: they can experiment without affecting the original

5. **Real-time Collaboration**
   - Both team members open the same collection
   - Edit a request name together
   - See changes sync in real-time

### Learning Outcomes

- Create and organize collections
- Invite team members and manage access
- Use forking to enable parallel work
- Understand role-based permissions (Admin, Editor, Viewer)

### Pain Point Addressed

**Collaboration is fragmented.** Email attachments, shared drives, and Slack threads don't scale. Postman workspaces keep everyone on the same page, with audit trails and versioning.

---

## Lab 10c: The Designer — "The Owner Approved a Loyalty Program — Let's Design the API"

**Scenario:** The owner says, "I want a points-based loyalty program. Customers earn points on purchases, redeem them for discounts, and see their balance." You have an idea in your head but need to formalize it.

**Duration:** 30–40 minutes

### Steps

1. **Open Agent Mode**
   - In Postman, navigate to Agent Mode (or a similar AI feature if naming changes)
   - Describe the loyalty program in natural language:
     - "Create an API for a points-based loyalty program. Customers can earn points on purchases, check their balance, and redeem points for discounts. Include endpoints for: POST /loyalty/purchase (record purchase and add points), GET /loyalty/balance/{customer_id} (view points), POST /loyalty/redeem (redeem points for a discount)."

2. **Review the Generated Collection**
   - Agent Mode generates request endpoints, parameters, and response structures
   - Review the collection for accuracy
   - Make edits as needed (rename endpoints, adjust parameters)

3. **Add Mock Responses**
   - For each endpoint, Agent Mode auto-generates response examples
   - Review and customize them to match your business logic

4. **Document the API**
   - Review the auto-generated documentation
   - Add business context (why this endpoint, when to use it, common errors)

### Learning Outcomes

- Use AI to speed up API design
- Understand best practices for endpoint naming and structure
- Create request/response examples
- Document APIs for other developers

### Pain Point Addressed

**Design takes forever.** API design is iterative and often blocked by paralysis (what endpoints do we need?). Agent Mode lets you go from conversation to a working design in minutes.

---

## Lab 10d: The Prototyper — "The Design Looks Great — Make It Feel Real Before We Spend Money on Developers"

**Scenario:** The owner loves the loyalty program design, but wants to see it in action before greenlit a dev team. You decide to mock the API so the frontend team can integrate it.

**Duration:** 30–40 minutes

### Steps

1. **Create a Mock Server**
   - In Postman, click "Create Mock Server"
   - Select the "Loyalty Program" collection
   - Choose to run it in the cloud (or locally with Postman CLI)
   - Copy the mock URL (e.g., `https://mock.postman.io/loyalty-api`)

2. **Configure Mock Responses**
   - For each request, set up response examples:
     - `POST /loyalty/purchase` → returns `{ success: true, points_added: 50, new_balance: 250 }`
     - `GET /loyalty/balance/{customer_id}` → returns `{ customer_id: "123", balance: 250 }`
     - `POST /loyalty/redeem` → returns `{ success: true, discount: 10, remaining_balance: 200 }`

3. **Set Up Environments**
   - Create an environment called "Mock"
   - Add a variable `base_url` = `https://mock.postman.io/loyalty-api`
   - Create another environment "Production" with `base_url` = `https://api.greenvalley.local/loyalty-api`

4. **Update Requests to Use Variables**
   - In each request, replace hardcoded URLs with `{{base_url}}/loyalty/purchase`
   - Switch between Mock and Production environments by selecting from the dropdown
   - Show how requests automatically update

5. **Hand to Frontend Team**
   - Give the frontend team the mock URL
   - They integrate against the mock while you build the real API
   - Both move in parallel instead of serially

### Learning Outcomes

- Create and configure mock servers
- Use environments and variables for flexibility
- Decouple frontend and backend development
- Understand the power of contract-based development

### Pain Point Addressed

**Development is blocked by sequential dependencies.** Frontend waits for backend. Backend waits for requirements. Mock servers break this chain—everyone can work in parallel.

---

## Lab 10e: The Publisher — "The Owner Approved — Hand It Off to the Dev Team"

**Scenario:** The mock server worked, the owner approved, and now you need to hand the API spec off to the dev team. You also want to publish it to your internal API marketplace so other teams know it exists.

**Duration:** 20–30 minutes

### Steps

1. **Review the Collection Documentation**
   - Open your Loyalty Program collection
   - Check that all endpoints are documented (description, parameters, examples)
   - Update any missing info

2. **Publish to Private API Network**
   - In Postman, click "Publish to API Network"
   - Choose "Private" (internal only)
   - Add metadata: name, description, category (Ecommerce), icon
   - Set permissions: who can view, fork, use

3. **Create a Workspace Share Link**
   - In the workspace, create a shareable link to the collection
   - Send it to the dev team so they can fork it and start building

4. **Export the Collection (Alternative)**
   - If your organization doesn't use the API Network, export as JSON
   - Share via GitHub, Confluence, or your internal API documentation tool

5. **Version the Collection**
   - Tag the current version: "1.0-approved"
   - Note: "Dev team will implement this spec. Freeze endpoint names and response structure."
   - If requirements change, create a v1.1 branch

### Learning Outcomes

- Publish APIs to a marketplace
- Share collections with external teams
- Version API definitions
- Understand the handoff from design to implementation

### Pain Point Addressed

**Knowledge is scattered.** APIs are built, but nobody knows they exist. The API Network creates a single source of truth—teams can discover, fork, and integrate instead of reinventing.

---

## Postman Features in This Module

- **Collections**: Organize requests, build libraries of API calls
- **Workspaces**: Collaborate with teammates, manage access
- **Forking**: Create parallel versions without affecting the original
- **Authentication**: Secure requests with API Key, Bearer Token, OAuth, etc.
- **Agent Mode**: Generate collections, tests, and docs from natural language
- **Mock Servers**: Prototype APIs without backend infrastructure
- **Environments & Variables**: Manage different settings (dev, staging, prod) without editing requests
- **API Network**: Publish and discover APIs across your organization
- **Partner Workspaces**: Share collections with external teams

---

## Activities & Checkpoints

### Checkpoint 1 (after 10a)
Ask: "Show me the response from the API request you just made. What are the three most important fields?"

### Checkpoint 2 (after 10b)
Ask: "Invite a teammate to your workspace. What permission level did you assign them, and why?"

### Checkpoint 3 (after 10c)
Ask: "Describe the loyalty program API in plain English. What endpoints does it have, and what does each do?"

### Checkpoint 4 (after 10d)
Ask: "Switch your request from Mock to Production environment. What changed in the URL? Why is this useful?"

### Checkpoint 5 (after 10e)
Ask: "Explain how you'd hand off this API spec to a developer. What's included, and what's their next step?"

---

## Facilitator Notes

**Pacing:** This is a long module if run as a full sequence. Consider:
- Running all 5 labs in sequence (90–120 minutes total) for a full immersion
- Running 10a, 10b, and 10d separately as "mini-labs" (30–40 min each) interspersed with other modules
- Letting participants pick 2–3 labs based on their role (developers → 10a, 10c, 10d; QA → 10a, 10d; product → 10c, 10e)

**Setup:**
- Ensure all participants have a Postman account (Team or higher)
- Pre-create the "Green Valley Market" workspace and share with all participants, OR have them create their own
- If using the JSONPlaceholder API, it's free and doesn't require auth—reduces setup friction
- Test the mock server creation flow beforehand to identify any UI changes

**Troubleshooting:**
- If a participant's mock server doesn't start, restart the mock server or switch to cloud-hosted
- If environment variables aren't substituting in requests, check that the syntax is `{{variable_name}}` (double braces)
- If forking fails, check that the user has workspace create permissions

**Common Questions:**
- "Can I do this with Postman CLI?" → Yes, all of these can be automated; show an example in Lab 10e
- "How do we version when we publish?" → API Network supports version tags; walk through the process
- "What if the real API differs from the mock?" → Explain that you'd update the mock, re-test, then update the real API; this is why mocking is powerful

**Extension Activities:**
- Integrate the mock server with a frontend app (have a simple HTML/JS form that calls the mock)
- Set up automated tests to run against the mock (show how Postman test assertions work)
- Generate an SDK from the collection (show SDK Distribution feature if available)
- Set up monitoring on the mock server (show Postman's monitoring feature)

---

## Pain Points Addressed

**UI Navigation is Confusing**
- Solution: Guided walkthroughs, clear step-by-step instructions, labeling of buttons and panels
- Postman Feature: Postman UI design, help tooltips

**Development is Slow and Fragmented**
- Solution: Mock servers enable parallel work; collections standardize format; workspaces centralize collaboration
- Postman Feature: Collections, Mock Servers, Workspaces

**Design and Implementation are Misaligned**
- Solution: Agent Mode speeds design; mocks enforce the spec; versioning tracks changes
- Postman Feature: Agent Mode, Mock Servers, Collections

**Onboarding New Team Members Takes Forever**
- Solution: Fork a collection, share a workspace, they're productive immediately
- Postman Feature: Workspaces, Forking, Collections

**APIs are Built but Nobody Knows About Them**
- Solution: Publish to API Network, use private marketplace, create shared documentation
- Postman Feature: API Network, Workspace sharing, API Catalog
