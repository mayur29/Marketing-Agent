# Runbook

This document explains how a human marketer or operator should use the DISH marketing agent system in practice.

The goal is not full autonomy.
The goal is to help a marketing team move faster with clear review points, reusable workflows, and consistent outputs across DISH products.

## Who This Is For

Use this runbook if you are:

- planning a new DISH campaign
- adapting an existing workflow to a different product
- reviewing agent-generated outputs before launch
- using the repo as a repeatable operating system for hospitality marketing

## What This System Produces

For each campaign, the system should generate:

1. strategic direction from the CMO Agent
2. research synthesis from the Market Research Agent
3. a message package from the Messaging and Positioning Agent
4. a filled campaign brief from the Campaign Strategist Agent
5. draft assets from the Copywriter Agent
6. an optimization plan from the Analytics and Optimization Agent

## Core Inputs You Need Before Starting

Before running a campaign, make sure these are available:

- correct DISH product context in `knowledge/offers.md`
- a product-specific sample campaign file in `knowledge/`
- clear market and language context
- approved proof points and claims
- known constraints around pricing, compliance, and launch approvals

## Standard Weekly Workflow

### 1. Choose the Product and Market

Decide:

- which DISH product is being promoted
- which market the campaign is for
- which language and tone register should be used

Examples:

- `DISH Order` in Germany with `DE Sie`
- `DISH Reservation` in Germany with `DE Sie`
- `DISH POS` in Germany with `DE Sie`

### 2. Create or Update the Campaign Input

Use an existing file in `knowledge/` or create a new one modeled after:

- `knowledge/sample-campaign.md`
- `knowledge/sample-campaign-reservation.md`
- `knowledge/sample-campaign-pos.md`

For faster setup, you can scaffold a new campaign workspace with:

```bash
python3 scripts/scaffold_campaign.py \
  --slug website \
  --product "DISH Website" \
  --campaign-name "DISH Website DE Demand Push"
```

This creates:

- one new sample campaign file in `knowledge/`
- the standard output file set in `outputs/`

Make sure the input includes:

- business goal
- audience
- offer
- pain point
- main promise
- proof themes
- channels
- primary KPI

### 3. Run the Strategy Layer

Create or update:

- CMO output
- research handoff
- research output
- messaging output
- campaign brief

Use the examples in `outputs/` as working references.

The order should be:

1. `CMO Agent`
2. `Market Research Agent`
3. `Messaging and Positioning Agent`
4. `Campaign Strategist Agent`

### 4. Review Before Asset Creation

Pause and check:

- is the audience correct?
- are the claims approved?
- does the message match the DISH product?
- does the market and language context appear in the brief?
- are we using the right tone for the market?

Do not move to copy until these are stable.

### 5. Run the Copy Layer

Create:

- landing page draft
- email sequence draft
- paid ad variants

The copy should:

- stay within approved claims
- use the selected market and language guidance
- sound practical and hospitality-specific
- reflect the actual product value, not generic tech messaging

### 6. Review Before Launch

Human review is required before launch.

Check:

- pricing language
- performance claims
- compliance wording
- CTA clarity
- channel fit
- German phrasing quality if the campaign is in DE

### 7. Create the Analytics Plan

Before launch, define:

- primary KPI
- secondary KPIs
- leading indicators
- reporting cadence
- planned experiments

Use the existing analytics plans in `outputs/` as templates.

### 8. Capture Learnings After Launch

After launch, update:

- `knowledge/campaigns.md`
- `knowledge/experiments.md`
- product-specific messaging assumptions if needed

The point is to make every campaign improve the next one.

## Decision Rules For Humans

Use these rules when deciding whether to accept or revise an agent output:

- reject outputs that sound generic or interchangeable across products
- reject outputs that introduce unapproved proof or claims
- reject outputs that ignore the selected market or language
- prefer practical operator language over abstract software language
- prefer one strong campaign angle over too many mixed messages

## File Map

Use these parts of the repo during a campaign:

- `MARKETING_AGENTS.md` for overall system design
- `PRODUCT_PLAYBOOK.md` for product-specific messaging logic
- `RUN_WORKFLOW.md` for the step-by-step agent sequence
- `agents/` for agent contracts
- `knowledge/` for reusable business and market inputs
- `templates/` for handoffs and brief structure
- `outputs/` for real campaign artifacts

## Recommended Operating Rhythm

### Weekly

- choose or update one campaign priority
- run the strategy outputs
- review and approve the campaign brief
- generate draft assets

### Biweekly

- review campaign performance
- update experiments and campaign learnings
- refine product angles based on what is working

### Monthly

- compare outputs across DISH products
- improve the product playbook
- refine agent instructions where outputs are repeatedly weak

## When To Create a New Product Workflow

Create a new workflow run when:

- a DISH product has a meaningfully different pain point
- the audience or market changes
- the proof themes are different enough to require new messaging
- channel strategy changes materially

## Recommended Next Evolution

Once the team is comfortable using this manually, the next step should be one of:

1. a script that scaffolds campaign output files automatically
2. a lightweight CLI that runs the workflow step by step
3. stronger brand and language QA for production-ready German copy
