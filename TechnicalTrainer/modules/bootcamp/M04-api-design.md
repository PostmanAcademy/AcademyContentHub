---
id: M04
title: "API Design & Architecture"
program: bootcamp
owner: Marcus Kidan
change_sensitivity: medium
status: current
last_updated: 2026-04-10
last_audited: 2026-04-10

postman_features:
  - "API Builder/Editor"
  - "Mock Servers"
  - "OpenAPI spec support"

update_triggers:
  - "New spec format support"
  - "Design tooling UI changes"
  - "Mock server feature updates"
  - "API Builder/Editor changes"
---

## Overview
This module shifts from "how APIs work" to "how they're designed." We explore REST as a design philosophy (not law), the trade-offs between API-first and code-first development, the difference between specs and documentation, and how system architecture affects API design. By the end, participants understand that API design is a series of deliberate choices, and Postman tools help you make and test those choices before committing to code.

## Learning Objectives
- Distinguish between API-first and code-first development approaches
- Explain what an API spec is versus documentation
- Understand monolith versus microservices architecture trade-offs

## Key Elements

### REST as Design Choice, Not Hard Science
REST (Representational State Transfer) is a set of principles for designing web APIs, not a law of nature. It says things like:
- Use standard HTTP methods for standard operations (GET for read, POST for create)
- Resources should have identifiable URLs (`/users/123`)
- Responses should be stateless (the server doesn't remember you between requests)

But REST is a guideline. You can break it if you have a good reason. Many successful APIs are not strictly RESTful. The point is: **design decisions should be intentional**, not accidental.

### The Fork-in-Drawer Analogy
Imagine you're designing the layout of a kitchen for a million homes. You have to decide: where do forks go? You could say "forks always go in the top-left drawer" (REST principle). But you could also say "forks go where they fit" (non-REST).

The benefit of the first approach: anyone living in any of those homes knows where to find a fork. Consistency matters. But if you're designing a single kitchen for a specific person, the overhead of strict consistency might not be worth it.

APIs are the same. Consistency is a design choice. Standards make things predictable, but they have a cost (less flexibility).

### API-First vs. Code-First Development

**API-First:** Design the API contract first (spec), then build the implementation.
- You ask: "What would developers want to call this? What parameters? What responses?"
- You design the interface like you're designing a public building—it needs to make sense to strangers.
- Pros: Clear contract, easier collaboration, changes are deliberate.
- Cons: Upfront design work, may not match implementation reality.

**Code-First:** Build the code first, then expose it as an API.
- You ask: "How do I solve this problem?" then wrap it in an API layer.
- Pros: Fast to build, directly connected to business logic.
- Cons: API design is an afterthought, harder to change later, may be clunky for external users.

The trade-off is **design upfront vs. speed to market**.

### Specs vs. Docs: Blueprint vs. Brochure

**Spec (OpenAPI, Swagger):**
- A machine-readable definition of your API (JSON or YAML)
- Defines every endpoint, every parameter, every response type
- The architectural blueprint filed with the city
- Tools can read it and generate code, mocks, tests, and documentation
- The source of truth

**Documentation:**
- Human-readable prose explaining how to use the API
- Often auto-generated from the spec, but can be written separately
- The brochure in the lobby
- Useful for onboarding and context, but not for tooling
- Usually lives in a browser or Markdown

A spec enables automation. If you have a spec, you can generate a mock server in seconds. If you only have docs, you have to build the mock yourself.

### Monolith vs. Microservices: Department Store vs. Specialist District

**Monolith:**
- One big codebase handling everything (store locator, inventory, billing, shipping, etc.)
- Fast to build initially; all logic is in one place
- Problem: If the billing system slows down, the whole store slows down. Hard to scale selectively. Hard to change one piece without risking the whole thing.
- Analogy: A department store where everything is in one building. Fast checkout, simple rules. But if the shoe department is popular, the whole building gets crowded.

**Microservices:**
- Many small, independent APIs (one for store locator, one for inventory, one for billing, one for shipping)
- Each team owns their building. If the billing API slows down, inventory still runs fast.
- Problem: More complexity to orchestrate. More places where things can fail. More infrastructure overhead.
- Analogy: A specialist district where each store handles one thing (shoes, groceries, hardware). If the hardware store is slammed, the grocery store is unaffected. But you need good signs to navigate the district.

The decision depends on scale, team size, and change velocity. A startup usually starts as a monolith. As it grows, parts splinter off into microservices.

### API Versioning: Building Renovations
When you want to change an API, you have a problem: external developers are already using it. If you change `/users` to return a different structure, you break their code.

Solution: versioning. You keep `/v1/users` running, but build `/v2/users` with the new design. Old clients keep using v1 (it stays open), new clients use v2 (it has better features).

The catch: you're now running two APIs. That's a cost. So versioning is a last resort—ideally, you design the API well enough that you don't need it.

Alternative: use query parameters or headers to signal version (`/users?version=2`), but this is less clean than URL versioning.

## Activities

### "Two Restaurants" – API-First vs. Code-First
Divide the class into two groups.

**Restaurant A (Menu-First):**
- You design the menu first. ("Our appetizers are in the $10–15 range, mains are $20–30, desserts are $8.")
- You decide what you want to cook based on what customers want to eat.
- You build the kitchen to match the menu.

**Restaurant B (Sell Tomorrow):**
- You open tomorrow with whatever you can make today.
- Your menu is whatever the kitchen produces.
- Customers find out what's available when they arrive.

Ask each group to fill in the pros and cons:

**Group A (Menu-First):**
- Pros: Clear expectations, easier to plan inventory, customers know what to expect
- Cons: Upfront design work, if you get the menu wrong, you've wasted effort

**Group B (Sell Tomorrow):**
- Pros: Fast to market, you're not constrained by early design decisions
- Cons: Chaotic customer experience, inefficient kitchen, hard to optimize once open

Then reveal the connection: API-First is Menu-First. API-Code-First is Sell Tomorrow.

Most successful APIs use some version of Menu-First because consistency matters. But many startups do Code-First and regret it.

## Postman Features in This Module

### API Builder/Editor
Postman's API Builder lets you design your API without writing code. You specify endpoints, methods, parameters, and response schemas. This is **spec-first development** in practice. Once you've designed it, you can mock it immediately.

### Mock Servers
If you've designed an API spec, Postman can instantly spin up a mock server that responds to requests according to your spec. This lets clients (frontend developers, partners) start integrating before the real API is built. This bridges the gap between API-First design and the team's readiness to build.

### OpenAPI Spec Support
Postman can import, edit, and export OpenAPI specs. This means your spec lives in Postman, and Postman becomes the source of truth. Generating docs, mocks, and tests all flows from that spec.

## Facilitator Notes
**Timing:** 30–35 minutes (15 for teaching, 10 for the Two Restaurants activity, 5 for discussion and synthesis).

**Tips:**
- The Two Restaurants activity is engaging but can run long. Set a strict timer for group brainstorming (5 minutes) and discussion (5 minutes).
- The fork-in-drawer analogy feels silly, but it sticks. Use it liberally.
- If the class is technical, they may object: "We do API-first at our company, and it's better." Good—that's true *for them*. The point is that the choice is deliberate, not accidental. If someone says "We do code-first and it works fine," they're probably a startup that hasn't hit scale yet.
- Versioning can feel academic until you point out: "Every time Google Maps adds a new field to their API, they have to worry about breaking old clients. That's why they version."

**Common Questions:**
- "Is REST dead?" – No, but newer patterns (GraphQL, gRPC) are gaining traction. REST is still the default for web APIs.
- "Which should we choose, monolith or microservices?" – Start with a monolith, split off microservices when you feel the pain. Premature microservices are usually a mistake.
- "Can I use Postman to design the API before writing code?" – Yes. That's the whole point of the API Builder and Mock Servers.

## Pain Points Addressed

**Design Decisions Made Late:**  
"Design decisions must happen before committing to development." Many teams jump straight to coding without asking "what is our API supposed to look like?" This is expensive to fix later. Postman's API Builder forces you to design first.

**Documentation Out of Sync:**  
"Classic hard-coded docs vs. living documentation." If docs are written separately from the API, they drift. If the spec is the source of truth, docs can be auto-generated and stay in sync. This is a real problem on teams with even modest-sized APIs.
