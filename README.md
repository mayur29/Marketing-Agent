# Marketing Agents

This project defines a system of AI marketing agents that can handle a large share of recurring marketing work while keeping humans in control of strategy, approvals, and brand risk.

The aim is to build a practical multi-agent marketing operating system, not a collection of disconnected prompts.

## What This Repo Contains

- `MARKETING_AGENTS.md` for the system-level vision and architecture
- `agents/` for role-specific agent definitions
- `knowledge/` for shared business and market context
- `templates/` for reusable output formats

## V1 Goal

Build a small set of high-leverage agents that can support an end-to-end marketing workflow:

1. understand business goals
2. research the market
3. shape positioning and messaging
4. plan campaigns
5. draft marketing assets
6. analyze results and recommend next actions

## V1 Agents

- `cmo.md`
- `market-research.md`
- `messaging-positioning.md`
- `campaign-strategist.md`
- `copywriter.md`
- `analytics-optimization.md`

## Operating Model

The agents should work as a coordinated system:

1. The CMO Agent turns company goals into priorities
2. The Market Research Agent updates competitive and audience context
3. The Messaging and Positioning Agent defines the core angle
4. The Campaign Strategist Agent creates the campaign plan
5. The Copywriter Agent creates channel-ready drafts
6. The Analytics and Optimization Agent closes the loop with learnings

## Guardrails

- humans approve publishing and budget decisions
- agents must use approved product facts and claims
- all output should be traceable to source context
- brand consistency matters more than content volume
- agents should draft, recommend, and summarize before they automate

## Next Build Steps

- complete all V1 agent files
- define knowledge base templates
- define shared handoff format between agents
- create execution scripts or workflows for invoking the agents
- connect outputs to real channels and analytics sources
