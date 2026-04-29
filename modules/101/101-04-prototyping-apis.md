---
id: 101-04
title: "Prototyping APIs with Mock Servers"
program: 101
owner: Marcus Kidan
change_sensitivity: medium
status: current
last_updated: 2026-04-28
last_audited: 2026-04-28

postman_features:
  - Mock Servers
  - Examples
  - Collections
  - Environments
  - Variables
  - Collection Runner
  - Postbot

update_triggers:
  - "Mock server feature updates"
  - "Dynamic variable changes"
  - "Mock matching algorithm changes"
  - "Example management updates"
  - "Postbot capability updates"
---

## Overview

Teaches API prototyping using mock servers in Postman. Participants learn to design API endpoints from requirements, create realistic examples with dynamic variables and contextual responses, set up mock servers for API simulation, write tests against mock servers, and transition from prototype to production testing. These are v11 materials; the hub monitors for v12 changes.

## Learning Objectives

- Design API endpoints from business requirements using collections and examples
- Create mock servers that simulate realistic API behavior using dynamic variables
- Write and run test suites against mock servers to validate API design before implementation
- Transition test suites from mock to production environments

## Key Elements

### API Design from Requirements

Before you build, you design. API design starts with business requirements and translates them into endpoint definitions. The process follows a predictable pattern:

**Identify the Resources:**
What "things" does the API manage? For a vehicle fleet management system, the resources might be: accounts, vehicles, drivers, trips, maintenance records.

**Define CRUD Operations:**
For each resource, determine which operations are needed:
- **Create** — POST /accounts (register a new fleet account)
- **Read** — GET /accounts/{id} (retrieve account details), GET /accounts (list all accounts)
- **Update** — PUT /accounts/{id} (update account information)
- **Delete** — DELETE /accounts/{id} (deactivate an account)

Not every resource needs all four operations. A read-only API might only have GET endpoints. A logging API might only have POST (write) and GET (read).

**Define Data Formats:**
What fields does each resource contain? What are their types? Which are required vs. optional?
```json
{
  "id": "uuid",
  "company_name": "string (required)",
  "contact_email": "string (required)",
  "fleet_size": "integer (optional)",
  "plan": "string (enum: basic, professional, enterprise)",
  "created_at": "datetime"
}
```

This design work happens in Postman by creating a collection with requests and examples — before any backend code exists.

### Examples with Dynamic Variables

Static examples are useful but limited. When a mock server always returns the same UUID, the same name, and the same timestamp, it feels artificial. Dynamic variables make mock responses realistic.

**Built-in Dynamic Variables:**
Postman provides dynamic variables that generate random data on each request:

- `{{$randomUUID}}` — Generates a unique ID like `6c84fb90-12c4-11e1-840d-7b25c5ee775a`
- `{{$randomFirstName}}` — Generates names like "Maria," "James," "Yuki"
- `{{$randomLastName}}` — Generates surnames
- `{{$randomEmail}}` — Generates realistic email addresses
- `{{$randomInt}}` — Generates a random integer
- `{{$timestamp}}` — Current Unix timestamp
- `{{$isoTimestamp}}` — Current time in ISO 8601 format

**Contextual Response Variables:**
Mock servers can reference parts of the incoming request in responses:

- `{{$body}}` — The entire request body (echo back what was sent)
- `{{$pathSegments}}` — Parts of the URL path (use the ID from the URL in the response)

**Example Using Dynamic Variables:**
A POST /accounts endpoint with a dynamic response:
```json
{
  "id": "{{$randomUUID}}",
  "company_name": "{{$body.company_name}}",
  "contact_email": "{{$body.contact_email}}",
  "fleet_size": "{{$body.fleet_size}}",
  "plan": "basic",
  "created_at": "{{$isoTimestamp}}"
}
```

Every time the mock is called, it returns a unique ID and the current timestamp — behaving much more like a real API.

### Mock Server Creation and Configuration

A mock server in Postman is a simulated API that responds based on the examples you've defined in your collection. It requires no backend infrastructure — Postman hosts it in the cloud.

**Creating a Mock Server:**
1. Select the collection you want to mock
2. Click "Create Mock Server"
3. Name the mock and choose configuration options (public/private, response delay)
4. Postman generates a URL like `https://abc123-mock.pstmn.io`
5. Store the mock URL in an environment variable for easy switching later

**How Matching Works:**
When a request hits the mock server, Postman matches it to an example using:
1. HTTP method + URL path (exact match)
2. If multiple examples exist for the same endpoint, it uses the default example
3. You can override matching with headers:
   - `x-mock-response-name` — Return the example with this specific name
   - `x-mock-response-code` — Return the example with this specific status code

**Example: Multiple Responses for One Endpoint**

For GET /accounts/{id}, you might have three examples:
- "Success - Active Account" (200)
- "Success - Suspended Account" (200)
- "Not Found" (404)

Without headers, the mock returns the default. With `x-mock-response-name: Not Found`, it returns the 404 example. This lets you test error handling without needing a real API that's broken.

### Mock Server Use Cases

Mock servers aren't just for prototyping. They solve several real-world problems:

**Prototyping:**
Design an API, create examples, spin up a mock, and share it with stakeholders for feedback — all before writing a line of backend code. This is the primary use case in this module.

**Sandbox Testing:**
Give QA teams a mock that always returns predictable responses. No flaky test databases, no shared staging environments that other teams break.

**Frontend/Backend Handoffs:**
The frontend team needs an API to build against, but the backend team hasn't finished. Create a mock from the agreed-upon spec. Frontend integrates against the mock. When the real API is ready, swap the URL. If the spec was accurate, everything works.

**Third-Party Dependency Mocking:**
Your API depends on a payment processor. During development, you don't want to hit the real payment API (it costs money, it's slow, it might reject test data). Mock it. Your tests run fast, free, and reliably.

### Testing Against Mock Servers

A mock server isn't just for visual demos — you can build a full test suite against it. This validates your API design before implementation begins.

**Why Test a Mock?**

It sounds circular: "Why test something I defined?" Because the tests validate your design decisions:
- Does the response structure make sense for consumers?
- Are all required fields present?
- Do error responses contain enough information for debugging?
- Does the endpoint naming follow a consistent pattern?

If writing a test feels awkward ("I'm asserting that field X exists, but I'm the one who put it there"), that's a signal. The test is a contract. When the real API replaces the mock, these same tests verify that the implementation matches the design.

**Writing Tests Against Mocks:**
The test scripts are identical to production tests. That's the point — you write them once and reuse them.
```javascript
pm.test("Account has required fields", function () {
    const account = pm.response.json();
    pm.expect(account).to.have.property("id");
    pm.expect(account).to.have.property("company_name");
    pm.expect(account).to.have.property("contact_email");
    pm.expect(account).to.have.property("plan");
    pm.expect(account).to.have.property("created_at");
});
```

### Transitioning from Mock to Production

The most powerful aspect of mock-based development is the transition. Because your collection uses environment variables for the base URL:

1. **Mock environment:** `base_url` = `https://abc123-mock.pstmn.io`
2. **Dev environment:** `base_url` = `https://dev-api.postvehicle.io`
3. **Production environment:** `base_url` = `https://api.postvehicle.io`

When the real API is ready, you switch environments and run the same collection with the same tests. If everything passes, the implementation matches the design. If tests fail, you have a precise list of discrepancies between the mock (the contract) and the implementation.

This workflow means:
- Tests are written once, used across all stages
- Design-to-implementation discrepancies are caught immediately
- The mock serves as the executable specification

### Postbot for Documentation Generation

Once you've built a collection with examples, Postbot can generate documentation from the structure:
- Endpoint descriptions based on the URL pattern and examples
- Parameter descriptions inferred from the request body schema
- Response field descriptions based on example data

This is useful when handing off the prototype to a development team — they receive not just the mock, but a documented collection explaining what each endpoint does and why.

## Activities

### PostVehicle Scenario

PostVehicle Enterprises is launching a new Account API for fleet management. The product team has defined requirements, and your job is to prototype it before the backend team starts development.

**Phase 1: Design the Account API from Requirements**

The product team provides these requirements:
- Fleet managers need to create, view, update, and delete accounts
- Each account has: company name, contact email, fleet size, plan level (basic/professional/enterprise), and creation date
- The API should return a unique ID for each account
- List endpoint should support pagination (page, per_page parameters)

Build the collection:
1. Create a new collection called "PostVehicle Account API"
2. Add a folder called "Accounts"
3. Create requests: POST /accounts, GET /accounts, GET /accounts/{id}, PUT /accounts/{id}, DELETE /accounts/{id}
4. Add request bodies with realistic data for POST and PUT
5. Add query parameters for GET /accounts (page, per_page)

**Phase 2: Create Examples with Dynamic Variables**

Make the mock responses realistic:
1. For POST /accounts: create a "Success - Created" example (201) using `{{$randomUUID}}` for the ID and `{{$isoTimestamp}}` for created_at, with `{{$body}}` references for echoing submitted fields
2. For GET /accounts/{id}: create three examples:
   - "Success - Active Account" (200) with realistic dynamic data
   - "Success - Enterprise Account" (200) with fleet_size of 500+ and enterprise plan
   - "Not Found" (404) with an error message
3. For GET /accounts: create a "Success - Page 1" example (200) with an array of accounts and pagination metadata
4. For DELETE /accounts/{id}: create "Success - Deleted" (204) and "Not Found" (404) examples
5. Name every example descriptively — these names are used for mock matching

**Phase 3: Create and Configure the Mock Server**

Bring the prototype to life:
1. Create a mock server from the Account API collection
2. Copy the mock server URL
3. Create a new environment called "PostVehicle - Mock"
4. Add `base_url` with the mock server URL as the value
5. Update all requests to use `{{base_url}}` in their URLs
6. Send test requests to each endpoint and verify the mock returns expected examples
7. Use `x-mock-response-name` header to request specific examples (e.g., the "Not Found" response)

**Phase 4: Write a Test Suite Against the Mock**

Validate the design with tests:
1. Add test scripts to each endpoint:
   - POST /accounts: verify 201 status, response contains id, company_name matches request body
   - GET /accounts/{id}: verify 200 status, response has all required fields
   - GET /accounts: verify 200 status, response is an array, pagination metadata is present
   - PUT /accounts/{id}: verify 200 status, updated fields reflect the request body
   - DELETE /accounts/{id}: verify 204 status
2. Add folder-level tests for common assertions: response is JSON, response time under 2 seconds
3. Use Postbot to generate additional edge case tests

**Phase 5: Transition to Development Server**

The backend team has a partial implementation ready. Switch targets:
1. Create a new environment called "PostVehicle - Dev" with `base_url` pointing to the development server URL
2. Switch from "PostVehicle - Mock" to "PostVehicle - Dev"
3. Run the full collection with the Collection Runner
4. Compare results: which tests pass against the real server? Which fail?
5. Document discrepancies — these are gaps between the design (mock) and the implementation (dev server)
6. Share the report with the backend team as a punch list of remaining work

### Expected Outcome

By the end of this activity, each participant has:
- A collection designed from business requirements with realistic examples
- Dynamic variables in examples for realistic mock responses
- A working mock server simulating the Account API
- A test suite validated against the mock
- Experience transitioning the same test suite from mock to a development environment
- A discrepancy report comparing mock and real API behavior

## Postman Features in This Module

### Mock Servers
The centerpiece of this module. Participants create, configure, and use mock servers to simulate the Account API. Mock servers are positioned as the tool that lets you validate API design before spending development resources — catching design mistakes when they're cheap to fix.

### Examples
Examples drive mock server behavior. Participants create multiple examples per endpoint with dynamic variables, learning that the quality of your examples determines the quality of your mock. Realistic examples lead to realistic testing; lazy examples lead to false confidence.

### Collections
Collections serve as the design artifact. The collection structure (folders, requests, examples) is the API specification in executable form. Participants learn that designing a collection IS designing the API.

### Environments
Environments enable the mock-to-production transition. Participants create separate environments for mock and dev, switching between them with a dropdown. This demonstrates that the same tests work across contexts — the collection is environment-agnostic.

### Variables
Variables appear in two contexts: environment variables for base URLs (enabling environment switching) and dynamic variables in examples (enabling realistic mock responses). Participants see both uses and understand that variables are the mechanism for making collections flexible and reusable.

### Collection Runner
The Collection Runner is used in Phase 5 to execute the full test suite against the development server. This is where the "transition" happens — participants see tests that passed against the mock fail against the real API, identifying implementation gaps.

### Postbot
Postbot assists with test generation and documentation. Participants use it to generate edge case tests they might not have thought of and to create endpoint documentation from the collection structure. Postbot is positioned as an accelerator for the tedious parts of prototyping.

## Facilitator Notes

**Timing:** 90 minutes total (20 for teaching prototyping concepts, 55 for hands-on activities, 15 for review and transition discussion).

**Setup Requirements:**
- Ensure participants have completed Module 101-01 (they need the environment setup knowledge)
- Prepare a partially-implemented development server for Phase 5 (intentionally leave 2-3 endpoints incomplete so participants see test failures that represent real implementation gaps)
- If a development server isn't available, use a second mock with slightly different responses to simulate the "implementation differs from design" scenario
- Test mock server creation beforehand — the flow involves several steps and may have UI changes between Postman versions

**Tips:**
- The "why test a mock?" question always comes up. The best answer: "You're not testing the mock. You're testing the contract. These tests will run against the real API when it exists. You're writing them now while the design is fresh, not later when you've forgotten the requirements."
- Dynamic variables are a crowd-pleaser. When participants see `{{$randomFirstName}}` generate a different name on every request, it clicks: "This actually feels like a real API." Use this moment to discuss what makes a mock convincing enough for frontend integration.
- The mock-to-production transition in Phase 5 is the most important moment in the module. When a test that passed against the mock fails against the dev server, ask: "Is the test wrong, or is the implementation wrong?" Sometimes it's the test (overly specific assertion). Sometimes it's the implementation (missing field). Learning to diagnose which is a key testing skill.
- If time is tight, Phase 5 can be instructor-led rather than hands-on. Walk through the transition on the projector, showing the Collection Runner results and how to interpret failures.

**Common Questions:**
- "Can I make the mock return errors randomly?" — Not natively, but you can use `x-mock-response-name` headers in pre-request scripts to programmatically select different responses. This simulates intermittent failures.
- "Is the mock server URL permanent?" — Mock servers persist as long as the collection exists. The URL stays stable. You can delete and recreate if needed.
- "Can multiple people hit the same mock?" — Yes, mock servers are cloud-hosted and can handle concurrent requests. This is how frontend and QA teams can integrate in parallel.
- "What if my mock doesn't match any example?" — The mock returns a generic response or a 404 with a message explaining no matching example was found. Check your URL path, HTTP method, and example names.
- "How is this different from a staging server?" — A mock is defined by examples you control. A staging server runs real code with a real database. Mocks are deterministic and instant to create; staging servers are realistic but fragile and shared.

## Pain Points Addressed

**Frontend Teams Blocked Waiting for Backend API Implementation**
The classic dependency chain: product defines requirements, backend builds the API, frontend integrates. If backend is two sprints behind, frontend sits idle. Mock servers break this chain. The team agrees on the API design (the collection with examples), creates a mock, and frontend integrates against it immediately. Backend builds to the same spec. When they meet in the middle, the API works because both sides built to the same contract.

**No Way to Evaluate API Design Before Committing to Development**
A spec document is abstract. Reading "POST /accounts returns a 201 with the created account object" tells you what it does, but not whether it feels right. A mock server lets stakeholders, frontend developers, and QA actually call the API, inspect responses, and raise concerns before development starts. Catching a bad endpoint design in the prototype stage costs a conversation. Catching it after implementation costs a sprint.

**Test Environments Are Fragile and Hard to Maintain**
Shared staging servers are a persistent pain point. Team A deploys a broken build. Team B's tests fail. Nobody knows why. Mock servers are isolated and deterministic — your mock doesn't break because someone else deployed bad code. For dependency testing (your API calls a payment processor), mocking the dependency means your tests run fast, free, and without external failures contaminating your results.
