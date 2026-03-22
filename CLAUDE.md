# CLAUDE.md

## Project Overview

Coop-framework is an open-source distribution framework for deploying Claude AI through cooperative networks. It provides strategic maps, operational templates, and educational frameworks designed for grassroots adoption by co-ops (food, grain, electric, credit unions, schools, etc.). Licensed CC0 (public domain) to maximize adoptability.

This is a **documentation and template repository**, not a traditional software package. There is no build system, no dependencies, and no CI/CD pipeline.

## Repository Structure

```
├── README.md                      # Project description with usage guide and file links
├── GETTING_STARTED.md             # Step-by-step guide for non-technical first-time users
├── template-index.md              # Complete catalog of all templates with descriptions
├── LICENSE                        # CC0 1.0 Universal (public domain)
├── Co-op-map.md                   # Strategic framework: co-op networks by region, type, trust propagation
├── trust-first.md                 # Philosophical positioning document
├── practical-plugins.md           # 11 copy-paste Claude templates for food/grain/electric co-ops
├── Montessori-plugin.md           # 6 Claude templates for Montessori schools
├── grain-elevator-coop.md         # 5 Claude templates for grain elevator operations
├── auto-repair-shop-plugin.md     # Claude templates for auto repair shop operations
├── credit-union-plugin.md         # 6 Claude templates for credit union operations
├── housing-coop-plugin.md         # 6 Claude templates for housing co-op operations
├── rural-electric-coop-plugin.md   # 6 Claude templates for rural electric co-op operations
├── tribal-enterprise-plugin.md    # 6 Claude templates for tribal enterprise operations
├── worker-owned-plugin.md         # 6 Claude templates for worker-owned business operations
├── coop_sim.py                    # Runnable co-op network simulation with CSV export
├── democratic-ai-education.py     # Pseudo-code educational AI transition framework
└── mentorship-learning-ai.py      # Pseudo-code AI mentorship/observation system
```

All files live at the root level. No subdirectories.

## File Types and Conventions

### Markdown Files (`.md`)
- Strategic documents and operational templates
- Templates use `[brackets]` to indicate user-customizable sections
- Grouped by industry/use case (agriculture, education, general co-op operations)
- Designed to be copy-pasted directly into Claude.ai by non-technical users

### Python Files (`.py`)
- **Educational pseudo-code**, not production-runnable code
- Demonstrate conceptual frameworks for AI-integrated education and mentorship
- Classes use descriptive, business-focused names (e.g., `EducationTransitionFramework`, `MentorshipObservationAI`)
- Include `run_simulation()` functions and `if __name__ == "__main__"` blocks as demonstration examples
- Note: Some syntax is intentionally pseudo-code (e.g., `**init**` instead of `__init__`)

## Key Naming Conventions

- **File names**: lowercase with hyphens (e.g., `grain-elevator-coop.md`)
- **Python identifiers**: snake_case for variables/functions, PascalCase for classes
- **Template names**: descriptive of the specific use case they address

## Running the Simulation

```bash
python3 coop_sim.py              # base simulation (trust, growth, resources)
python3 coop_sim.py --extended   # all extensions enabled
```

No dependencies required — stdlib only (`random`, `math`, `sys`).

## No Build/Test/Lint Commands

This project has no:
- Package manager or dependency installation
- Build process
- Test suite or test framework
- Linters or formatters
- CI/CD pipeline

## How to Contribute

1. **New plugin templates**: Create a new `.md` file at root following the pattern of existing plugins. Include description, example data with `[customizable]` sections, Claude prompts, and expected outputs.
2. **New industry verticals**: Follow the pattern of `grain-elevator-coop.md` or `Montessori-plugin.md` — 5-6 templates covering core operations for that industry.
3. **Educational frameworks**: Python pseudo-code files modeling AI integration concepts. Focus on clarity over runnability.
4. **Strategic documents**: Markdown files mapping distribution channels and trust propagation.

## Design Philosophy

- No data collection or upstream reporting
- No lock-in contracts or proprietary dependencies
- Forking and adaptation explicitly encouraged
- Templates must work by copy-paste into Claude.ai — no technical setup required
- Trust-based, grassroots distribution model
- Anti-extraction, anti-lock-in by design

## Co-op Type Taxonomy (for context)

- **Tier 1 (Direct Supply Chain)**: Food/grocery, grain/agricultural, worker-owned co-ops
- **Tier 2 (Infrastructure)**: Rural electric, credit unions, housing co-ops
- **Tier 3 (Multiplier Nodes)**: Co-op development funds, umbrella organizations, tribal enterprises

## Geographic Strategy

- **Phase 1**: Minnesota (densest co-op network) + Portland, Oregon
- **Phase 2**: Wisconsin, Vermont, Appalachia, Northern Michigan, Dakotas
