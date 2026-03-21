# Claude for Housing Co-ops: Practical Templates

## How to Use These

These are prompts you can paste directly into Claude. No coding experience needed. Copy, paste, and replace the parts in `[brackets]` with your own information.

Housing co-ops are community anchors — member-owned, democratically governed, and built to keep housing affordable. These templates handle the operational overhead so board members and managers can focus on the community.

---

## 1. Maintenance Request Triage & Tracking

Paste this into Claude:

```
# Housing Co-op Maintenance Tracker
# Update weekly, paste into Claude for analysis

pending_requests = {
    "unit_204": {
        "member": "[Name]",
        "submitted": "[date]",
        "issue": "Bathroom faucet dripping constantly",
        "urgency_reported": "medium",
        "photos_submitted": True,
        "notes": "Has been getting worse over 2 weeks"
    },
    "unit_112": {
        "member": "[Name]",
        "submitted": "[date]",
        "issue": "No heat in bedroom — baseboard unit not working",
        "urgency_reported": "high",
        "photos_submitted": False,
        "notes": "Elderly member, temperatures below freezing this week"
    },
    "unit_305": {
        "member": "[Name]",
        "submitted": "[date]",
        "issue": "Kitchen cabinet door hinge broken, door hanging",
        "urgency_reported": "low",
        "photos_submitted": True,
        "notes": ""
    },
    "common_area_hallway_2nd": {
        "member": "Board report",
        "submitted": "[date]",
        "issue": "Carpet stain and smell near unit 208",
        "urgency_reported": "medium",
        "photos_submitted": True,
        "notes": "Multiple members have mentioned it"
    },
    "unit_118": {
        "member": "[Name]",
        "submitted": "[date]",
        "issue": "Window won't lock — ground floor unit",
        "urgency_reported": "high",
        "photos_submitted": False,
        "notes": "Security concern"
    }
}

maintenance_resources = {
    "in_house_handyperson": {"available_hours_per_week": 20, "hourly_rate": 25},
    "plumber_on_call": {"company": "[name]", "rate": "$95/hour + parts", "response_time": "24-48 hours"},
    "electrician_on_call": {"company": "[name]", "rate": "$110/hour", "response_time": "same day for emergencies"},
    "hvac_contractor": {"company": "[name]", "rate": "$85/hour", "response_time": "24 hours"},
    "monthly_maintenance_budget": 3500
}

# Ask Claude:
# 1. Prioritize these requests by actual urgency (safety > habitability > comfort > cosmetic)
# 2. Which ones can our handyperson handle vs need a contractor?
# 3. Estimate costs for each repair
# 4. Draft a response to each member: acknowledgment, timeline, what to expect
# 5. Flag anything that might be a building code or liability issue
# 6. Will this month's requests fit our budget? If not, what do we defer?
```

---

## 2. Lease & Bylaw Plain-Language Summaries

```
I serve on the board of a housing cooperative. Our members often have
questions about their rights and responsibilities but find our legal
documents hard to understand.

Take the following document and create:

1. PLAIN-LANGUAGE SUMMARY (one page)
   - What this document means for everyday life in the co-op
   - Member rights highlighted clearly
   - Member responsibilities highlighted clearly
   - Common situations and what the rules say about them:
     - Having guests / overnight visitors
     - Noise and quiet hours
     - Pets
     - Modifications to your unit
     - Parking
     - Common area use
     - Subletting or temporary absence

2. FAQ SHEET based on actual questions members ask:
   - "Can I paint my walls?"
   - "What happens if I can't pay my monthly charge?"
   - "How do I request a repair?"
   - "Can my adult child move in with me?"
   - "What are my rights if the board wants to change a rule?"
   - "How do I run for the board?"
   - "What happens when I want to leave the co-op?"

3. NEW MEMBER WELCOME VERSION
   - A warm, non-legal summary of how the co-op works
   - What makes a co-op different from renting an apartment
   - Their ownership stake and what it means
   - How decisions get made (board, committees, general meetings)
   - Who to contact for what

Document to summarize:
[Paste your proprietary lease, occupancy agreement, or bylaws here]

Write at an 8th grade reading level. No legalese.
These are people's homes — the tone should reflect that.
```

---

## 3. Board Communication & Governance

```
I'm the board [president/secretary] of [co-op name], a [number]-unit
housing cooperative in [city, state].

Help me with the following board communications:

1. MONTHLY MEMBER UPDATE
   Recent board actions:
   - [Decision 1: e.g., approved roof repair contract for $45,000]
   - [Decision 2: e.g., updated guest policy to allow 14-day visits]
   - [Decision 3: e.g., approved 2026-2027 budget with 3% maintenance increase]

   Upcoming:
   - [Event/deadline 1]
   - [Event/deadline 2]

   Tone: Transparent, accountable. We work for the members.
   Format: One page, suitable for posting in lobby and emailing.

2. ANNUAL MEETING MATERIALS
   - Agenda for [date] annual meeting
   - Year-in-review summary: financial highlights, major projects
     completed, occupancy rate
   - Proposed budget presentation: plain language, show where the
     money goes using approximate percentages
   - Board candidate statements: [number] seats open
     Candidates: [names and brief bios]
   - Proxy form for members who can't attend

3. DIFFICULT COMMUNICATION
   Situation: [describe — e.g., "We need to do a special assessment
   of $2,000 per unit for emergency boiler replacement" or "A member
   has repeated noise violations and we need to send a formal warning"]

   Draft a communication that is:
   - Factual and specific
   - Empathetic to the impact on members
   - Clear about what happens next
   - Legally careful (we'll have our attorney review, but start with
     a solid draft)

4. COMMITTEE VOLUNTEER RECRUITMENT
   We need members for: [maintenance committee / finance committee /
   social committee / garden committee / welcome committee]
   Draft a recruitment notice that makes it sound appealing,
   not like homework. Include time commitment honestly.
```

---

## 4. Budget Planning & Financial Management

```
# Housing Co-op Budget Planner
# Replace with your actual numbers

current_budget = {
    "units": [number],
    "monthly_maintenance_per_unit_avg": [amount],
    "total_monthly_income": [amount],
    "reserve_fund_balance": [amount],
    "operating_account_balance": [amount]
}

monthly_expenses = {
    "mortgage_or_underlying": [amount],
    "property_taxes": [amount],
    "insurance": [amount],
    "utilities": {
        "water_sewer": [amount],
        "gas_heat": [amount],
        "electric_common_areas": [amount],
        "trash_removal": [amount]
    },
    "maintenance_and_repairs": [amount],
    "management_fee_or_staff": [amount],
    "professional_services": {"legal": [amount], "accounting": [amount]},
    "reserve_contribution": [amount],
    "other": [amount]
}

upcoming_capital_projects = [
    {"project": "Roof replacement", "estimated_cost": [amount], "urgency": "within 2 years"},
    {"project": "Boiler replacement", "estimated_cost": [amount], "urgency": "within 5 years"},
    {"project": "Window replacement phase 1", "estimated_cost": [amount], "urgency": "within 3 years"},
    {"project": "Hallway renovation", "estimated_cost": [amount], "urgency": "cosmetic, flexible"}
]

# Ask Claude:
# 1. Are our reserve contributions adequate for the upcoming capital projects?
# 2. If we need to raise maintenance charges, model 3%, 5%, and 8% increases
# 3. What's our break-even occupancy rate?
# 4. Draft a budget summary for the annual meeting — visual, plain language
#    Show members where each dollar of their maintenance charge goes
# 5. Compare our per-unit costs to typical co-ops in [our city/region]
# 6. Build a 5-year capital plan with funding strategy
#    (reserve allocation vs special assessment vs financing)
# 7. Flag any expenses trending in the wrong direction
```

---

## 5. New Member Onboarding & Community Building

```
We're a [number]-unit housing cooperative in [city].

A new member-owner is moving into unit [number] on [date].

Create an onboarding package:

1. WELCOME LETTER
   - From the board president
   - What makes co-op living different (and better)
   - They're not tenants — they're owners
   - Warm, genuine, makes them feel they joined a community

2. MOVE-IN CHECKLIST
   - Key/fob pickup: [where and when]
   - Parking assignment: [details]
   - Storage unit: [if applicable]
   - Mailbox and intercom setup
   - Utility accounts to set up (if any)
   - Move-in procedures: elevator reservation, loading dock hours,
     floor protection requirements
   - Emergency contacts: superintendent, board president,
     management company

3. CO-OP LIVING GUIDE
   - How to submit maintenance requests
   - Quiet hours and noise policy (friendly version)
   - Laundry room / common area etiquette
   - Recycling and trash procedures
   - Pet policy summary
   - Guest policy summary
   - How to get involved: committees, board, social events
   - Neighbor introduction: [we could include a brief "meet your
     neighbors on your floor" note]

4. GOVERNANCE OVERVIEW
   - Board meeting schedule and how to attend
   - How to propose changes or raise concerns
   - Committee descriptions and how to join
   - Annual meeting: when it is, why it matters, how to vote
   - "Your voice matters here" — this isn't a landlord situation

5. COMMUNITY EVENT IDEAS
   - Plan a "welcome new members" gathering: [quarterly/seasonal]
   - Suggest 3-4 low-cost community building events appropriate
     for [our co-op's demographics: families, seniors, mixed, etc.]
   - Include logistics: space, budget estimate, who organizes

Tone: Warm, practical, community-oriented.
This is their home and their community. Make it feel that way.
```

---

## How to Use Any of These

1. Go to [claude.ai](https://claude.ai)
2. Copy any template above
3. Replace the `[brackets]` with your real information
4. Press Enter
5. Review, refine, ask follow-ups

---

*Housing co-ops keep communities stable. These tools keep co-ops running smoothly.*

*Pass it on.*
