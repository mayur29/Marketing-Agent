# Run Workflow

This document shows how to run the V1 DISH hospitality marketing agent system end to end using the sample campaign in `knowledge/sample-campaign.md`.

The goal is not to automate every action yet.
The goal is to make the workflow explicit, testable, and easy to improve.

## Workflow Goal

Take a single business goal and move it through the V1 agent stack:

1. CMO Agent sets priority and direction
2. Market Research Agent sharpens context
3. Messaging and Positioning Agent defines the message
4. Campaign Strategist Agent creates the campaign plan
5. Copywriter Agent drafts initial assets
6. Analytics and Optimization Agent defines how we learn and improve

The default example in this file is a German campaign for `DISH Order`, so all handoffs should preserve market and language context.

## Input Files

Use these files as the starting context:

- `knowledge/sample-campaign.md`
- `knowledge/brand.md`
- `knowledge/offers.md`
- `knowledge/icps.md`
- `knowledge/competitors.md`
- `templates/agent-handoff.md`
- `templates/campaign-brief.md`

## Step 1: CMO Agent

### Reads

- `knowledge/sample-campaign.md`
- business constraints and priorities
- prior campaign context if available

### Objective

Turn the raw campaign idea into a clear strategic priority and assign the next agents.

### Expected Output

- strategic priority
- recommended audience
- recommended offer framing
- campaign objective
- agent assignments
- open risks or assumptions

### Example CMO Output

```md
1. Strategic Priority
Generate qualified demo requests from German restaurant operators for DISH Order.

2. Why This Matters Now
High aggregator commissions create a clear financial pain point, and DISH Order offers a direct-order alternative.

3. Recommended Campaign Direction
Lead with direct ordering economics, ownership of the guest relationship, and the benefit of avoiding per-order commissions.

4. Agent Assignments
- Market Research Agent: validate operator pains, urgency triggers, and local competitor framing in Germany
- Messaging Agent: turn the offer into a sharper proof-backed value proposition for restaurant operators
- Campaign Strategist Agent: prepare a focused campaign plan after messaging is approved

5. Risks and Assumptions
- price sensitivity and setup complexity may create hesitation
- messaging must avoid implying instant revenue guarantees

6. Escalations
- human review needed before any hard savings or revenue claims are used publicly

7. Next Handoff
Send a research brief to the Market Research Agent
```

### Example Handoff to Market Research

Use `templates/agent-handoff.md` and populate it like this:

```md
## From Agent
- CMO Agent

## To Agent
- Market Research Agent

## Task
- Validate the strongest audience pains, urgency triggers, and competitor framing for this campaign

## Business Goal
- Generate qualified demo requests

## Target Audience
- independent restaurant owners in Germany
- small hospitality groups with delivery or pickup demand

## Offer or Product
- DISH Order

## Campaign Context
- Campaign name: DISH Order DE Launch Push
- Funnel stage: consideration to conversion
- Channels: landing page, email, Meta ads, sales follow-up
- Market or country: Germany
- Primary language: German
- Tone register: DE Sie

## Approved Context
- Main promise: increase direct online orders with an own-branded ordering experience that avoids per-order commission fees

## Constraints
- no unsupported savings or revenue claims
- no autonomous publishing

## Required Output
- a research memo that identifies operator pains, objections, competitor patterns, and implications for positioning in Germany

## Known Risks or Open Questions
- whether operators care more about commission savings, brand control, or operational simplicity
- whether setup friction is a larger objection than switching cost

## Source References
- knowledge/sample-campaign.md
- knowledge/competitors.md
- knowledge/icps.md

## Approval Status
- Draft

## Success Check
- the output should directly improve positioning and campaign decisions
```

## Step 2: Market Research Agent

### Reads

- handoff from CMO Agent
- `knowledge/sample-campaign.md`
- competitor and ICP knowledge

### Objective

Produce decision-useful research that sharpens the audience and message.

### Expected Output

- key audience pains
- objections
- urgency triggers
- competitor positioning patterns
- implications for messaging

### Example Research Output

```md
1. Research Focus
Understand what makes German restaurant operators consider shifting more order volume away from aggregators.

2. Key Findings
- aggregator commissions and weak direct customer ownership are strong pain points
- operators respond well to transparent pricing and practical ease-of-use
- setup complexity and fear of low guest adoption can block interest

3. Evidence and Signals
- campaign context centered on direct ordering economics
- approved offer notes emphasize no commission per order and own-branded experience

4. Strategic Implications
- position DISH Order as a margin-protection and guest-relationship product
- emphasize commission avoidance, brand ownership, and simple guest ordering

5. Confidence Level
Medium

6. Recommended Knowledge Updates
- add recurring objections around onboarding effort, menu setup, and staff adoption

7. Next Handoff
Send to Messaging and Positioning Agent
```

## Step 3: Messaging and Positioning Agent

### Reads

- CMO direction
- market research output
- brand and offer knowledge

### Objective

Define the best positioning and message hierarchy for the campaign.

### Expected Output

- positioning statement
- value proposition
- key messages
- approved proof themes
- objections to address
- campaign angles

### Example Messaging Output

```md
1. Positioning Statement
For restaurant operators in Germany who want more direct online orders and better margin control, DISH Order provides an own-branded ordering experience without per-order commission fees.

2. Core Value Proposition
Keep more of each order, own the guest experience, and give customers a direct way to order from your restaurant.

3. Key Messages
- reduce dependence on commission-heavy delivery platforms
- strengthen direct guest relationships through your own ordering channel
- give guests a mobile-friendly branded ordering experience

4. Proof Points
- no commission per order
- direct payment through the merchant's own brand experience
- mobile-optimized ordering flow

5. Objections to Address
- concern that setup will be difficult
- doubt that guests will switch from aggregator apps
- uncertainty about operational effort for staff

6. Tone Guidance
Practical, trustworthy, margin-aware, and operationally grounded

7. Recommended Campaign Angles
- fewer commissions, more direct orders
- make your restaurant easier to order from directly
- own the order, own the guest relationship

8. Next Handoff
Send approved message package to Campaign Strategist Agent
```

## Step 4: Campaign Strategist Agent

### Reads

- approved message package
- campaign context
- channel constraints

### Objective

Turn the message into a focused, executable campaign.

### Expected Output

- campaign brief
- channel plan
- asset plan
- KPI plan
- test ideas

### Example Campaign Direction

```md
1. Campaign Summary
Run a focused German conversion campaign around one core promise: win more direct orders without paying per-order commissions.

2. Objective and Audience
Drive qualified DISH Order demo requests from German restaurant operators.

3. Offer and Core Message
Promote DISH Order as a direct ordering channel with stronger economics and better guest ownership.

4. Channel Plan
- landing page as core conversion asset
- lifecycle or outbound email for direct demand generation
- Meta ads for local restaurant operator reach
- sales follow-up after lead capture

5. Asset Plan
- one landing page
- one 3-email German nurture or outbound sequence
- one Meta ad set with angle variants
- one sales follow-up sheet

6. KPI Plan
- primary: qualified demo requests
- secondary: landing page conversion rate, email click-through rate, cost per qualified lead

7. Experiments
- test "no commission per order" against "own your guest relationship"

8. Risks and Constraints
- messaging must avoid overstating savings or implying guaranteed order growth

9. Next Handoff
Send landing page and outbound email tasks to Copywriter Agent
```

## Step 5: Copywriter Agent

### Reads

- campaign brief
- message package
- brand guidance

### Objective

Create the first usable campaign assets for review.

### Expected Output

- landing page draft
- email sequence draft
- headline and CTA variants

### Example Copywriter Deliverables

```md
1. Asset Summary
Landing page hero section for DISH Order Germany

2. Draft Copy
Headline: Mehr Direktbestellungen, weniger Provisionskosten
Subhead: Mit DISH Order bieten Sie Ihren Gaesten einen eigenen Bestellweg fuer Lieferung und Abholung, ohne Provision pro Bestellung.
CTA: Demo buchen

3. Variant Options
- Eigener Bestellshop statt hohe Provisionskosten
- Direkter bestellen lassen, Marge besser schuetzen

4. CTA Options
- Demo buchen
- Jetzt mehr erfahren

5. Assumptions or Open Questions
- customer proof and implementation reassurance should be added before final launch copy

6. Next Handoff
Send draft assets for human review, then route approved assets to campaign execution
```

## Step 6: Analytics and Optimization Agent

### Reads

- campaign brief
- asset list
- KPI targets
- performance data once the campaign is live

### Objective

Define how the team will measure results and learn from them.

### Expected Output

- KPI framework
- reporting cadence
- early warning signals
- optimization recommendations

### Example Analytics Output

```md
1. Performance Summary
Track the campaign weekly against qualified demo requests, landing page conversion, email engagement, and cost per qualified lead.

2. KPI Status
- primary KPI: qualified demo requests
- leading indicators: hero-to-CTA conversion, email click-through rate, qualified lead rate

3. What Worked
- to be filled after launch

4. What Did Not Work
- to be filled after launch

5. Likely Explanations
- to be filled after launch

6. Recommended Next Actions
- compare commission-savings angle versus guest-ownership angle
- compare performance by audience subtype such as independents versus small groups

7. Learning Log Updates
- preserve message-angle results in knowledge/experiments.md

8. Next Handoff
Send learnings back to CMO Agent and Messaging Agent
```

## Human Review Points

Human approval is required before:

- publishing external content
- approving hard performance claims
- changing budget assumptions
- changing core positioning
- sending scaled outbound messaging

## Definition of a Successful Workflow Run

A good workflow run should produce:

- one clear strategic direction
- one coherent message package
- one focused campaign brief
- at least one usable draft asset
- one KPI and learning plan
- explicit approval and escalation points

## Recommended Next Step

After this workflow is stable in markdown, convert it into one of these:

1. a CLI runner that passes files from one agent to the next
2. a prompt orchestration script
3. a manual operating checklist for the team
