---
id: 101-03
title: "Testing APIs"
program: 101
owner: Marcus Kidan
change_sensitivity: high
status: current
last_updated: 2026-04-28
last_audited: 2026-04-28

postman_features:
  - Test Scripts
  - Collection Runner
  - Postbot
  - Package Library
  - Collections
  - Environments
  - Scheduled Runs

update_triggers:
  - "Test script syntax or API changes"
  - "Collection Runner UI changes"
  - "Postbot capability updates"
  - "Package Library changes"
  - "Script execution order changes"
---

## Overview

Introduces API testing fundamentals using Postman's testing tools. Participants learn the typical testing workflow, how to write test scripts using code snippets, organize tests at collection/folder/request levels, use Postbot for AI-assisted test generation, leverage shared packages for reusable test logic, and automate collection runs with the Collection Runner. These are v11 materials; the hub monitors for v12 changes.

## Learning Objectives

- Write post-response test scripts for common validation patterns (status codes, response format, data accuracy)
- Organize tests at collection, folder, and request levels understanding execution order
- Use the Collection Runner to automate test execution
- Leverage Postbot and shared packages to accelerate test development

## Key Elements

### The Typical Testing Workflow

API testing follows a predictable cycle. Understanding this cycle helps you write better tests and diagnose failures faster.

1. **Prepare** — Set up the request: URL, headers, authentication, request body. Use pre-request scripts to generate dynamic data or fetch tokens.
2. **Validate the setup** — Confirm variables are resolved, the environment is correct, and prerequisites are met.
3. **Send the request** — Execute the API call.
4. **Check the response** — Run post-response test scripts that assert expected behavior.
5. **Debug failures** — When tests fail, inspect the response body, headers, status code, and timing to diagnose the issue.
6. **Iterate** — Fix the issue (in the API or the test) and re-run.

This cycle applies whether you're testing manually (one request at a time) or automated (collection runs with hundreds of requests).

### Writing Test Scripts

Test scripts in Postman are JavaScript code that runs after a response is received. They use the `pm` library to make assertions about the response.

**Status Code Validation:**
The most basic test — did the API return the expected HTTP status code?
```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});
```

**Response Format Validation:**
Confirm the response is JSON and has the expected Content-Type header.
```javascript
pm.test("Response is JSON", function () {
    pm.response.to.have.header("Content-Type", "application/json; charset=utf-8");
    pm.response.to.be.json;
});
```

**Data Accuracy:**
Check that specific fields exist and contain expected values.
```javascript
pm.test("Response contains user email", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData.email).to.be.a("string");
    pm.expect(jsonData.email).to.include("@");
});
```

**Response Time:**
Ensure the API responds within acceptable limits.
```javascript
pm.test("Response time is under 500ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(500);
});
```

**Authentication Validation:**
Verify that unauthorized requests are properly rejected.
```javascript
pm.test("Returns 401 without auth token", function () {
    pm.response.to.have.status(401);
    const jsonData = pm.response.json();
    pm.expect(jsonData.error).to.eql("Unauthorized");
});
```

### The Code Snippet Library

You don't need to memorize test syntax. Postman provides a code snippet library — a sidebar of pre-written test patterns you can click to insert. Common snippets include:

- Status code is 200
- Response body contains string
- Response time is less than 200ms
- Response body is JSON
- Response has specific header
- Set an environment variable from response

Snippets are starting points. Click one, then customize it for your specific endpoint. This dramatically reduces the barrier to writing tests — you go from "I don't know JavaScript" to "I have a working test" in seconds.

### Postbot: AI-Assisted Testing

Postbot is Postman's AI assistant that accelerates test development in several ways:

**Writing Tests:**
Describe what you want to test in natural language, and Postbot generates the test script. Example: "Write a test that verifies the response contains an array of users, each with an id, name, and email field" — Postbot produces the JavaScript.

**Debugging Failures:**
When a test fails, Postbot can analyze the response and suggest why the assertion didn't pass. It reads the test code, the actual response, and identifies the mismatch.

**Generating Documentation:**
Postbot can generate endpoint descriptions and parameter documentation from the request and response structure, reducing manual documentation effort.

**Best Practice Suggestions:**
Postbot can review your existing tests and suggest improvements — missing edge cases, redundant assertions, or better assertion patterns.

### Package Library: Shared Reusable Test Logic

The Package Library lets teams create and share reusable test utilities. Instead of copying the same validation logic across 50 collections, you write it once and import it everywhere.

**Common Shared Packages:**
- Response schema validators (verify JSON structure matches expected schema)
- Authentication helpers (token refresh logic, OAuth flow utilities)
- Data generators (random user data, valid/invalid inputs for fuzz testing)
- Custom assertion libraries (domain-specific validation patterns)

**How It Works:**
1. A team member creates a package with reusable functions
2. The package is published to the team's Package Library
3. Other collections import the package and call its functions in test scripts
4. When the package is updated, all consuming collections get the latest version

This eliminates the "copy-paste-modify" pattern that leads to test logic divergence across teams.

### Script Execution Order: Collection, Folder, Request

Understanding execution order is critical for organizing tests effectively. When Postman runs a request, scripts execute in this order:

**Pre-request scripts:**
1. Collection-level pre-request script
2. Folder-level pre-request script
3. Request-level pre-request script

**Post-response scripts (tests):**
1. Collection-level test script
2. Folder-level test script
3. Request-level test script

**Why This Matters:**

Put common setup in collection-level pre-request scripts (e.g., refresh auth token). Put shared assertions in folder-level tests (e.g., "all endpoints in this folder return JSON"). Put endpoint-specific assertions in request-level tests (e.g., "this endpoint returns a user object with these fields").

This hierarchy prevents duplication. If every endpoint should return JSON, write that test once at the collection level — not 50 times at the request level.

### Collection Runner

The Collection Runner executes an entire collection (or folder) sequentially, running all pre-request scripts, sending all requests, and executing all test scripts. It produces a summary report showing pass/fail counts.

**Key Features:**
- **Environment selection** — Choose which environment to run against (dev, staging, prod)
- **Iteration count** — Run the collection multiple times (useful with data files)
- **Data file input** — Supply a CSV or JSON file to parameterize requests across iterations
- **Delay between requests** — Add pauses to avoid rate limiting
- **Run order** — Requests execute in collection order, top to bottom

### Scheduled Collection Runs

Beyond manual runs, you can schedule collections to run automatically on a recurring basis:

- **Frequency** — Hourly, daily, weekly, or custom cron schedules
- **Notifications** — Get alerted when tests fail (email, Slack, webhooks)
- **History** — View past run results to identify trends (flaky tests, performance degradation)
- **Environment pinning** — Schedule runs against a specific environment

Scheduled runs turn your collection into a continuous monitoring tool. A collection that tests your production API every hour is a lightweight uptime monitor.

## Activities

### PostVehicle Scenario

PostVehicle Enterprises has a Remote Services API that controls vehicle functions (lock, unlock, start engine, check battery). Your team needs to build a test suite to validate the API before the next release.

**Phase 1: Add Test Scripts to Individual Endpoints**

Start with manual test scripts on key endpoints:
1. Open the Remote Services API collection
2. Navigate to the "Lock Vehicle" endpoint (POST /vehicles/{id}/lock)
3. Add a test script that validates: status code is 200, response contains `{ "status": "locked" }`, response time is under 1 second
4. Navigate to "Get Vehicle Status" (GET /vehicles/{id}/status)
5. Add a test that validates the response contains battery_level (number), location (object with lat/lng), and lock_status (string)
6. Send each request and verify tests pass (green checkmarks in the test results panel)

**Phase 2: Use Code Snippets and Postbot**

Accelerate test writing with tooling:
1. On the "Unlock Vehicle" endpoint, open the code snippet sidebar
2. Insert the "Status code is 200" snippet and the "Response body is JSON" snippet
3. Use Postbot to generate a comprehensive test: prompt it with "Write tests that verify the unlock response contains a status field of 'unlocked', a timestamp in ISO format, and the vehicle_id matches the request parameter"
4. Review and adjust the generated test — Postbot gets you 80% of the way, but domain-specific logic may need tweaking

**Phase 3: Import Shared Test Packages**

Leverage the team's existing test utilities:
1. Browse the Package Library for PostVehicle's shared packages
2. Import the "Response Schema Validator" package
3. Import the "Auth Token Refresh" package
4. Use the schema validator in a test script to validate the Get Vehicle Status response against the expected schema
5. Add the auth token refresh logic to the collection-level pre-request script

**Phase 4: Organize Tests at Folder Level**

Move common tests up the hierarchy:
1. Create a folder-level test script for the "Vehicle Commands" folder
2. Move common assertions there: status code is 200, response is JSON, response time under 2 seconds
3. Remove duplicate assertions from individual request tests
4. Verify that tests still pass — folder-level tests run before request-level tests

**Phase 5: Run with Collection Runner and Schedule**

Automate the full test suite:
1. Open the Collection Runner
2. Select the Remote Services API collection
3. Choose the "PostVehicle - Dev" environment
4. Run the collection and review the summary report
5. Identify any failures and debug using the response details
6. Schedule the collection to run daily against the development environment
7. Configure failure notifications to alert the team channel

### Expected Outcome

By the end of this activity, each participant has:
- Test scripts on individual endpoints covering status codes, response format, and data accuracy
- Experience using code snippets and Postbot for test generation
- Shared packages imported and used in test scripts
- Tests organized at collection, folder, and request levels
- A Collection Runner execution with pass/fail summary
- A scheduled run configured for continuous testing

## Postman Features in This Module

### Test Scripts
The core feature of this module. Participants write JavaScript test scripts using the `pm` library, learning common assertion patterns. Test scripts are positioned as the mechanism that turns a collection from "a bunch of requests" into "a test suite."

### Collection Runner
The Collection Runner automates what would otherwise be manual, one-at-a-time request execution. Participants run their full test suite and see aggregate results. This is the bridge between "I have tests" and "I have automated testing."

### Postbot
Postbot accelerates test development by generating test scripts from natural language descriptions. Participants experience the productivity gain of describing what they want to test and getting working code back. The module emphasizes that Postbot is an accelerator, not a replacement — generated tests still need human review.

### Package Library
The Package Library enables test logic reuse across teams. Participants import shared packages and use them in their test scripts, seeing how centralized utilities prevent copy-paste duplication and ensure consistency.

### Collections
Collections are the organizational container for tests. The module teaches participants to think of collection structure as test architecture — folders map to test categories, and the hierarchy determines script execution order.

### Environments
Environments enable the same test suite to run against different targets. Participants switch between dev and staging environments without modifying any test code — the variables handle the differences.

### Scheduled Runs
Scheduled runs turn test suites into continuous monitors. Participants configure daily runs with failure alerts, understanding that a scheduled collection run is the simplest form of API monitoring.

## Facilitator Notes

**Timing:** 90 minutes total (25 for teaching testing concepts, 50 for hands-on activities, 15 for review and discussion).

**Setup Requirements:**
- Pre-create the Remote Services API collection with working endpoints (use a mock server if a live API isn't available)
- Pre-publish shared packages to the Package Library (Response Schema Validator, Auth Token Refresh)
- Ensure participants have the "PostVehicle - Dev" environment from Module 101-01
- Test the scheduled run configuration — permissions may vary by team plan

**Tips:**
- JavaScript anxiety is real. Many participants will freeze when they see a code editor. Start with code snippets — clicking a button to insert working code is much less intimidating than writing from scratch. Postbot is the next step. By the time participants need to write custom logic, they've already seen dozens of working examples.
- The execution order (collection > folder > request) is the most conceptually important lesson. Draw it on a whiteboard. Run a collection with `console.log` statements at each level to show the order visually. This prevents the common mistake of putting the same assertion at every level.
- When participants use Postbot, ask them to review every generated test critically. "Does this test actually validate what you care about, or does it just check that the response isn't empty?" This builds good testing instincts.
- If the Package Library isn't available on the team's plan, demonstrate it and have participants simulate the pattern by copying utility functions into collection-level scripts.

**Common Questions:**
- "Do I need to know JavaScript?" — You need enough to read and modify test scripts. The snippet library and Postbot handle most code generation. Over time, you'll naturally learn the patterns.
- "What's the difference between pre-request and post-response scripts?" — Pre-request runs before the API call (setup), post-response runs after (validation). Think of them as "prepare" and "check."
- "Can I share test results with my manager?" — Yes, Collection Runner generates reports that can be exported. Scheduled runs maintain a history dashboard.
- "How do I test error cases?" — Send a deliberately bad request (wrong ID, missing auth, invalid body) and write tests that assert the expected error response.

## Pain Points Addressed

**Writing and Maintaining Test Scripts Is Tedious and Repetitive**
Without tooling, every test is hand-written JavaScript. The same "check status code 200" assertion gets written hundreds of times across an organization. Code snippets, Postbot, and the Package Library each attack a different dimension of this problem: snippets handle common patterns, Postbot handles custom logic, and packages handle shared utilities. Together, they reduce test authoring time from hours to minutes.

**Test Logic Gets Duplicated Across Teams**
When Team A writes a response schema validator and Team B writes their own slightly different version, the organization has two validators to maintain, debug, and update. The Package Library centralizes shared test logic. One package, maintained by one team, consumed by everyone. When the package improves, every consumer benefits automatically.

**No Visibility Into Which Tests Are Passing/Failing Across the Organization**
Without scheduled runs and dashboards, test results live in individual developers' Postman instances. Nobody has an aggregate view of API health. Scheduled collection runs with notification integration create organizational visibility: "The Vehicle API test suite has been failing since Tuesday" becomes a team-level signal, not a hidden individual problem.
