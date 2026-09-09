# Backlog Refinement — Working Session

## Purpose

Create enough shared understanding for upcoming Product Backlog Items so the team can inspect, discuss and forecast them responsibly.

## Participants

- Product Owner
- Scrum Master
- Developers
- UX representative when needed
- QA representative when needed

## Refinement agenda

### 1. Reconfirm Product Goal
Keep the conversation connected to customer value.

### 2. Review ordering
The Product Owner explains the current ordering and value assumptions.

### 3. Inspect upcoming stories
For each item:

- Who needs this?
- What problem does it solve?
- What does success look like?
- What are the acceptance criteria?
- What dependencies exist?
- Is the story small enough?
- What questions remain?

### 4. Identify risks and dependencies

Capture unresolved items rather than allowing them to disappear into meeting notes.

### 5. Inspect readiness

Use the Definition of Ready as a conversation aid, not an approval bureaucracy.

## Example refinement outcome

### US-005 — Filter results by category

**Value:** Customers can narrow knowledge results and find relevant information faster.

**Acceptance criteria:**

- Given search results exist, when the customer selects a category, then only matching results are displayed.
- Given no articles match the selected category, then the user sees a clear empty-state message.
- The selected category remains visible while browsing the results.
- The filter works with existing keyword search.

**Dependency:** Article taxonomy must be available from the knowledge service.

**Open question:** Should categories be single-select or multi-select?

**Scrum Master action:** Make the dependency and decision visible; facilitate the conversation without deciding the product behavior.

## Practical observation

A good refinement session reduces uncertainty. It should not become a ceremony where the Scrum Master reads every backlog item aloud.
