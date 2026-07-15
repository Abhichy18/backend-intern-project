# FL-01 Workflow Audit: AI Collaboration Framework

**Name:** Abhishek Choudhary
**Role:** Backend AI Engineer Intern — Flyrank
**Date:** July 15, 2026
**Assignment:** Phase Setup — FL-01

---

## Section 1 — Weekly Task Classification Audit

> **Framework used:** Ethan Mollick's "On-boarding your AI Intern" task-classification model.
> **Categories:** Just Me | Collaborate with AI | Delegate to AI with Review | Fully Automate

| # | Task (Real, Recurring) | Classification | One-Line Rationale |
|---|------------------------|----------------|--------------------|
| 1 | Writing boilerplate API routes (Flask/Express) | **Collaborate with AI** | AI generates standard CRUD scaffolding fast; I adapt it to project-specific auth and middleware logic. |
| 2 | Designing database schema and entity relationships | **Collaborate with AI** | AI suggests table structures and indexes, but only I can weigh real business constraints and future scaling needs. |
| 3 | Writing unit & integration tests for API endpoints | **Delegate to AI with Review** | AI writes comprehensive test cases reliably; I review to ensure they match actual acceptance criteria and edge cases. |
| 4 | Debugging API crash logs and stack traces | **Delegate to AI with Review** | AI pinpoints root cause from trace output within seconds; I validate the fix and guard against regressions. |
| 5 | Writing technical documentation and README files | **Collaborate with AI** | AI handles structure and language polish; I supply project-specific setup steps and architectural decisions. |
| 6 | Attending team standup meetings and sync calls | **Just Me** | Real-time relationship building, accountability, and reading team dynamics cannot be delegated — presence is the output. |
| 7 | Deciding system architecture and tech stack tradeoffs | **Just Me** | Requires accountability for long-term consequences, understanding of team capabilities, and context no AI has access to. |
| 8 | Setting up CI/CD pipelines (GitHub Actions / Docker) | **Collaborate with AI** | AI generates YAML configs and explains each step; I make deployment environment and secrets decisions. |
| 9 | Deploying code to staging/production server | **Fully Automate** | A Git-push-triggered CI/CD pipeline should handle this — no human should be manually SSHing to deploy. |
| 10 | Generating mock/seed database data for testing | **Fully Automate** | Faker.js or Python Faker scripts auto-generate hundreds of relational rows; zero human judgment required here. |
| 11 | Learning new libraries or framework APIs | **Collaborate with AI** | AI provides interactive, personalized explanations and examples; I drive the questions and retain the understanding. |
| 12 | Reviewing other developers' pull requests (PRs) | **Collaborate with AI** | AI scans for security vulnerabilities and syntax bugs; I review overall design intent and code ownership decisions. |
| 13 | Formatting and cleaning raw JSON/CSV data files | **Fully Automate** | Standard regex scripts or one-shot AI pipelines handle this reliably; no repeated human effort needed. |
| 14 | Writing first-draft project proposals or status reports | **Delegate to AI with Review** | AI structures and drafts reports from my bullet-point notes; I review for accuracy and tone before sending. |
| 15 | Researching unfamiliar backend concepts (e.g., Redis, Kafka) | **Collaborate with AI** | AI gives a tailored crash course; I then verify with official docs before applying concepts to production code. |

**Summary: 15 tasks | Just Me: 2 | Collaborate: 6 | Delegate with Review: 3 | Fully Automate: 3**

---

## Section 2 — Claude Project Configuration

### Custom Instructions (set inside Claude → Projects)

```
Who I am:
I am Abhishek Choudhary, a Backend AI Engineer intern at Flyrank. I build
web backends using Python (Flask) and Node.js. I am a learner-practitioner —
comfortable with basic APIs but actively growing in system design, database
optimization, and production-readiness.

Tone preferences:
- Technical but educational: explain the "why" behind every code decision
- Concise and step-by-step: no fluff, no padding
- Treat me as a junior engineer, not a beginner student
- If I ask for code, give working code with inline comments

Current goals (FL-01 to FL-04 internship cycle):
1. Build production-quality API endpoints with proper error handling
2. Master unit testing patterns for backend services
3. Understand when and how to use AI in a real engineering workflow
4. Develop the habit of reviewing AI output critically before shipping
```

> **Screenshot:** [Paste screenshot of configured Claude Project here]
> Steps: claude.ai → Projects → New Project → Paste above instructions → Save

---

## Section 3 — Three Target Tasks for FL-02 through FL-04

These three tasks are drawn from the audit above and will be reused across FL-02, FL-03, and FL-04.

---

### Target Task 1 — Writing Unit Tests for API Endpoints
**Audit Classification:** Delegate to AI with Review
**Reuse in phases:** FL-02 (prompt engineering), FL-03 (evaluation), FL-04 (workflow optimization)

#### "Done Well" Success Definition

| Criterion | Measurable Target |
|-----------|-------------------|
| Coverage | At least **80% line coverage** measured by `pytest-cov` or `jest --coverage` |
| Completeness | Includes tests for **happy path (2xx)**, **client errors (400, 404)**, and **server errors (500)** |
| Speed | Full test suite runs in **under 10 seconds** locally |
| No false passes | Zero tests that pass with a wrong/missing assertion (no bare `assert True`) |
| Readability | Each test name clearly describes what it tests: `test_create_user_returns_201_on_valid_payload` |

---

### Target Task 2 — Debugging API Crash Logs
**Audit Classification:** Delegate to AI with Review
**Reuse in phases:** FL-02 (diagnosis prompting), FL-03 (evaluating AI accuracy), FL-04 (speed benchmarking)

#### "Done Well" Success Definition

| Criterion | Measurable Target |
|-----------|-------------------|
| Diagnosis time | Root cause identified in **under 5 minutes** from pasting the stack trace |
| Fix correctness | The fix resolves the crash; **no existing tests break** after applying it |
| Regression guard | A new test case is added that would have **caught the original bug** |
| Explanation quality | The bug is explainable in **one plain-English sentence** without jargon |
| No blind copy-paste | Every line of AI-suggested fix is **read and understood** before committing |

---

### Target Task 3 — Generating Mock / Seed Database Data
**Audit Classification:** Fully Automate
**Reuse in phases:** FL-02 (scripting via AI), FL-03 (output quality review), FL-04 (integration with test pipeline)

#### "Done Well" Success Definition

| Criterion | Measurable Target |
|-----------|-------------------|
| Volume | Script generates **100+ rows** across at least **2 related tables** (e.g., users → posts) |
| Constraints respected | All foreign key constraints, unique fields (email), and NOT NULL columns are satisfied |
| Speed | Generation + DB insertion completes in **under 10 seconds** |
| Repeatability | Script is idempotent — running it twice does **not crash or duplicate** data |
| Portability | Script works with a single command: `python seed.py` or `node seed.js` |

---

## Appendix — Tool Setup Checklist

| Tool | Status | Evidence |
|------|--------|----------|
| Claude (claude.ai) account | ☐ Created | [Add screenshot] |
| ChatGPT account | ☐ Created | [Add screenshot] |
| Anthropic Academy account | ☐ Enrolled | [Add screenshot] |
| AI Fluency: Framework & Foundations — Module 1 | ☐ Completed | [Add screenshot] |
| Claude Project with custom instructions | ☐ Done | [Add screenshot] |

---

*Submitted for FL-01 evaluation — Flyrank Backend AI Engineer Internship*
