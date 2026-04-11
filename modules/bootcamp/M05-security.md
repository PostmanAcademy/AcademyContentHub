---
id: M05
title: "Security & Authentication"
program: bootcamp
owner: Marcus Kidan
change_sensitivity: medium
status: current
last_updated: 2026-04-10
last_audited: 2026-04-10

postman_features:
  - Auth tab
  - API key management
  - OAuth 2.0 flows
  - Vault integration

update_triggers:
  - "New auth types added"
  - "Auth UI changes"
  - "Security governance features added"
  - "Vault or secrets management updates"
---

## Overview

APIs are the digital doors to your applications and data. Without proper security, anyone could walk in. In this module, we explore authentication and authorization—the gatekeeping mechanisms that protect APIs at scale. You'll learn how Postman helps teams manage API security, from simple API keys to complex OAuth flows, and how to prevent common security pitfalls.

## Learning Objectives

- Distinguish between authentication and authorization
- Explain common authentication mechanisms (API keys, OAuth 2.0, JWT)
- Identify how Postman handles API security in practice
- Apply security concepts to real-world API governance scenarios

## Key Elements

### Authentication vs. Authorization

Think of your office building. **Authentication** is proving you belong there—your access badge gets you in. **Authorization** is what you're allowed to do once inside—your clearance level determines which floors and rooms you can access.

- **Authentication** answers: "Are you who you claim to be?"
- **Authorization** answers: "What are you allowed to do?"

### Common Authentication Mechanisms

**API Keys**
- Simple bearer token you send with requests
- Metaphor: Your building access badge
- Trade-off: Easy to implement, less flexible
- Postman feature: Stores keys securely in the Auth tab

**OAuth 2.0**
- Delegation protocol: users grant apps permission without sharing passwords
- Metaphor: A valet parking ticket—you give the valet a time-limited, scope-limited credential
- Trade-off: More complex setup, but industry standard for third-party integrations
- Postman feature: Native OAuth 2.0 flow support with automatic token refresh

**JWT (JSON Web Tokens)**
- Self-contained token with claims (user, role, expiration)
- Metaphor: A time-stamped visitor pass—contains info about who you are and how long you can stay
- Trade-off: Stateless, good for microservices, but harder to revoke mid-session
- Postman feature: Decode and validate JWTs in tests

### Other Security Concepts

**Rate Limiting**
- Controls how many requests an API consumer can make
- Metaphor: Maximum occupancy rules—prevents overcrowding
- HTTP status: 429 (Too Many Requests)

**CORS (Cross-Origin Resource Sharing)**
- Restricts which websites can call your API
- Metaphor: Only visitors from approved neighborhoods allowed
- Protects against browser-based attacks

**Common Status Codes**
- **401 Unauthorized**: You forgot your authentication (badge)—prove who you are
- **403 Forbidden**: You're authenticated but don't have permission—clearance denied
- **429 Too Many Requests**: Exceeded rate limit

## Activities

### Discussion Prompt: Security at Scale

Imagine your organization has 50 API teams across three regions. Each team manages its own authentication.

- How does an organization ensure every API has proper security?
- What happens when different teams use different auth mechanisms?
- How would Postman's vault help standardize and audit credentials across teams?

*Facilitation tip: Use this to surface governance pain points and show how Postman's centralized auth management helps.*

## Postman Features in This Module

- **Auth Tab**: Configure API keys, OAuth, basic auth, bearer tokens, and custom auth methods
- **API Key Management**: Securely store and inject keys without exposing them in collections
- **OAuth 2.0 Flows**: Automated token requests and refresh cycles
- **Vault Integration**: Organization-wide secret management and audit trails

## Facilitator Notes

- Emphasize the "badge vs. clearance" metaphor early—it's the clearest way to distinguish auth from authz
- In live demos, show the Auth tab side-by-side with the actual request to illustrate how Postman injects credentials
- Avoid deep cryptographic dives; focus on "what it does" and "when to use it"
- Highlight the risk of embedding secrets in collections—this is a common mistake trainers should catch

## Pain Points Addressed

**Security Governance at Scale**: Organizations struggle to ensure every API is properly secured and that credentials don't leak. Postman's Vault and Auth tab centralize credential management, making audits and rotation easier.

**Developer Confusion**: Developers often conflate "I know you" (authentication) with "I trust you" (authorization). The metaphors in this module make the distinction concrete.

**Credential Sprawl**: Teams accumulate API keys in code, configs, and emails. Postman's Auth features and Vault prevent this through centralized, encrypted storage.
