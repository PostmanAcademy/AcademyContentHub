---
id: M02
title: "The Internet & APIs"
program: bootcamp
owner: Marcus Kidan
change_sensitivity: low
status: current
last_updated: 2026-04-10
last_audited: 2026-04-10

postman_features: []

update_triggers:
  - "Fundamental shift in Postman's API narrative"
---

## Overview
This module introduces the core concept of APIs by building from what the internet is, to what APIs are, using concrete metaphors. We establish both technical and human definitions of APIs and show how they power the applications participants use every day.

## Learning Objectives
- Explain what an API is in both technical and human terms
- Use the City Metaphor to reason about internet architecture
- Identify the APIs behind familiar applications

## Key Elements

### What is the Internet?
The internet is a network of computers talking to each other. But for learners new to APIs, that's abstract. The **City Metaphor** makes it concrete: imagine a city where different buildings provide services—a bank handles money, a hospital handles health, a library handles information. These buildings have doorways and rules about how to interact with them. That's what an API is.

### Two Definitions of an API

**Technical Definition:**  
An API is a defined contract between two pieces of software. It specifies what requests you can make, what format those requests take, and what responses you'll get back.

**Human Definition:**  
The apps your apps use. When you scroll through Netflix, Netflix is using APIs from payment processors, recommendation engines, streaming servers, authentication services, and more. Netflix is the customer walking into different buildings in the city.

### The Bezos Mandate Story
Amazon's famous 2002 edict: all teams must expose their functionality through APIs, or be fired. This forced Amazon to think of itself not as a monolith, but as a city of specialized services. Netflix followed the same pattern—they couldn't stream movies without APIs for billing, user auth, catalog search, recommendations, and infrastructure.

### Netflix as a City: The Five Buildings
When you use Netflix, it's actually talking to five distinct "buildings" (API services):

1. **Billing (Stripe)** – Charges your card, manages subscriptions
2. **Authentication (Auth0 or similar)** – Verifies you are who you say you are
3. **Catalog** – Searches and returns show metadata
4. **Streaming** – Delivers video frames
5. **Recommendations** – Suggests what you should watch next

None of these are built by Netflix. Netflix orchestrates them. That's modern software architecture.

### Building Types in the City
Different buildings specialize in different services:

- **Bank** (Stripe, Square) – Payment processing
- **Hospital** (EHR systems, health APIs) – Medical records and health data
- **Library** (Wikipedia API, Elastic Search) – Information retrieval and search
- **Post Office** (email APIs) – Sending messages
- **City Hall** (government data APIs) – Public records and permits
- **Utility Company** (weather APIs, mapping) – Environmental and location data

Each building has a specific expertise and interface. Knowing what building exists and how to ask for what you need is the foundation of modern development.

## Activities

### "What APIs (Buildings) Would You Need for a Weather App?"
Present a simple scenario: "You're building a weather app. Walk me through the city. What buildings would you need to visit, and what would you ask them for?"

Guide participants to think like city planners:
- **Weather Data Building** – "Give me the forecast for this location"
- **Maps Building** – "Find the coordinates of this address"
- **Notifications Building** – "Send the user an alert when rain is coming"
- **User Database Building** – "Store which cities this user is following"

This reveals that even simple apps are built on networks of specialized services. There's no such thing as a standalone app anymore.

## Postman Features in This Module
None—this is a conceptual foundation module.

## Facilitator Notes
**Timing:** 20–25 minutes.

**Tips:**
- The City Metaphor is your anchor. Every time something feels abstract, walk back to "which building are we talking to?"
- The Netflix example is powerful because everyone knows Netflix. Use it to make the abstract concrete.
- If someone says "I don't use APIs," push back gently: "Every time you log into an app with your Google account, you're using an API. Every time an app sends you a notification, it's using an API."

**Common Questions:**
- "Are all APIs on the internet?" – No, but we're focusing on internet-based (HTTP) APIs in this bootcamp. Internal company APIs follow the same logic.
- "Who builds these APIs?" – Usually the company that owns the service. But increasingly, third-party companies expose their services as APIs for others to build on (Stripe for payments, Twilio for SMS, etc.).

## Pain Points Addressed
**Discovery** – "How do you even find the right building in a city of millions?" This is a real problem in API development. There are thousands of public APIs, and finding the right one for your use case is hard. Later modules will address how to document and search for APIs.
