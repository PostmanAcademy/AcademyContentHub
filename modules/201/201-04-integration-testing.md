---
id: 201-04
title: "Integration Testing and CI/CD"
program: 201
owner: Marcus Kidan
change_sensitivity: high
status: current
last_updated: 2026-04-28
last_audited: 2026-04-28

postman_features:
  - Test Scripts
  - Collection Runner
  - Postman CLI
  - Scheduled Runs
  - Package Library
  - Collections
  - Environments
  - Variables

update_triggers:
  - "Postman CLI changes"
  - "Collection Runner updates"
  - "Script execution changes"
  - "Package Library changes"
  - "Scheduled run or monitor changes"
  - "Data file handling updates"
---

## Overview

Advanced testing techniques including integration test suites that validate multi-API workflows, data-driven testing with CSV/JSON files, external library loading in scripts, controlling execution order with pm.execution methods, scheduled runs for regression testing, and Postman CLI for CI/CD pipeline integration. These are v11 materials; the hub monitors for v12 changes.

## Learning Objectives

- Build integration test suites that validate workflows across multiple APIs
- Use data files (CSV/JSON) to drive parameterized test runs with multiple iterations
- Control execution flow using pm.execution.skipRequest() and postman.setNextRequest()
- Integrate collection runs into CI/CD pipelines using the Postman CLI

## Key Elements

### Integration Testing Strategy: Setup, Test, Cleanup

Integration tests validate that multiple APIs work together correctly. Unlike unit tests (which test a single endpoint in isolation), integration tests exercise a complete workflow — create a user, add a vehicle, subscribe to a service, verify the subscription, then clean up.

The recommended folder structure for integration test collections is:

```
Integration Tests/
  Setup/
    Create test user
    Authenticate
    Create test vehicle
  Tests/
    Verify vehicle registration
    Verify service subscription
    Verify billing record
  Cleanup/
    Delete test vehicle
    Delete test user
```

**Setup** creates the preconditions. **Tests** validate the behavior. **Cleanup** removes test data so the next run starts fresh. This three-phase structure ensures tests are repeatable and do not pollute the target environment with leftover data.

The cleanup phase is often skipped by teams who are new to integration testing. This is a mistake — stale test data accumulates, causes false failures, and makes the test environment unreliable. Always clean up.

### Data-Driven Testing

Data-driven testing uses external files (CSV or JSON) to run the same collection multiple times with different input data. Instead of hardcoding a single test case, you define a data file with multiple rows, and the Collection Runner iterates through each row.

**CSV example:**
```csv
vin,make,model,year,expected_status
WBA12345678901234,BMW,X5,2024,200
JH4KA7650NC000001,Acura,Integra,1992,200
INVALID_VIN_12345,Unknown,Unknown,0,400
,,,0,422
```

**JSON example:**
```json
[
  {"vin": "WBA12345678901234", "make": "BMW", "model": "X5", "year": 2024, "expected_status": 200},
  {"vin": "INVALID_VIN_12345", "make": "Unknown", "model": "Unknown", "year": 0, "expected_status": 400},
  {"vin": "", "make": "", "model": "", "year": 0, "expected_status": 422}
]
```

In scripts, access data file values using `pm.iterationData.get("vin")` or use `{{vin}}` directly in request bodies and URLs. The data variable syntax `{{vin}}` works in request fields just like environment variables.

Data-driven testing is powerful for:
- **Boundary testing** — Valid inputs, invalid inputs, empty inputs, edge cases
- **Multi-tenant testing** — Run the same workflow for different user accounts
- **Regression testing** — A growing data file becomes your regression suite

### External Libraries in Scripts

Postman scripts run in a sandboxed JavaScript environment, but you can load external libraries using `pm.sendRequest()` to fetch a script file and `eval()` to execute it.

The pattern: use `pm.sendRequest()` to fetch the library URL, then `eval(res.text())` to make its functions available in the script scope. This is useful for specialized validation (VIN format checking, IBAN validation, custom business rules) that would be complex to write inline. The library can be hosted on a CDN, internal server, or even a Postman mock server.

**Caution:** `eval()` executes arbitrary code. Only load libraries from trusted sources. In a corporate environment, host libraries internally.

### Controlling Execution Order

By default, the Collection Runner executes requests in order from top to bottom. Two methods let you override this:

**pm.execution.skipRequest()** — Skips the current request without executing it. Useful for conditional logic: "If the user already exists, skip the create step."

```javascript
// Pre-request script
if (pm.variables.get("user_already_exists") === "true") {
    pm.execution.skipRequest();
}
```

**postman.setNextRequest("request_name")** — After the current request completes, jump to the named request instead of proceeding sequentially. This enables branching logic, loops, and conditional flows.

```javascript
// Post-response script
if (pm.response.json().status === "pending") {
    // Poll again — loop back to this same request
    postman.setNextRequest("Check Processing Status");
} else {
    // Done — proceed to the next request in the collection
    postman.setNextRequest("Verify Final Result");
}
```

**postman.setNextRequest(null)** — Stops the collection run immediately. Use this in the cleanup phase if a critical setup step fails and there is no point continuing.

These methods transform the Collection Runner from a linear executor into a programmable workflow engine. Use them judiciously — complex branching logic makes tests harder to understand and debug.

### Package Library for Shared Test Utilities

The Package Library allows teams to create reusable JavaScript modules that can be imported across collections. Instead of copying the same validation functions or helper scripts into every collection, publish them to the Package Library and import them.

Use cases include shared assertion helpers (`assertValidVIN()`), common setup functions (`createTestUser()`), data transformation utilities, and cross-team test standards. When validation rules change, update the library once and every importing collection gets the update automatically.

### Postman CLI

The Postman CLI (`postman`) runs collections from the command line, enabling integration with CI/CD pipelines. It replaces the older Newman tool with a Postman-native solution.

Key commands: `postman collection run <collection-id> -e <environment-id>` runs by ID (always uses latest version from Postman servers), while `postman collection run ./collection.json` runs from a local file. Add `-d test-data.csv` for data-driven runs and `--folder "Tests"` to run a specific folder.

The CLI returns standard exit codes: 0 for all tests passing, non-zero for failures. CI/CD pipelines use these exit codes to gate deployments. A typical GitHub Actions step installs the CLI, logs in with an API key, and runs the collection — three lines that connect Postman tests to your deployment pipeline.

### Cloud vs Local Runs

Cloud runs (Collection Runner UI, scheduled runs) execute on Postman's infrastructure with cloud-synced variables and team-visible results. Local runs (Postman CLI) execute on your machine or CI server, reading data files from the filesystem and outputting results to the terminal or JSON/JUnit reports. The key distinction: cloud runs access synced environment variables automatically; local runs need API-key-authenticated access or local environment files.

### Scheduled Collection Runs

Scheduled runs execute a collection on a recurring basis (hourly, daily, weekly) on Postman's cloud. Set up from the collection's Runs tab: choose frequency, select environment, optionally attach a data file, and enable failure notifications (email or Slack). Requirements: the collection must be in a workspace (not local), environment variables must be synced, and target APIs must be reachable from Postman's cloud servers. Scheduled runs are ideal for daily regression testing — the team finds out about overnight breakages from a notification, not a customer report.

## Activities

### PostVehicle Scenario: Integration Test Suite for Remote Services v2

**Setup:** Participants build a comprehensive integration test suite for the PostVehicle Remote Services v2 API. This suite tests the complete flow: authenticate a user, register a vehicle, subscribe to remote services, execute a remote command, and clean up.

**Phase 1: Build the Test Structure (15 min)**
- Create a collection called "Remote Services v2 — Integration Tests"
- Create three folders: Setup, Tests, Cleanup
- In Setup, add requests:
  - `POST /auth/login` — Authenticate as a test user
  - `POST /vehicles` — Register a test vehicle with a VIN from the data file
  - `POST /vehicles/{{vehicle_id}}/services` — Subscribe to Remote Services
- In Tests, add requests:
  - `GET /vehicles/{{vehicle_id}}/services` — Verify subscription is active
  - `POST /vehicles/{{vehicle_id}}/commands/lock` — Execute remote lock command
  - `GET /vehicles/{{vehicle_id}}/commands/{{command_id}}` — Check command status (with polling loop)
- In Cleanup, add requests:
  - `DELETE /vehicles/{{vehicle_id}}/services` — Cancel subscription
  - `DELETE /vehicles/{{vehicle_id}}` — Remove test vehicle

**Phase 2: External Library and Data-Driven Testing (20 min)**
- Write a pre-request script on the vehicle registration request that loads a VIN validation library using `pm.sendRequest()` and `eval()`, then uses `pm.execution.skipRequest()` to skip invalid VINs
- Create a CSV data file with test vehicles (2 valid VINs, 1 invalid, 1 empty) and run the collection with 4 iterations
- Review results: expect 2 successful flows, 1 skipped (invalid VIN), 1 validation error (empty VIN)

**Phase 3: Control Execution Flow (15 min)**
- On the "Check command status" request, add a polling loop: if status is "pending" and poll count is under 5, use `postman.setNextRequest("Check Command Status")` to loop back; if "completed," assert success; otherwise fail the test
- Run the collection and observe the polling behavior in the Runner output
- Discuss: this pattern handles asynchronous operations where the result is not immediately available

**Phase 4: Scheduled Runs and CLI (15 min)**
- Set up a daily scheduled run at 6:00 AM UTC with email notifications for failures
- Demonstrate the Postman CLI: `postman login`, then `postman collection run <id> -e <env-id> -d test-data.csv`
- Show the CLI output and discuss CI/CD pipeline integration (GitHub Actions, Jenkins, GitLab CI)

**Expected Outcome:** A complete integration test suite with data-driven testing, external library validation, execution flow control, scheduled runs, and CLI integration readiness.

## Postman Features in This Module

### Test Scripts
Test scripts (post-response scripts with `pm.test()`) are the assertion layer. They validate that responses contain the expected data, status codes, and structures. In integration testing, test scripts validate not just individual responses but the state built up across the entire workflow.

### Collection Runner
The Collection Runner executes the integration test suite, handling iterations (from data files), variable passing between requests, and result reporting. It is the primary tool for running integration tests locally before pushing them to CI/CD.

### Postman CLI
The Postman CLI bridges Postman collections and CI/CD pipelines. It runs collections from the command line with the same behavior as the Collection Runner, returns standard exit codes for pipeline gating, and supports data files and environment references.

### Scheduled Runs
Scheduled runs automate regression testing by running collections on a recurring basis. They execute on Postman's cloud infrastructure and notify the team of failures via email or Slack integration.

### Package Library
The Package Library enables sharing test utilities across collections and teams. Shared validation functions, assertion helpers, and setup scripts live in the library and are imported where needed, promoting consistency and reducing duplication.

### Collections
Collections are the container for integration test suites. The folder structure (Setup, Tests, Cleanup) organizes the test phases. The collection becomes a reusable, shareable, and automatable test artifact.

### Environments
Environments store the target API URLs, credentials, and configuration for test runs. Switching environments lets the same test suite run against Dev, Staging, or Production without modifying the collection.

### Variables
Variables at multiple scopes (environment, local, data, collection) enable parameterized testing and data passing between requests. Data variables from CSV/JSON files drive iterations. Local variables store temporary state during a run.

## Facilitator Notes

**Timing:** 75-90 minutes total (15 min structure, 15 min external library, 15 min data-driven testing, 15 min execution flow, 15 min scheduled runs and CLI, 15 min discussion).

**Prerequisites:** Participants should have completed 201-02 (workflows) and be comfortable with basic Postman scripting. Familiarity with CI/CD concepts (pipelines, gates, automated testing) is helpful but not required.

**Tips:**
- The data-driven testing phase is usually the most impactful. Emphasize that the data file is the test plan — adding a test case means adding a row, not writing new code.
- The polling loop pattern is advanced. Draw it on a whiteboard: "Request fires, response says pending, script loops back, request fires again, response says completed, script moves on."
- Do the CLI demo live. Test results scrolling in a terminal makes the CI/CD connection concrete.
- The cleanup phase is worth emphasizing. Ask: "What happens if you run this 100 times without cleanup?" The answer makes the point.

**Common Questions:**
- "Can I use Newman instead of the Postman CLI?" — Newman still works but is no longer actively developed. The Postman CLI is the recommended replacement.
- "What if my APIs are behind a firewall?" — The CLI runs on your machine, so it can reach internal APIs. Scheduled runs use Postman's cloud and can only reach publicly accessible endpoints.
- "How do I share test data files?" — Check them into your code repository alongside CI/CD pipeline config. The CLI reads them from the filesystem.
- "Can I run just the Tests folder?" — Yes, use `--folder`. But the Tests folder expects Setup to have run first.

**v11 Note:** These materials reflect v11 Postman CLI syntax, Collection Runner behavior, and Package Library capabilities. The hub monitors for v12 changes that may affect CLI commands, script execution lifecycle, data file handling, or scheduled run configuration.

## Pain Points Addressed

**Integration Tests That Span Multiple APIs Are Complex to Set Up and Maintain**
- Problem: Testing a workflow that touches User API, Vehicle API, and Services API requires careful orchestration — creating test data, managing auth tokens, passing IDs between requests, and cleaning up afterward. Most teams skip integration testing because the setup cost is too high.
- Solution: The Setup/Tests/Cleanup folder structure provides a repeatable pattern. Scripts handle data passing between requests. The Collection Runner executes the full suite with one click. The complexity is front-loaded into the collection design, and every subsequent run is automatic.
- Postman Feature: Collections, Test Scripts, Collection Runner, Variables

**No Easy Way to Run the Same Tests with Different Data Sets**
- Problem: Testing a single happy path is not enough. You need to test boundary cases, invalid inputs, multiple user types, and edge conditions. Writing a separate test for each case is tedious and unmaintainable.
- Solution: Data-driven testing with CSV/JSON files lets you define all test cases in a spreadsheet. Each row is a test case, each column is a parameter. The Collection Runner iterates through every row, running the full suite with different data each time. Adding a test case means adding a row.
- Postman Feature: Collection Runner, Variables (data scope)

**Testing Is Disconnected from the CI/CD Pipeline**
- Problem: API tests live in Postman, but the CI/CD pipeline knows nothing about them. Deployments proceed without running API-level integration tests. Teams rely on manual testing or catch issues in production.
- Solution: The Postman CLI runs collections from the command line with standard exit codes. Add one step to your pipeline configuration, and integration tests run automatically on every deployment. Failures gate the deployment — broken APIs do not reach production.
- Postman Feature: Postman CLI, Collection Runner, Scheduled Runs
