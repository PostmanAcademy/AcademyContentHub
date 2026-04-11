---
id: M03
title: "How APIs Work"
program: bootcamp
owner: Marcus Kidan
change_sensitivity: low
status: current
last_updated: 2026-04-10
last_audited: 2026-04-10

postman_features: []

update_triggers:
  - "New HTTP methods or API patterns become mainstream"
---

## Overview
This module teaches the mechanics of how APIs work at a practical level. We introduce the client-server model, CRUD operations, HTTP methods, and the anatomy of requests and responses. By the end, participants understand that they're already using these concepts—we're just naming them.

## Learning Objectives
- Describe the client-server request/response cycle
- Map CRUD operations to HTTP methods
- Read a URL and identify its components (server, endpoint, query parameters)

## Key Elements

### The Client-Server Model
The internet is built on a simple conversation: **You (the client) ask for something. A building (the server) answers.**

The client sends a **request**. The server sends back a **response**. That's it. Everything else is details.

### CRUD: The Four Things You Can Do With Data
Every interaction with an API comes down to four operations:

- **Create** – Add new data (make a reservation)
- **Read** – Get existing data (check the weather)
- **Update** – Change existing data (edit your profile)
- **Delete** – Remove data (cancel a reservation)

These are *not* technical concepts. They're human operations. The technical details (which HTTP method to use) come next.

### HTTP Methods: The Language of CRUD

Each CRUD operation maps to an HTTP method:

| Operation | HTTP Method | What You're Saying |
|-----------|-------------|-------------------|
| Create    | POST        | "Add something new" |
| Read      | GET         | "Show me something" |
| Update    | PUT/PATCH   | "Change something" |
| Delete    | DELETE      | "Remove something" |

These are standardized so that every API works the same way (in theory). GET always means "read," POST always means "create."

### The Receptionist Metaphor
Think of the server as a building with a receptionist:

- You walk up (client) and hand them a form (request)
- You tell them what you want (HTTP method: GET, POST, etc.)
- They understand your request because the form is in a standard format
- They go find what you asked for and hand you back a response
- You check the response to see if they found it, if there was an error, or if they need more information

The receptionist doesn't know your name or who you are unless you prove it. If you don't have proper credentials, they send you away.

### Request Anatomy
Every API request has four parts:

**1. The Method** (GET, POST, PUT, DELETE)  
What action you're taking.

**2. The URL** (endpoint)  
Which building and which desk you're going to.

**3. The Headers** (envelope)  
Metadata about your request: "I speak English," "Here's my authentication token," "I want JSON back, not XML."

**4. The Body** (form)  
The actual data you're sending, if any. A GET request usually has no body. A POST request does—that's the new data you're creating.

### Response Anatomy
Every API response has the same structure:

**1. Status Code** (200, 404, 401, 500, etc.)  
A three-digit number telling you what happened.

**2. Headers**  
Metadata about the response: "This data expires in 5 minutes," "This is in JSON format."

**3. Body**  
The actual data you asked for, if the request succeeded.

### Status Codes: The Building's Answer

- **200 (OK)** – "You asked nicely and I found what you wanted. Here it is."
- **201 (Created)** – "You submitted a form and I created something new."
- **400 (Bad Request)** – "Your form was filled out wrong. Try again."
- **401 (Unauthorized)** – "You don't have a badge. I need to verify who you are."
- **403 (Forbidden)** – "You have a badge, but you're not allowed to go to this desk."
- **404 (Not Found)** – "That room doesn't exist in this building."
- **500 (Internal Server Error)** – "The building caught fire. Try again later."

### URL Anatomy: Reading an Address
Take this URL: `https://www.youtube.com/results?search_query=postman`

- **`https://`** – The protocol (secure web)
- **`www.youtube.com`** – The building (server)
- **`/results`** – The specific desk (endpoint)
- **`?search_query=postman`** – A sticky note with instructions (query parameter)

The query parameter is how you pass extra information without changing the URL structure. You're asking "give me results, but filter them to only show stuff about Postman."

### "You're Already Using This"
The revelation: Every time a user opens an app, refreshes a browser, submits a form, or scrolls through social media, they're creating HTTP requests. They've been clients and servers all along—we're just making it explicit.

## Activities

### "What HTTP Method is Liking a Post?"
Pose this to the class: "When you like a post on social media, what's happening? What HTTP method is that?"

The answer is: **POST**—you're creating new data (the "like" relationship between you and that post).

But then ask: **"What if you unlike it?"** Now it's **DELETE**—you're removing that relationship.

And: **"What if you edit your bio?"** That's **PUT**—you're updating existing data about you.

The beauty of this activity is that there are multiple right answers depending on design choice. Liking could theoretically be a POST (create a "like" record) or a PUT (update a "likes" count on the post). Both work. This reinforces that HTTP methods are design choices, not laws.

## Postman Features in This Module
None—this is a conceptual foundation module.

## Facilitator Notes
**Timing:** 25–30 minutes.

**Tips:**
- Use hand gestures and physical metaphors: "You're here (client), the server is over there, you throw the request across the room, they throw the response back."
- Status codes are memorable when framed as building scenarios. 200 = "All good," 404 = "That place doesn't exist," 500 = "We broke something."
- The URL anatomy activity can feel too technical; slow down and show real examples from the browser address bar.

**Common Misconceptions:**
- "POST always creates, GET always reads" – True as a general rule, but there are exceptions (some APIs misuse POST for filtering). Stress that **conventions** exist for good reasons, but code doesn't enforce them.
- "Status codes are just numbers" – No, they're standardized communication. A 404 is not an error in the server's eyes; it's the correct answer to "does this thing exist?" (No.)

## Pain Points Addressed
**Testing** – "How do you know the receptionist is giving you the right response?" This is where Postman enters in future modules. Right now, you might test an API by hand (typing in a browser), but that's limited. Postman lets you craft precise requests, see exact responses, and repeat tests reliably.
