# Postman for Postmanauts (P4P): Program Playbook

> **Purpose:** A plan for running, promoting, and keeping the P4P upskilling program current — so every Postmanaut has just-in-time access to product fluency when they need it.
>
> **Owner:** Marcus Kidan | **Last Updated:** April 10, 2026

---

## What P4P Is (and Isn't)

The Bootcamp gives new hires a foundation. P4P is the ongoing sharpening tool for *everyone*. It's one-on-one or small-group sessions that employees book when they need to get fluent on something specific — a new feature, a customer conversation, a product area they've never explored.

P4P is not a recurring class with a fixed curriculum. It's a menu of session types that flex based on what Postman is shipping and what employees are asking for. The catalog evolves as the product does.

---

## Current Session Catalog

Based on the existing booking page:

| Session | Format | Who It's For | Duration |
|---------|--------|-------------|----------|
| **Intro to Postman: Exploring the Tool** | Guided walkthrough | Anyone who wants a tour of core workflows and the interface | ~60 min |
| **Why Do Customers Use Postman? (The Four Pain Points)** | Deep dive discussion | GTM, customer-facing roles wanting to connect product to customer value | ~60 min |
| **What's New In V12** | Briefing + demo | Anyone wanting to understand the V12 platform shift (AI, Git, Catalog, etc.) | ~45-60 min |
| **30 Minute Pit Stop** | Quick Q&A | Anyone with a few targeted questions or needing help translating a concept | 30 min |
| **Specific Features** | Tailored walkthrough | Anyone wanting depth on a feature relevant to their role — their choice | ~45 min |
| **Deeper Dive: Advanced Features** | Hands-on exploration | Anyone ready to explore complex features and connect them to strategic outcomes | ~60 min |
| **Understanding APIs** | Conversational | Anyone building foundational API literacy — what they are, how they work, why they matter | ~45-60 min |

### Recommended Catalog Additions

Based on what's been shipping through #product-updates and the velocity of V12 changes, consider adding:

**"MCP & AI Agents: What They Mean for Us"** — MCP is one of the fastest-moving areas. There have been 6+ MCP-related updates in the last 60 days alone (MCP Catalog UX improvements, OAuth security, Private API Network search in MCP, external MCP in Flows, CLI generator for AI agents). This is becoming core product vocabulary that GTM and Engineering both need. This session would cover what MCP is, how Postman uses it, and why customers care.

**"Postman CLI & Developer Workflow"** — The CLI has expanded significantly (Flows CLI, performance testing, mock servers, SDK generation, multi-protocol support). Employees in Solutions, Support, and Engineering benefit from understanding how Postman fits into CI/CD and the developer inner loop.

**"Security & Governance in Postman"** — With Secrets Resolution, Shared Vault, Account Discovery & Control, and EU data residency, security has become a major product pillar. Customer-facing teams especially need fluency here.

---

## The Announcement Strategy

Demand is spiky around releases — so the strategy is to **ride the waves proactively** rather than waiting for employees to realize they need a session.

### Announcement Cadence

| Timing | What | Where | Who |
|--------|------|-------|-----|
| **Weekly** (Fridays) | "This Week in Postman" digest | Company-wide Slack channel (#general or a dedicated #postman-academy channel) | All employees |
| **On major releases** | Targeted session promo | Relevant team channels + all-company | All employees, with callouts for specific roles |
| **Monthly** | "P4P Menu Refresh" | All-company channel + email | All employees |
| **Post-bootcamp** | Personal follow-up | DM or bootcamp follow-up channel | New hire cohorts |

### "This Week in Postman" — The Weekly Digest

This is the anchor. Every Friday, a short Slack post summarizing what shipped that week and connecting it to why employees should care. The format:

```
🚀 This Week in Postman (Apr 7-11, 2026)

WHAT SHIPPED
• CLI Generator — Generate a CLI for your APIs in one click, 
  usable by AI agents and humans. [Demo →]
• Publisher Self-Serve Verification — Simplified to just domain 
  ownership verification.
• Secrets Resolution & Shared Vault — Secrets are now first-class, 
  resolved just-in-time, never stored in plain text.

WHY YOU SHOULD CARE
→ If you talk to customers about AI: The CLI Generator makes any 
  API "AI-ready" in one click. That's a powerful story.
→ If you manage team credentials: Shared Vault changes how your 
  team handles secrets. Book a P4P session to see it in action.

📅 BOOK A SESSION
[30 Minute Pit Stop] — Quick questions about any of the above
[What's New in V12] — Full V12 briefing with live demos
[Specific Features] — Deep dive on any feature listed above
```

This does three things: keeps everyone informed, creates natural demand spikes for P4P, and gives Marcus a structured rhythm instead of reacting to ad-hoc requests.

### Major Release Announcements

When something big ships (like Secrets Resolution, CLI Generator, or a major Agent Mode update), send a standalone announcement within 24-48 hours:

```
🔔 New in Postman: [Feature Name]

[2-3 sentence plain-English summary of what it does and why it matters]

This affects: [roles — e.g., "Everyone in Solutions and Support 
who handles Enterprise customer conversations about security"]

🎯 Want to get fluent fast? 
Book a P4P session: [link]
I'll walk you through it hands-on in 30-45 minutes.
```

### Monthly Menu Refresh

First Monday of each month, post the full updated P4P catalog with any new sessions added based on recent product changes. Frame it as "here's what's available, here's what's new, here's what I'd recommend based on what shipped last month."

---

## Keeping Marcus Up to Date: The Weekly Product Digest

Instead of Marcus having to monitor #product-updates constantly, Cowork produces a **weekly digest every Monday morning** that synthesizes the past week's updates into actionable intelligence for the P4P program.

### What the Digest Includes

1. **Product changes this week** — Summarized from #product-updates with plain-English descriptions
2. **P4P session impact** — Which existing sessions are affected (e.g., "What's New in V12 should now cover CLI Generator")
3. **Announcement draft** — A ready-to-post "This Week in Postman" Slack message for Friday
4. **Bootcamp module flags** — Cross-reference with the Bootcamp Module Registry (ties into the bootcamp monitoring system)
5. **Session demand prediction** — Based on the type of updates, which sessions are likely to see increased bookings

### Example Digest Output

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
P4P WEEKLY DIGEST — Apr 7-11, 2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📦 PRODUCT CHANGES (3 this week)

1. CLI Generator (Stage 7, Team + Enterprise)
   Generate a CLI for any API in one click. Supports AI agents, 
   multiple auth methods, Go SDK under the hood.
   → SESSION IMPACT: Update "What's New in V12" with demo. 
     Consider adding to "Deeper Dive: Advanced Features."
   → ANNOUNCEMENT: High priority. AI-readiness story is 
     compelling for GTM.

2. Publisher Self-Serve Verification (Stage 7, All plans)
   Simplified to just domain ownership verification.
   → SESSION IMPACT: Minor. Mention in "Intro to Postman" 
     if discussing API Network publishing.
   → ANNOUNCEMENT: Low priority for company-wide. Relevant 
     for DevRel/Partner teams.

3. Secrets Resolution & Shared Vault (Stage 2, All plans)
   Secrets as first-class concept. Just-in-time resolution, 
   never exposed in plain text. Shared Vault for team collab.
   → SESSION IMPACT: Major. Update "What's New in V12" and 
     "Specific Features" options. Consider standalone session.
   → ANNOUNCEMENT: High priority. Security is a top customer 
     concern. Enterprise teams especially.

📊 DEMAND PREDICTION
Expect increased bookings for:
  • "What's New in V12" (CLI Generator buzz)
  • "30 Minute Pit Stop" (Secrets questions from Engineering)
  • "Specific Features" (teams wanting CLI Generator deep dive)

📝 FRIDAY ANNOUNCEMENT DRAFT
[Ready-to-post Slack message — see below]

🏫 BOOTCAMP FLAGS
  • M05 (Security & Auth): Shared Vault changes auth landscape
  • M08 (AI & Agents): CLI Generator is a new AI capability
  • M09 (Postman Platform): Both updates expand product surface
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## How It All Connects

```
#product-updates (Slack)
        ↓
  Cowork Weekly Digest (Monday AM)
  - Reads #product-updates from past 7 days
  - Categorizes by P4P session impact
  - Drafts Friday announcement
  - Flags bootcamp modules
        ↓
  Marcus Reviews (Monday)
  - Adjusts digest if needed
  - Plans any special sessions
  - Decides if catalog needs new options
        ↓
  "This Week in Postman" (Friday)
  - Posted to all-company Slack
  - Drives awareness and P4P bookings
        ↓
  P4P Sessions (ongoing)
  - Marcus delivers sessions with current content
  - Session content stays fresh because it's fed 
    by the weekly digest cycle
        ↓
  Monthly Catalog Refresh (1st Monday)
  - Add/retire session types based on product trajectory
  - Post updated menu company-wide
```

---

## Scaling P4P

If demand grows beyond what one person can handle, here are levers:

**Recorded sessions.** For high-demand topics (like "What's New in V12"), record a session and make it available on-demand. Frees Marcus for live Q&A and deeper dives.

**Session champions.** Train 2-3 product-savvy employees in other departments to deliver the "Understanding APIs" and "Intro to Postman" sessions. Marcus focuses on the sessions that require deep product knowledge.

**Group sessions.** When 3+ people book the same session type in a week, offer a small-group format instead of 1:1. More efficient, and the group discussion often adds value.

**Async resources.** The API Fundamentals Field Guide already exists as a reference. Build similar standalone resources for the most-requested topics, so P4P sessions can focus on Q&A and hands-on rather than lecture.

---

## Metrics to Track

To understand if P4P is working and where to invest:

| Metric | Why It Matters | How to Track |
|--------|---------------|-------------|
| Sessions booked per week | Overall demand signal | Booking system |
| Sessions by type | Which topics are hottest | Booking system |
| Bookings within 48hrs of announcement | Are announcements driving demand? | Compare booking timestamps to announcement dates |
| Post-bootcamp booking rate | Are new hires following up? | Cross-reference bootcamp cohort with P4P bookings |
| Repeat bookers | Who's becoming a power user of P4P? | Booking system |
| NPS or satisfaction rating | Session quality | Post-session survey |

---

## Source Material

| Resource | Purpose |
|----------|---------|
| #product-updates (Slack) | Primary source for product changes |
| Bootcamp Modular System Playbook | Cross-references bootcamp module impacts |
| API Fundamentals Field Guide | Reference material for "Understanding APIs" sessions |
| Postman for Postmanauts booking page | Current session catalog |
| Postman Learning Center | Supplementary learning resources to share with attendees |
