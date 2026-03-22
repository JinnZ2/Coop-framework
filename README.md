# Coop-framework

**Open-source templates for deploying Claude AI through cooperative networks.**

Co-ops already run on trust, shared ownership, and word-of-mouth. This framework gives them AI tools that work the same way — no data extraction, no lock-in, no corporate middleman. Just copy-paste templates that help real people run real operations.

## Who This Is For

- **Food co-op** managers juggling vendors, inventory, and member newsletters
- **Grain elevator** operators tracking harvest intake, basis pricing, and rail logistics
- **Rural electric co-op** staff managing outages, load forecasting, vegetation management, and rate design
- **Tribal enterprise** leaders balancing sovereignty, federal grants, community impact, and economic development
- **Credit union** teams handling loan documents, compliance, and community outreach
- **Housing co-op** boards managing maintenance, bylaws, and new member onboarding
- **Worker-owned businesses** coordinating democratic decisions, profit-sharing, and scheduling
- **Montessori schools** tracking enrollment, curriculum documentation, and budgets
- **Auto repair shops** managing job tracking, parts ordering, and customer communication
- Anyone who runs a small operation and wants AI to help without strings attached

## How It Works

1. Pick a template from the list below
2. Go to [claude.ai](https://claude.ai)
3. Copy the template, replace the `[brackets]` with your real information
4. Hit enter — Claude gives you a ready-to-use result

No app to install. No coding. No training required. See [GETTING_STARTED.md](GETTING_STARTED.md) for a detailed walkthrough.

## Templates by Industry

### General Co-op Operations — [practical-plugins.md](practical-plugins.md)
11 templates covering vendor orders, board minutes, delivery routes, grant applications, contract analysis, inventory tracking, newsletters, cost modeling, event planning, knowledge preservation, and price comparison.

### Grain Elevator Co-ops — [grain-elevator-coop.md](grain-elevator-coop.md)
5 templates for harvest intake tracking, basis & pricing analysis, transportation logistics, compliance & reporting, and farmer communication.

### Electric Co-ops — [practical-plugins.md](practical-plugins.md#electrical-co-op-plug-ins)
5 templates for outage response, load forecasting, line maintenance scheduling, rate communication, and solar/distributed generation management.

### Montessori Schools — [Montessori-plugin.md](Montessori-plugin.md)
6 templates for enrollment management, curriculum documentation, budget modeling, licensing compliance, community integration, and staff retention.

### Auto Repair Shops — [auto-repair-shop-plugin.md](auto-repair-shop-plugin.md)
Templates for job tracking, estimates, parts management, and customer communication.

### Rural Electric Co-ops — [rural-electric-coop-plugin.md](rural-electric-coop-plugin.md)
6 templates for outage management, load forecasting, vegetation management, capital credits, rate design, and renewable energy/distributed generation.

### Tribal Enterprises — [tribal-enterprise-plugin.md](tribal-enterprise-plugin.md)
6 templates for sovereignty-aligned business planning, federal grants & contracts, community impact tracking, cultural tourism, infrastructure/broadband development, and inter-tribal partnerships.

### Credit Unions — [credit-union-plugin.md](credit-union-plugin.md)
6 templates for loan document analysis, member communication, financial health dashboards, compliance prep, community development, and board reporting.

### Housing Co-ops — [housing-coop-plugin.md](housing-coop-plugin.md)
6 templates for maintenance triage, bylaw summarization, board communication, financial management, member onboarding, and conflict resolution.

### Worker-Owned Businesses — [worker-owned-plugin.md](worker-owned-plugin.md)
6 templates for onboarding new worker-owners, democratic decision-making, profit-sharing calculations, scheduling, business development, and financial transparency.

## Strategic Documents

- **[Co-op-map.md](Co-op-map.md)** — Geographic strategy for co-op network adoption, starting with Minnesota and Portland
- **[trust-first.md](trust-first.md)** — Why trust-based distribution matters and how co-ops are built for it

## Simulation

A runnable network simulation that models trust propagation, network growth, and resource sharing across co-op networks.

```bash
python3 coop_sim.py                    # base simulation
python3 coop_sim.py --extended         # all extensions (bridge events, adoption decay, type affinity)
python3 coop_sim.py --csv results.csv  # export results to CSV
```

No dependencies — Python 3 standard library only.

## Template Index

See **[template-index.md](template-index.md)** for a complete catalog of every template with one-line descriptions.

## Educational Frameworks

- **[democratic-ai-education.py](democratic-ai-education.py)** — Pseudo-code framework for AI-integrated democratic education
- **[mentorship-learning-ai.py](mentorship-learning-ai.py)** — Pseudo-code AI mentorship and observation system

These are conceptual demonstrations, not production code.

## Contributing

1. **New templates**: Create a `.md` file at root. Include description, example data with `[customizable]` sections, Claude prompts, and expected outputs.
2. **New industries**: Follow the pattern of existing plugins — 5-6 templates covering core operations.
3. **Improvements**: Better examples, sample outputs, or real-world refinements to existing templates.

See [CLAUDE.md](CLAUDE.md) for detailed conventions.

## License

**CC0 1.0 Universal** — Public domain. No restrictions. Fork it, adapt it, share it. This is infrastructure, not intellectual property.

## Design Principles

- No data collection or upstream reporting
- No lock-in contracts or proprietary dependencies
- Templates work by copy-paste into Claude.ai — zero technical setup
- Trust-based, grassroots distribution
- Anti-extraction, anti-lock-in by design

---

*Seeds don't need permission to grow. They just need to be planted in good soil.*
