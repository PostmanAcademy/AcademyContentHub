---
id: 201-01
title: "Advanced API Prototyping"
program: 201
owner: Marcus Kidan
change_sensitivity: medium
status: current
last_updated: 2026-04-28
last_audited: 2026-04-28

postman_features:
  - Mock Servers
  - Examples
  - Collections
  - Variables
  - Environments
  - Workspaces
  - Postbot
  - Collection Runner

update_triggers:
  - "Mock server feature updates"
  - "Dynamic variable changes"
  - "Mock matching algorithm changes"
  - "Postbot capability updates"
  - "Workspace collaboration features"
---

## Overview

Advanced mock server techniques including collaborative prototyping, dynamic variables with contextual mock responses ($body, $pathSegments, $headers, $queryParams template helpers), mock response matching strategies (x-mock-response-name/code/id headers, body/header matching), mock server configuration (delays, private servers), and team collaboration on prototypes using workspaces and comments. Builds on 101-04 fundamentals. These are v11 materials; the hub monitors for v12 changes.

## Learning Objectives

- Create sophisticated mock responses using contextual template helpers ($body, $pathSegments)
- Configure mock response matching to return specific examples based on headers
- Collaborate on API prototypes using workspaces, comments, and team visibility
- Set up mock server configuration options (delays, privacy, body/header matching)

## Key Elements

### Collaborative Prototyping Workflow

Prototyping is not a solo activity. The 201-level workflow follows a deliberate sequence designed for team-based API design:

1. **Create a shared workspace** — Set up a team workspace so all collaborators see the same resources in real time.
2. **Build the collection** — Define the endpoints, methods, and request structures that represent the API contract.
3. **Add examples** — Create multiple response examples per request to cover success, error, and edge-case scenarios.
4. **Create the mock server** — Stand up a cloud-hosted mock from the collection so consumers can start integrating immediately.
5. **Test the mock** — Validate that the mock returns the correct examples for each request scenario.
6. **Share and publish** — Broadcast workspace updates so stakeholders know the prototype is ready for review.

This workflow ensures that by the time a mock server is live, multiple team members have reviewed the contract, added realistic examples, and validated behavior. It replaces the old pattern of one developer building a mock in isolation and emailing the URL.

### Contextual Mock Responses

Standard mock responses return static JSON. Contextual mock responses use template helpers to echo back parts of the incoming request, making the mock feel like a real server.

**$body** — References fields from the request body. If the client sends `{ "name": "Alice" }`, the mock response can include `{{$body 'name'}}` to return "Alice" in the response. This is critical for create/update endpoints where the response should reflect what was submitted.

**$pathSegments** — References URL path segments by index. For a request to `/accounts/ABC-123/vehicles`, `{{$pathSegments '1'}}` returns "ABC-123". This lets a single mock example handle multiple resource IDs without creating separate examples for each.

**$headers** — References request headers. Useful for returning correlation IDs, content types, or authentication-dependent responses. `{{$headers 'X-Correlation-ID'}}` echoes back whatever the client sent.

**$queryParams** — References query string parameters. For a request to `/vehicles?status=active`, `{{$queryParams 'status'}}` returns "active". This enables mock responses that adapt to filter criteria without multiple static examples.

These helpers transform mock servers from static stubs into contextual prototypes that respond intelligently to varied inputs.

### Mock Response Matching Strategies

When a mock server receives a request, it needs to decide which example to return. Postman provides several matching strategies:

**x-mock-response-name** — Send this header with the exact name of an example, and the mock returns that example. Useful when you have multiple examples for the same endpoint (e.g., "success," "not-found," "validation-error") and want to test each one explicitly.

**x-mock-response-code** — Send this header with an HTTP status code (e.g., 404), and the mock returns the example that matches that status code. Useful for testing error handling paths.

**x-mock-response-id** — Send this header with the unique ID of a specific example. The most precise matching method, useful for automation and scripting.

**Body matching** — When enabled, the mock server compares the request body against example request bodies and returns the closest match. This is powerful for POST/PUT endpoints where different payloads should produce different responses.

**Header matching** — When enabled, the mock server factors in request headers when choosing which example to return. Combined with body matching, this creates highly specific mock behavior.

The matching priority follows a specific order: explicit header overrides (name > code > id) take precedence, then body/header matching, then the default algorithm (URL path + method + status code).

### Dynamic Variables (Faker Library)

Dynamic variables generate random but realistic data each time a request is sent. They use the faker library under the hood:

- **$randomUUID** — Generates a UUID (e.g., "6929bb52-3ab2-448a-8f77-42a3be5edf2a"). Use for IDs in mock responses.
- **$randomFirstName** — Generates a first name (e.g., "Petra"). Use for user-facing test data.
- **$randomEmail** — Generates an email address. Use for account creation mock responses.
- **$isoTimestamp** — Generates the current ISO 8601 timestamp. Use for created_at/updated_at fields.

Dynamic variables are different from contextual template helpers. Dynamic variables generate new data; contextual helpers echo back request data. Both can be used in the same example for maximum realism.

### Mock Server Configuration

**Response delays** — Simulate network latency by adding configurable delays (in milliseconds) to mock responses. This is critical for testing loading states, timeouts, and retry logic in client applications. Without delays, mocks respond instantly, which masks real-world UX issues.

**Private mock servers** — Restrict mock access to authenticated Postman users only. By default, mock URLs are public. Private mocks require an API key header, which prevents unauthorized access to prototype data and is essential for sensitive API designs.

**Matching settings** — Body matching and header matching can be toggled on or off at the mock server level. When turned on, the mock becomes more specific in its responses; when turned off, it falls back to URL-and-method matching only. The right setting depends on how many examples you have and how granular your test scenarios are.

### Postbot Documentation Generation

Postbot can auto-generate documentation for your collection, including endpoint descriptions, parameter explanations, and usage examples. In the prototyping workflow, use Postbot after building the collection structure to produce a first draft of documentation, then refine it manually. This accelerates the path from "we have endpoints" to "we have a documented prototype that stakeholders can review."

### Publishing Updates for Team Visibility

When changes are made to a prototype collection or mock server, workspace members need to know. Publishing workspace updates — adding comments, using the changelog, and broadcasting changes — ensures that everyone on the team stays informed. This is especially important in the prototyping phase when the contract is still evolving and breaking changes are common.

### Testing Mock Servers via cURL

Mock servers are not limited to Postman. Any HTTP client can hit a mock URL, including cURL from the command line. This is important for two reasons: (1) it proves that the mock behaves like a real API to external consumers, and (2) it enables integration with scripts, CI pipelines, and other tools that don't use the Postman UI.

Example:
```
curl -X GET https://mock-id.mock.pstmn.io/accounts/123 \
  -H "x-mock-response-name: success" \
  -H "x-api-key: your-mock-api-key"
```

## Activities

### PostVehicle Scenario: Collaborative Account API Prototype

**Setup:** Participants work in pairs (representing Poe and Petra from the PostVehicle team). The goal is to collaboratively build an Account API prototype that the frontend team can integrate against before the backend is built.

**Phase 1: Workspace and Collection Setup (15 min)**
- Create a shared team workspace called "PostVehicle Account API Prototype"
- Build a collection with the following endpoints:
  - `POST /accounts` — Create a new account
  - `GET /accounts/{{accountId}}` — Retrieve account details
  - `PUT /accounts/{{accountId}}` — Update account information
  - `GET /accounts/{{accountId}}/vehicles` — List vehicles for an account

**Phase 2: Add Examples with Contextual Responses (20 min)**
- For `POST /accounts`, create an example that uses `{{$body 'name'}}` and `{{$body 'email'}}` in the response to echo back submitted data, plus `{{$randomUUID}}` for the account ID and `{{$isoTimestamp}}` for created_at.
- For `GET /accounts/{{accountId}}`, create a success example and a 404 example. Use `{{$pathSegments '1'}}` to return the requested account ID in the success response.
- For `GET /accounts/{{accountId}}/vehicles`, create an example that returns a list filtered by the account from `{{$pathSegments '1'}}`.

**Phase 3: Create and Configure the Mock Server (10 min)**
- Create a mock server from the collection.
- Enable body matching for the POST endpoint.
- Set a 500ms delay to simulate realistic network latency.
- Make the mock private and note the API key.

**Phase 4: Test via Postman and cURL (15 min)**
- Test each endpoint in Postman using x-mock-response-name headers to explicitly select examples.
- Test the POST endpoint twice with different body data to see contextual responses change.
- Test the GET endpoint via cURL from the terminal.
- Verify that the 404 example returns correctly when using x-mock-response-code: 404.

**Phase 5: Publish and Share (10 min)**
- Add comments to the collection documenting design decisions.
- Use Postbot to generate endpoint documentation.
- Publish a workspace update announcing the prototype is ready for frontend integration.

**Expected Outcome:** Each pair has a live, documented mock server with contextual responses that behaves realistically enough for the frontend team to build against.

## Postman Features in This Module

### Mock Servers
The core feature of this module. Participants go beyond basic mocking to configure matching strategies, response delays, privacy settings, and contextual template helpers. They learn that mock servers are not just stubs — they are configurable prototyping tools that simulate real API behavior.

### Examples
Examples are the building blocks of mock responses. Each request can have multiple examples representing different scenarios (success, error, edge case). The matching strategy determines which example is returned for a given request.

### Collections
Collections serve as the container for the API prototype. The collection structure (folders, request order, documentation) becomes the shareable artifact that the team reviews and iterates on.

### Variables
Variables ({{accountId}}, {{base_url}}) decouple requests from hardcoded values. In prototyping, this means the same collection works against the mock, staging, or production by swapping environments.

### Environments
Environments store the mock server URL and API key. Participants create a "Mock" environment and later a "Production" environment, demonstrating how to switch contexts without editing requests.

### Workspaces
Workspaces are the collaboration layer. Team members see the same collections, mock servers, and environments. Comments and changelogs keep everyone aligned during the prototyping phase.

### Postbot
Postbot accelerates documentation by generating endpoint descriptions and usage guidance from the collection structure. In this module, it is used after the prototype is built to produce stakeholder-ready documentation.

### Collection Runner
The Collection Runner is used to execute the full set of prototype requests in sequence, validating that all mock responses return correctly. This serves as a smoke test for the prototype before sharing it with the team.

## Facilitator Notes

**Timing:** 70-80 minutes total (15 min setup, 20 min examples, 10 min mock config, 15 min testing, 10 min publishing, 10 min discussion).

**Prerequisites:** Participants should have completed 101-04 (Introduction to Mocking) or have equivalent experience creating basic mock servers and examples.

**Tips:**
- The contextual template helpers ($body, $pathSegments) are the "wow moment" of this module. Spend extra time here if participants are engaged. The difference between a static "hardcoded ID" response and a dynamic "echo back whatever you sent" response is immediately compelling.
- Pair work is important. One person should drive (type) while the other navigates (directs). Switch roles at Phase 3. This mirrors real collaborative prototyping.
- If participants ask "why not just build the real API?" — this is the teachable moment. Prototyping with mocks lets you validate the contract with consumers before investing in implementation. It catches design mistakes early.
- The cURL testing step often surprises participants who assume mocks only work inside Postman. Emphasize that mock URLs are standard HTTP endpoints.

**Common Questions:**
- "What happens if no example matches?" — The mock returns a default response (usually the first example). Walk through the matching priority order.
- "Can I use contextual helpers in headers, not just the body?" — Yes, template helpers work in response headers too.
- "How long does the mock server stay active?" — Cloud mocks persist as long as the collection exists. They don't expire.
- "Can I version my mock?" — The mock always reflects the current state of the collection. To version, create a fork of the collection and mock the fork.

**v11 Note:** These materials reflect the v11 mock server interface and matching behavior. The hub monitors for v12 changes that may affect template helper syntax, matching priority, or configuration UI.

## Pain Points Addressed

**Mock Responses Are Too Static and Don't Simulate Real API Behavior**
- Problem: Basic mocks return the same hardcoded JSON every time, regardless of input. Consumers can't test realistic scenarios like "what happens when I submit different data?"
- Solution: Contextual template helpers ($body, $pathSegments, $headers, $queryParams) make mock responses dynamic. The mock echoes back request data, simulating real server behavior without a backend.
- Postman Feature: Examples with template helpers, Mock Servers

**Teams Struggle to Coordinate on API Design Without a Shared Prototype**
- Problem: API design happens in documents, Slack threads, and meetings. There is no single artifact that the whole team can interact with, test, and iterate on.
- Solution: A shared workspace with a mock server gives the team a live, testable prototype. Comments, changelogs, and workspace updates keep everyone aligned.
- Postman Feature: Workspaces, Mock Servers, Collections, Comments

**No Way to Test API Consumers Without a Running Backend**
- Problem: Frontend and mobile teams are blocked until the backend is built. They can't start integration work because there is nothing to call.
- Solution: Mock servers provide a live HTTP endpoint that behaves like the real API. Consumers can integrate against the mock immediately, and switch to the real backend later by changing the environment.
- Postman Feature: Mock Servers, Environments, Variables
