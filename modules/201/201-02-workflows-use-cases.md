---
id: 201-02
title: "Building Use Cases and Workflows"
program: 201
owner: Marcus Kidan
change_sensitivity: high
status: current
last_updated: 2026-04-28
last_audited: 2026-04-28

postman_features:
  - Collections
  - Pre-request Scripts
  - Post-response Scripts
  - Variables
  - Environments
  - Collection Runner
  - Postbot
  - Authentication

update_triggers:
  - "Script execution changes"
  - "Variable scope changes"
  - "Collection Runner updates"
  - "Authentication feature changes"
  - "Postbot capability updates"
---

## Overview

Teaches how to build executable workflow documentation that chains multiple API calls together. Participants learn to orchestrate requests across different APIs using variables and scripts, manage authentication across services (API keys vs JWT tokens), use local variables for secure temporary data, leverage Postbot for documentation generation, and run complete workflows with the Collection Runner. These are v11 materials; the hub monitors for v12 changes.

## Learning Objectives

- Build collections that chain requests across multiple APIs into executable workflows
- Manage different authentication methods within a single collection (API keys, JWT tokens)
- Use local variables to securely store temporary sensitive data during collection runs
- Write pre-request and post-response scripts that extract and pass data between requests

## Key Elements

### Workflow Documentation: Executable Docs for Specific Use Cases

Traditional API documentation describes individual endpoints in isolation: "POST /users creates a user," "POST /cart adds an item." But real-world use cases require multiple endpoints called in a specific sequence. "Register a user, authenticate, add items to cart, and check out" is a workflow — a series of API calls that together accomplish a business process.

A Postman collection can serve as executable workflow documentation. Each request in the collection represents one step. Scripts between requests handle data extraction and passing. When you click "Run" in the Collection Runner, the entire workflow executes end-to-end. This is documentation that proves itself — if the workflow runs successfully, the documentation is accurate.

The shift from "here are our endpoints" to "here is how you accomplish this use case" is the difference between a reference manual and a recipe book. Both are useful, but recipes are what people actually follow.

### Cross-API Orchestration

Real workflows often span multiple APIs owned by different teams or even different vendors. A "Register and subscribe" workflow might touch:

- **User API** — Create account, authenticate, retrieve profile
- **Cart API** — Add subscription item, apply promo code, check out

Each API may use a different authentication method. The User API might use an API key for registration and return a JWT token for subsequent calls. The Cart API might accept that JWT token for user-scoped operations but require a separate API key for admin endpoints.

Managing this in a single collection requires understanding how to set authorization at different levels (collection, folder, request) and how to override inherited auth when needed.

### Script Execution Order

Scripts in Postman execute in a specific, predictable order. Understanding this order is essential for building reliable workflows:

1. **Collection-level pre-request script** — Runs before every request in the collection. Use for shared setup logic (e.g., checking if a token is expired).
2. **Folder-level pre-request script** — Runs before every request in that folder. Use for folder-specific setup (e.g., setting API-specific headers).
3. **Request-level pre-request script** — Runs before this specific request. Use for request-specific preparation (e.g., generating a unique username).
4. **The request fires.**
5. **Collection-level post-response script** — Runs after every request. Use for shared validation (e.g., logging all response times).
6. **Folder-level post-response script** — Runs after every request in that folder. Use for API-specific response handling.
7. **Request-level post-response script** — Runs after this specific request. Use for extracting data from the response (e.g., saving a JWT token).

The order is always collection then folder then request, for both pre-request and post-response phases. This layered model lets you put shared logic at higher levels and specific logic at the request level, reducing duplication.

### Local Variables: Secure Temporary Data

Local variables (set via `pm.variables.set()`) are the most restricted variable scope in Postman. They exist only for the duration of a single collection run and are never persisted to Postman's servers.

This makes them ideal for sensitive data like JWT tokens, session IDs, and temporary credentials. Unlike environment or collection variables, local variables:

- Disappear when the run completes
- Are never synced to the cloud
- Cannot be accidentally shared with team members
- Do not appear in exported collections

In a workflow, the pattern is: a post-response script extracts the JWT token from a login response and stores it as a local variable. Subsequent requests reference `{{jwt_token}}` in their authorization header. When the run ends, the token is gone. No cleanup needed, no security risk from stale tokens sitting in environment variables.

```javascript
// Post-response script on the login request
const response = pm.response.json();
pm.variables.set("jwt_token", response.token);
```

```javascript
// Pre-request script on subsequent requests (or set in Authorization tab)
// Authorization header: Bearer {{jwt_token}}
```

### Collection-Level vs Request-Level Authorization

Postman allows setting authorization at the collection level, which all requests inherit by default. Individual requests can override this inheritance.

In a cross-API workflow, the pattern is:
- Set the **collection-level auth** to the most common method (e.g., API key for the User API).
- For requests that need different auth (e.g., JWT for authenticated endpoints), override at the request level or folder level.
- For the Cart API folder, set folder-level auth to use the JWT token extracted from the login response.

The "Inherit from parent" option in the Authorization tab is the default. When you explicitly set auth on a request, it overrides the parent. This inheritance model keeps the collection clean — you only specify auth where it differs from the default.

### Dynamic Variables for Test Data

When building workflows that create resources, you need unique test data for each run. Hardcoded values like "testuser@example.com" will fail on the second run because the user already exists. Dynamic variables ($randomUserName, $randomFullName, $randomEmail, $randomUUID) generate unique data each time, ensuring every workflow run creates fresh, non-colliding test data.

### Postbot for Documentation Generation

After building the workflow, use Postbot to generate documentation that explains each step. Postbot can describe what each request does, what parameters it expects, and what the expected response looks like. This turns your executable workflow into a self-documenting artifact — the collection both runs the workflow and explains it.

The generated documentation is a starting point. Add business context manually: why this step exists, what happens if it fails, what the user should see at each stage. The combination of auto-generated technical docs and human-written business context creates comprehensive workflow documentation.

### Collection Runner for Workflow Execution

The Collection Runner executes every request in a collection (or folder) in sequence, passing data between requests via variables. For workflow collections, the Runner is the "play" button — it proves the workflow works end-to-end.

Key Runner settings for workflows:
- **Iteration count** — Run the workflow multiple times (useful with dynamic variables to test with different data each time).
- **Delay between requests** — Add pauses to avoid rate limiting or simulate realistic timing.
- **Data file** — Supply external CSV/JSON data to drive the workflow (covered in 201-04).
- **Persist responses** — Save responses for review after the run completes.

The Runner output shows each request's status, response time, and pass/fail result. A green run means the workflow is valid; a red request pinpoints where it breaks.

## Activities

### PostVehicle Scenario: Register and Subscribe to a Service

**Setup:** Participants build an end-to-end workflow that registers a new PostVehicle user and subscribes them to the Remote Services package. This workflow spans two APIs (User API and Cart API) with different authentication methods.

**Phase 1: Environment Setup (10 min)**
- Create an environment called "PostVehicle Dev" with the following variables:
  - `user_api_url` — Base URL for the User API
  - `cart_api_url` — Base URL for the Cart API
  - `user_api_key` — API key for the User API (set as secret type)
  - `cart_api_key` — API key for the Cart API (set as secret type)

**Phase 2: Build the Workflow Collection (20 min)**
- Create a collection called "Register and Subscribe Workflow"
- Set collection-level auth to API Key using `{{user_api_key}}`
- Create the following request sequence:

  **Folder: User Registration**
  1. `POST {{user_api_url}}/users` — Register a new user with `{{$randomFullName}}` and `{{$randomEmail}}` in the body
  2. `POST {{user_api_url}}/auth/login` — Authenticate with the new user credentials

  **Folder: Subscription**
  3. `GET {{cart_api_url}}/services` — List available services (uses Cart API key)
  4. `POST {{cart_api_url}}/cart` — Add Remote Services package to cart
  5. `POST {{cart_api_url}}/cart/checkout` — Complete the subscription

**Phase 3: Write Scripts to Chain Requests (20 min)**
- On the Register request: add a post-response script that extracts the user ID and email, stores them as local variables
- On the Login request: add a post-response script that extracts the JWT token and stores it as a local variable using `pm.variables.set("jwt_token", response.token)`
- On the Subscription folder: set folder-level auth to Bearer Token using `{{jwt_token}}`
- On the Add to Cart request: add a pre-request script that uses the service ID from the List Services response
- On the Checkout request: add a post-response script that validates the subscription was created successfully

```javascript
// Example: Post-response script on Login request
const response = pm.response.json();
pm.variables.set("jwt_token", response.data.token);
pm.variables.set("user_id", response.data.user.id);
console.log("JWT token stored as local variable (will not persist after run)");
```

**Phase 4: Run the Workflow (15 min)**
- Open the Collection Runner
- Select the "Register and Subscribe Workflow" collection
- Set iteration count to 1
- Run the workflow end-to-end
- Review the results — each request should show a green status
- Run again with iteration count 3 to verify dynamic variables create unique users each time

**Phase 5: Document and Share (10 min)**
- Use Postbot to generate documentation for each request
- Add a collection description explaining the business use case: "This workflow demonstrates the complete user registration and subscription flow for PostVehicle Remote Services"
- Add comments on the Login request explaining the JWT token extraction pattern

**Expected Outcome:** A fully executable workflow collection that registers a user, authenticates, and completes a subscription — all driven by scripts and variables with no manual intervention between steps.

## Postman Features in This Module

### Collections
Collections serve as the container for the workflow. The folder structure (User Registration, Subscription) organizes requests by API and business phase. The collection becomes executable documentation of the use case.

### Pre-request Scripts
Pre-request scripts run before each request to prepare data. In this module, they set up dynamic test data, check for required variables, and configure request-specific parameters based on data extracted from previous responses.

### Post-response Scripts
Post-response scripts run after each response to extract and store data. The critical pattern is extracting a JWT token from a login response and storing it as a local variable for subsequent requests. This is the "glue" that chains requests into a workflow.

### Variables
Variables at multiple scopes (environment, local, dynamic) enable the workflow to be portable and secure. Environment variables store configuration, local variables store sensitive temporary data, and dynamic variables generate unique test data.

### Environments
Environments allow the same workflow to run against different backends (Dev, Staging, Production) by swapping configuration. The API URLs and keys change; the workflow logic stays the same.

### Collection Runner
The Collection Runner is the execution engine for workflows. It runs requests in sequence, respects scripts, and reports pass/fail status for each step. It is the tool that proves the workflow works.

### Postbot
Postbot generates documentation from the collection structure, turning the executable workflow into a human-readable guide. It describes endpoints, parameters, and expected responses.

### Authentication
This module demonstrates managing multiple auth methods (API keys, JWT tokens) within a single collection using inheritance and overrides. Collection-level auth sets the default; folder and request-level auth override where needed.

## Facilitator Notes

**Timing:** 75-85 minutes total (10 min environment, 20 min collection building, 20 min scripting, 15 min running, 10 min documentation, 10 min discussion).

**Prerequisites:** Participants should be comfortable with basic Postman collections, environments, and variables. Familiarity with JavaScript basics is helpful for the scripting phase but not strictly required — the scripts are provided as templates.

**Tips:**
- The scripting phase is where participants struggle most. Have the script snippets ready to paste. The goal is understanding the pattern (extract token, store as local variable, reference in next request), not memorizing JavaScript syntax.
- The local variable security benefit is a key selling point. Demonstrate it by running the workflow, then checking the environment — the JWT token is not there. It existed only during the run. This often generates an "aha" moment.
- If the User API or Cart API is unavailable, have a backup mock server ready. The workflow pattern is the lesson, not the specific APIs.
- The iteration count feature surprises many participants. Running the workflow 3 times and seeing 3 different users created (thanks to dynamic variables) demonstrates both the Runner's power and why dynamic variables matter.

**Common Questions:**
- "Why not store the JWT token in an environment variable?" — You can, but it persists after the run, syncs to the cloud, and is visible to team members. Local variables are more secure for tokens.
- "What if a request in the middle fails?" — The Runner stops at the failing request (by default). You can configure it to continue, but for workflows, stopping on failure is usually what you want.
- "Can I reorder the requests?" — Yes, drag and drop. But the workflow logic (scripts that depend on previous responses) must match the order. This is a common source of bugs.
- "How is this different from a test suite?" — A workflow collection proves a use case works. A test suite asserts that individual endpoints behave correctly. They overlap but serve different purposes. 201-04 covers testing in depth.

**v11 Note:** These materials reflect v11 script execution order and variable scoping behavior. The hub monitors for v12 changes that may affect script lifecycle, variable persistence, or Collection Runner behavior.

## Pain Points Addressed

**No Documented Examples of How to Use Multiple APIs Together for a Business Process**
- Problem: API documentation describes individual endpoints, but real use cases require calling multiple endpoints across multiple APIs in a specific sequence. Developers piece together the workflow through trial and error.
- Solution: Workflow collections serve as executable documentation. Each request is a step, scripts handle the data flow, and the Collection Runner proves it works. The collection is both the documentation and the proof.
- Postman Feature: Collections, Collection Runner, Pre-request Scripts, Post-response Scripts

**Authentication Handoffs Between Services Are Complex and Error-Prone**
- Problem: A workflow that spans two APIs with different auth methods (API key for one, JWT for the other) requires careful credential management. Developers manually copy tokens between tools, miss auth headers, or use the wrong credentials.
- Solution: Collection and folder-level auth inheritance lets you set the default once and override where needed. Post-response scripts automatically extract tokens and store them for subsequent requests. The workflow handles auth transitions seamlessly.
- Postman Feature: Authentication, Post-response Scripts, Variables

**Sensitive Tokens Stored in Plain Text in Environment Variables**
- Problem: JWT tokens and session credentials stored in environment variables persist after the workflow finishes, sync to the cloud, and are visible to anyone with access to the environment. This is a security risk.
- Solution: Local variables (`pm.variables.set()`) exist only for the duration of a single collection run. They are never persisted, never synced, and never shared. When the run ends, the token is gone.
- Postman Feature: Variables (local scope)
