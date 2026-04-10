---
id: M08
title: "AI & Agents"
program: bootcamp
owner: Marcus Kidan
change_sensitivity: high
status: current
last_updated: 2026-04-10
last_audited: 2026-04-10

postman_features:
  - Agent mode
  - AI test generation
  - AI debugging
  - AI documentation generation
  - MCP server support
  - Flows AI
  - CLI Generator

update_triggers:
  - "Any AI or agent feature release"
  - "MCP protocol changes"
  - "Agent mode capability additions"
  - "AI test generation updates"
  - "New AI-powered features"
---

## Overview

AI is reshaping how engineers work. But not all AI is created equal. In this module, we explore the difference between AI that generates text and AI that *acts*—agentic AI that can use tools, make decisions, and solve complex problems. You'll learn about Large Language Models (LLMs), the Model Context Protocol (MCP), and how Postman's AI capabilities turn repetitive API tasks into automated workflows. By the end, you'll understand how to harness Postman's AI agents to accelerate development, testing, debugging, and documentation.

## Learning Objectives

- Explain what makes AI "agentic" vs. purely generative
- Understand the Model Context Protocol (MCP) and why it matters for API tooling
- Identify Postman's AI-powered capabilities and when to use each one
- Apply AI features to real API development workflows

## Key Elements

### What Are LLMs?

Large Language Models (LLMs) like GPT are trained on massive amounts of text. They're pattern recognition engines—they predict the next most likely word, billions of times.

**Key trait: Probabilistic, not deterministic.**
- If you ask "What is 2+2?", an LLM calculates based on patterns in training data, not math.
- This works great for creative tasks (writing, brainstorming). It's risky for precise tasks (calculations, code generation without validation).

**Practical truth**: LLMs are powerful at understanding intent and generating reasonable starting points. They're not reliable oracles.

### What Makes AI "Agentic"?

**Generative AI**: Takes input, generates output. Done.
- Example: "Write a description of REST APIs"
- LLM produces text; that's it.

**Agentic AI**: Takes input, *uses tools* to gather information, take actions, and refine answers.
- Example: "Generate tests for my API endpoint"
- Agent reads the endpoint code, understands the contract, generates tests, *validates* them by running them, and refines if they fail

**Agents have:**
1. **Tool access**: Can read code, run tests, call APIs, access documentation
2. **Reasoning loop**: Observe → Decide → Act → Observe → Refine
3. **Goal orientation**: Keeps working until the goal is achieved

**Why it matters**: An agent can fix its own mistakes. A generative model can't.

### Model Context Protocol (MCP)

Imagine the city's various departments (planning, utilities, permits, construction) need to coordinate. How do they share information?

**Without MCP**: Each department has its own filing system. To get information, you visit them in person or call. Chaos.

**With MCP**: An underground highway system connects all departments. Requests and responses flow through a standardized protocol. Any person can submit a request to any department without learning their specific systems.

**MCP is that highway for AI agents.**

MCP is an open protocol that defines how AI agents can:
- **Request tools**: "I need to run tests" → Agent calls `run_tests` tool
- **Access data sources**: "I need the API schema" → Agent calls `get_schema` tool
- **Understand resources**: "What tools are available?" → MCP server advertises capabilities

**Why Postman cares**: With MCP support, Postman becomes an accessible source of truth for AI agents. An agent doesn't need to know Postman's UI; it calls MCP tools to read collections, generate tests, etc.

**Real example**: An AI agent in your IDE could say "Add a test for this API endpoint" and use MCP to:
1. Query Postman for the collection
2. Understand the endpoint schema
3. Generate a test
4. Submit it back to Postman
5. Validate it runs

All without leaving your IDE.

### Postman's AI Capabilities

**1. Agent Mode**
- Reads your code and API schemas
- Understands intent from natural language
- Generates tests, request stubs, mock data, documentation
- Validates and refines output

**Example**: "Write tests for error handling in `/users` endpoint"
- Agent reads your endpoint code
- Generates tests for 400, 401, 404, 500 cases
- Runs tests to validate they work
- Refines if needed

**2. AI Test Generation**
- Describe a scenario; AI generates test code
- Understands common patterns (auth, pagination, validation)
- Produces working tests you can run immediately

**3. AI Debugging**
- Paste a failed test or API error
- AI analyzes the issue and suggests fixes
- Learns from context (endpoint code, test code, error messages)

**4. AI Documentation Generation**
- Reads collections and generates human-readable docs
- Understands API patterns and creates cohesive narratives
- Outputs to multiple formats (Markdown, HTML, API portals)

**5. Flows AI**
- Orchestrate multi-step API workflows visually
- AI helps design flows based on requirements
- Reduces manual flow building

**6. CLI Generator**
- Describe a workflow in plain language
- AI generates Postman CLI (Newman) commands
- Saves time learning CLI syntax

**7. MCP Server Support**
- Postman exposes its capabilities via MCP
- External AI agents (in IDEs, Slack, custom tools) can query Postman
- Enables integration without leaving your current tools

## Activities

### Agent Mode Demo & Discussion

**Scenario**: Your team needs to add tests for a new payment API endpoint. The endpoint handles:
- Successful payments
- Invalid card numbers
- Insufficient funds
- Authentication failures
- Rate limiting

**Activity**:
1. **Demo** (facilitator): Show Agent Mode reading the endpoint schema and generating tests for 3-4 cases
2. **Class Discussion**:
   - What did the agent get right?
   - What would you refine?
   - How much time did this save vs. writing tests manually?
   - When would you *not* trust AI-generated tests?

3. **Hands-on** (if tools available): Have students describe an API scenario; use Agent Mode to generate tests; review the output together

*Facilitation tip: Emphasize that AI is a force multiplier, not a replacement. The agent creates a starting point; engineers review, validate, and refine. This builds confidence that AI is a tool, not a threat.*

## Postman Features in This Module

- **Agent Mode**: Natural language → Collections, tests, documentation, stubs, mocks
- **AI Test Generation**: Describe a scenario → Generate test code
- **AI Debugging**: Paste error → Get diagnosis and fix suggestions
- **AI Documentation Generation**: Collections → Readable API docs in multiple formats
- **Flows AI**: Describe a workflow → Visual flow diagram
- **CLI Generator**: Describe a command → Generate Newman CLI code
- **MCP Server Support**: External AI agents can query Postman via a standardized protocol

## Facilitator Notes

- **Start with philosophy**: Not all AI is agentic. Make sure learners understand the difference before diving into features.
- **Demystify LLMs**: They're pattern recognition, not magic. This builds realistic expectations.
- **Show mistakes**: AI generates reasonable-but-wrong code sometimes. Demonstrate error cases so learners know they must validate output.
- **Emphasize the workflow**: AI accelerates repetitive tasks (test generation, docs), but humans own decisions (what to test, documentation tone).
- **Connect to DX**: Tie AI features back to Module 7 concepts. "Agent Mode reduces context switching—you describe what you want in English, not syntax."
- **MCP is abstract**: Use the highway/department metaphor to make it concrete. Optional deeper dive for architects.
- **Handle skepticism**: Some engineers are skeptical of AI. Validate the concern, but show concrete examples of time savings and quality.

## Pain Points Addressed

**Test Automation Burden**: Writing and maintaining tests is tedious and repetitive. AI test generation creates starting points; engineers validate and extend.

**Documentation Debt**: Docs are written once and drift. AI can regenerate docs from collections, keeping them fresh. Enables docs-as-code.

**Debugging Friction**: Errors are cryptic. AI can analyze stack traces and API errors, suggesting fixes faster than manual investigation.

**Onboarding Overhead**: New engineers spend days learning API contracts and writing boilerplate tests. Agent Mode accelerates onboarding—describe what you want, AI generates a starting point.

**Workflow Complexity**: Multi-step API workflows are error-prone to build manually. Flows AI and Agent Mode help design and validate complex workflows.

**Tool Fragmentation**: Engineers work in multiple tools (IDE, Postman, monitoring). MCP allows external tools (IDE extensions, Slack bots) to query Postman directly, reducing context switching.

---

## Appendix: When to Use Each AI Feature

| Task | Feature | Why |
|------|---------|-----|
| Write 10 test cases for an endpoint | AI Test Generation | Fast, covers common patterns |
| Debug a failing test | AI Debugging | Analyzes error context, suggests fixes |
| Generate API docs for portal | AI Documentation Generation | Produces readable, cohesive narrative |
| Design a multi-step payment flow | Flows AI | Visualizes logic without manual drawing |
| Generate Newman CLI command for CI/CD | CLI Generator | Saves learning syntax |
| Automate a complex workflow end-to-end | Agent Mode | Can reason across multiple steps, refine iteratively |
| Integrate Postman data into external AI tool | MCP Server | Standardized access without learning Postman internals |
