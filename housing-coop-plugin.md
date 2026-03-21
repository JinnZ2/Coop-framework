Housing Co-op Plug-ins
1. Maintenance Request Triage

# Housing Co-op Maintenance Tracker
# Update weekly, paste into Claude for analysis

maintenance_requests = {
    "open_requests": [
        {"unit": "4B", "member": "[Name]", "submitted": "2026-03-10", "category": "plumbing", "description": "Kitchen faucet leaking steadily", "priority": "medium", "estimated_cost": 250, "assigned_to": None},
        {"unit": "2A", "member": "[Name]", "submitted": "2026-03-08", "category": "heating", "description": "Radiator not producing heat in bedroom", "priority": "high", "estimated_cost": 600, "assigned_to": "Driftless Mechanical"},
        {"unit": "7C", "member": "[Name]", "submitted": "2026-03-12", "category": "electrical", "description": "Outlet sparking in bathroom", "priority": "urgent", "estimated_cost": 350, "assigned_to": None},
        {"unit": "1D", "member": "[Name]", "submitted": "2026-03-01", "category": "appliance", "description": "Refrigerator not cooling properly", "priority": "high", "estimated_cost": 400, "assigned_to": "Valley Appliance"},
        {"unit": "5A", "member": "[Name]", "submitted": "2026-02-20", "category": "structural", "description": "Crack in living room ceiling, appears to be growing", "priority": "medium", "estimated_cost": "unknown", "assigned_to": None},
        {"unit": "3B", "member": "[Name]", "submitted": "2026-03-14", "category": "pest_control", "description": "Mice spotted in kitchen two nights in a row", "priority": "medium", "estimated_cost": 200, "assigned_to": None}
    ],
    "contractors": [
        {"name": "Driftless Mechanical", "specialty": "plumbing, heating", "rate": "85/hr", "availability": "Mon-Fri", "rating": "reliable"},
        {"name": "Valley Appliance", "specialty": "appliances", "rate": "75/hr + parts", "availability": "Tue-Sat", "rating": "reliable"},
        {"name": "County Electric", "specialty": "electrical", "rate": "95/hr", "availability": "Mon-Fri, emergency weekends", "rating": "good"},
        {"name": "[Contractor name]", "specialty": "[type]", "rate": "[rate]", "availability": "[days]", "rating": "[notes]"}
    ],
    "annual_maintenance_budget": 45000,
    "spent_ytd": 18200,
    "month": "March"
}

completed_last_90_days = [
    {"unit": "2A", "category": "plumbing", "cost": 320, "date": "2026-01-15"},
    {"unit": "6B", "category": "plumbing", "cost": 180, "date": "2026-02-02"},
    {"unit": "4B", "category": "plumbing", "cost": 275, "date": "2026-02-18"},
    {"unit": "2A", "category": "heating", "cost": 450, "date": "2025-12-20"},
    {"unit": "3A", "category": "appliance", "cost": 550, "date": "2026-01-28"},
    {"unit": "7C", "category": "electrical", "cost": 200, "date": "2026-02-10"}
]

# Ask Claude:
# 1. Prioritize open requests by safety risk and assign to available contractors
# 2. Unit 2A has had 3 repairs in 90 days — is there a bigger problem here?
# 3. Flag any recurring issues by category or building area
# 4. At current spend rate, will we stay within annual budget?
# 5. Draft a maintenance update email to all members — status of open requests, no unit names
# 6. Which requests need board approval based on cost threshold of $[amount]?


2. Lease & Bylaw Plain-Language Summarizer

I'm on the board of a housing co-op. I'm going to paste our
[occupancy agreement / bylaws / house rules / proprietary lease] below.

Please:

1. Summarize the entire document in plain English. No legal jargon.
   Write it so a new member with no legal background can understand
   every section.

2. Flag any unusual or potentially problematic clauses:
   - Anything that limits members' rights more than typical co-op agreements
   - Clauses that give the board unusual power without member vote
   - Financial obligations beyond standard monthly assessments
   - Restrictions on subletting, guests, modifications, or pets
   - Anything about forced sale or involuntary termination of membership
   - Dispute resolution clauses (arbitration vs court)

3. Generate a one-page FAQ for new members:
   - What am I actually paying for each month?
   - What can I change in my unit without permission?
   - What needs board approval?
   - How do I vote on co-op decisions?
   - What happens if I want to leave?
   - What happens if I fall behind on payments?
   - Who do I contact for what?

4. Compare this document to standard housing co-op best practices.
   Note anything missing that should be there:
   - Maintenance responsibility split (co-op vs member)
   - Reserve fund requirements
   - Conflict resolution process
   - Anti-discrimination language
   - Accessibility provisions

Document text:
[Paste your occupancy agreement, bylaws, or house rules here]


3. Board Communication & Meeting Prep

# Housing Co-op Board Communication Hub
# Use any section independently — paste into Claude with your info

# --- SECTION A: Agenda Generator ---

upcoming_meeting = {
    "type": "monthly board meeting",
    "date": "[date]",
    "time": "[time]",
    "location": "[location or virtual link]",
    "old_business": [
        "[Elevator repair contract — vote needed]",
        "[Parking policy update — second reading]",
        "[Landscaping bid review — 3 bids received]"
    ],
    "new_business": [
        "[Roof inspection results]",
        "[Holiday party planning]",
        "[New member application — Unit 6A]"
    ],
    "committee_reports": [
        {"committee": "Finance", "chair": "[Name]", "topic": "[Monthly financial summary]"},
        {"committee": "Maintenance", "chair": "[Name]", "topic": "[Open work orders update]"},
        {"committee": "Membership", "chair": "[Name]", "topic": "[Waitlist status]"}
    ],
    "member_concerns_submitted": [
        "[Noise complaint from 3rd floor]",
        "[Bike storage request]",
        "[Recycling bin overflow]"
    ]
}

# Ask Claude:
# 1. Build a formal agenda with time estimates for each item
# 2. Flag which items require a member vote vs board-only decision
# 3. Draft a meeting notice to all members (email-ready, include date/time/location)
# 4. Estimate total meeting length and suggest what to table if it runs over 90 minutes

# --- SECTION B: Minutes Processor ---

# Paste your raw notes from the board meeting below.
# Handwritten notes, bullet points, even voice-to-text transcripts work.

# Ask Claude to organize into:
# 1. Formal minutes with: date, attendees, call to order, quorum confirmed
# 2. Each agenda item: discussion summary, motions made, who moved/seconded, vote result
# 3. Action items table: task, assigned to, deadline
# 4. Next meeting date and any items tabled for next time
#
# Raw notes:
# [Paste your meeting notes here]

# --- SECTION C: Member Notifications ---

# Generate ready-to-send member communications:
#
# 1. Policy change announcement:
#    Policy: [describe the change]
#    Effective date: [date]
#    Reason for change: [brief explanation]
#    How it affects members: [practical impact]
#    Tone: Respectful, clear, not condescending
#
# 2. Building-wide notice:
#    Topic: [water shutoff / construction / inspection / pest treatment]
#    Date and time: [when]
#    Duration: [how long]
#    What members need to do: [specific actions]
#    Contact for questions: [name and number]
#
# 3. Annual meeting announcement:
#    Include: date, time, location, agenda preview, board election info,
#    proxy voting instructions, RSVP request, childcare availability


4. Financial Management

# Housing Co-op Financial Dashboard
# Update monthly, paste into Claude for analysis

monthly_financials = {
    "assessments": {
        "total_units": 24,
        "monthly_assessment_per_unit": 875,
        "expected_monthly_revenue": 21000,
        "collected_this_month": 19250,
        "delinquent_units": [
            {"unit": "3A", "months_behind": 2, "amount_owed": 1750, "payment_plan": False},
            {"unit": "8B", "months_behind": 1, "amount_owed": 875, "payment_plan": True}
        ]
    },
    "monthly_expenses": {
        "mortgage_or_land_lease": 8500,
        "property_taxes_escrow": 3200,
        "insurance": 1400,
        "utilities_common_area": 1800,
        "water_sewer": 2100,
        "trash_removal": 450,
        "management_fee_or_admin": 1500,
        "routine_maintenance": 1200,
        "landscaping_snow": 600,
        "reserve_fund_contribution": 2000,
        "legal_accounting": 300
    },
    "reserve_fund": {
        "current_balance": 68000,
        "target_balance": 150000,
        "monthly_contribution": 2000,
        "recent_withdrawals": [
            {"item": "Boiler repair", "amount": 12000, "date": "2026-01-15"}
        ]
    },
    "upcoming_capital_improvements": [
        {"project": "Roof replacement", "estimated_cost": 85000, "urgency": "within 2 years"},
        {"project": "Window upgrades (common areas)", "estimated_cost": 15000, "urgency": "within 1 year"},
        {"project": "Lobby renovation", "estimated_cost": 8000, "urgency": "elective"},
        {"project": "Elevator modernization", "estimated_cost": 45000, "urgency": "within 3 years"}
    ]
}

# Ask Claude:
# 1. Are we running at surplus or deficit this month? Year-to-date?
# 2. At current contribution rate, when do we hit our reserve fund target?
# 3. Can we fund the roof replacement from reserves, or do we need a special assessment?
# 4. If we need a special assessment, what's the per-unit cost spread over 6/12/18 months?
# 5. Draft a delinquency notice for unit 3A — firm but respectful, include payment plan option
# 6. Build a 5-year capital improvement timeline matched against projected reserve fund balance
# 7. Draft a one-page financial summary for the annual meeting — plain language, no accounting jargon


5. New Member Onboarding

A new member is moving into Unit [number] on [date].

Our co-op details:
- Co-op name: [name]
- Address: [address]
- Number of units: [number]
- Year established: [year]
- Equity share / membership fee: $[amount]
- Monthly assessment: $[amount]
- Board contact: [name, phone, email]
- Management contact: [name, phone, email]
- Emergency maintenance: [phone number]

Generate a complete onboarding package:

1. Welcome letter:
   - Warm, personal tone. They just joined a community, not signed a lease.
   - What it means to be a member-owner (not a tenant)
   - How decisions get made (board meetings, member votes, committees)
   - Encouragement to get involved

2. House rules summary — one page, plain language:
   - Quiet hours: [times]
   - Guest policy: [summary]
   - Pet policy: [summary]
   - Parking: [summary]
   - Common area use: [laundry, roof, garden, storage, etc.]
   - Trash and recycling: [schedule and locations]
   - Move-in/move-out rules: [elevator reservations, hours, deposits]
   - What to do about maintenance issues: [process]

3. Move-in checklist:
   - Before move-in day: reserve elevator, get keys, set up utilities
   - Move-in day: check-in with [contact], unit walkthrough, sign condition report
   - First week: meet neighbors, find mailbox, locate storage, emergency exits
   - First month: attend board meeting, join a committee, review bylaws

4. Equity share explanation — written for someone who has never heard of this:
   - What it is (your ownership stake)
   - What it costs
   - What it gets you
   - What happens to it when you leave
   - How it's different from a security deposit

5. Key contacts and resources — one-page reference card:
   - Board president
   - Treasurer
   - Management company
   - Emergency maintenance
   - Nearest hospital / urgent care
   - Non-emergency police
   - Building super / handyperson
   - Recycling and bulk trash schedule


6. Conflict Resolution & Governance

Our housing co-op needs help with member conflicts and governance.

Co-op details:
- Units: [number]
- Members: [number]
- Current board size: [number]
- Bylaws last updated: [year]
- Conflict resolution process: [describe current process or "none formal"]

Help with the following:

1. Noise / behavior complaint template:
   Write a form members can fill out when they have a complaint.
   Include: date, time, unit making complaint, nature of issue,
   how many times it's happened, whether they've spoken directly
   to the other member, and desired resolution.
   Tone: Neutral. This is documentation, not accusation.

2. Mediation process documentation:
   - Step-by-step process from complaint filed to resolution
   - Step 1: Direct conversation between members (with guidance)
   - Step 2: Written complaint to board / management
   - Step 3: Mediation meeting with neutral board member or outside mediator
   - Step 4: Board hearing with both parties
   - Step 5: Board decision, written and delivered to both parties
   - Include timeline expectations at each step
   - Template letters for each step

3. Voting procedure guide for members:
   Explain how co-op voting works in plain language:
   - What decisions require member vote vs board vote
   - How many votes each unit/member gets
   - Quorum requirements: [number or percentage]
   - Proxy voting: how it works, form to fill out
   - How to propose a motion at a member meeting
   - How amendments to bylaws work
   - How board elections work: nominations, terms, eligibility

4. Bylaw amendment drafts:
   Our board wants to propose the following changes:
   - [Describe proposed change 1, e.g., "Allow subletting with board approval"]
   - [Describe proposed change 2, e.g., "Create a mandatory reserve fund policy"]
   - [Describe proposed change 3, e.g., "Update pet policy to allow dogs under 40 lbs"]

   For each proposed change:
   - Draft the formal amendment language
   - Write a plain-English explanation for members
   - Draft the notice to members with required advance notice per bylaws
   - Create a simple ballot or voting form

5. Board code of conduct:
   Draft a one-page code of conduct for board members covering:
   - Fiduciary duty to the co-op
   - Conflict of interest disclosure
   - Confidentiality of member information
   - Fair and impartial decision-making
   - How to handle complaints against board members themselves
   - Term limits and succession planning


Built for housing co-ops. Built to be shared. Pass it on.
