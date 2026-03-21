Worker-Owned Co-op Plug-ins
1. New Worker-Owner Onboarding

# Worker-Owner Onboarding Tracker
# Update when new members join, paste into Claude

new_member = {
    "name": "[New Member Name]",
    "start_date": "2026-04-01",
    "role": "[primary role — e.g., barista, machinist, delivery driver]",
    "previous_experience": "[brief summary]",
    "probationary_period_months": 6,
    "probationary_end_date": "2026-10-01",
    "equity_buyin": {
        "total_amount": 5000,
        "payment_plan": "payroll deduction",
        "monthly_deduction": 200,
        "months_remaining": 25,
        "amount_paid_to_date": 0
    },
    "governance_training": {
        "bylaws_review": False,
        "board_meeting_observation": False,
        "committee_intro": False,
        "voting_rights_explained": False,
        "financial_transparency_walkthrough": False
    },
    "mentorship": {
        "assigned_mentor": "[Mentor Name]",
        "mentor_role": "[Mentor's role]",
        "mentor_tenure_years": 4,
        "checkin_schedule": "weekly for first 3 months, biweekly after",
        "checkins_completed": 0
    },
    "skills_training": [
        {"skill": "[Core skill 1]", "status": "not started", "trainer": "[Name]"},
        {"skill": "[Core skill 2]", "status": "not started", "trainer": "[Name]"},
        {"skill": "[Safety/compliance training]", "status": "not started", "trainer": "[Name]"}
    ]
}

current_owners = {
    "total_worker_owners": 12,
    "probationary_members": 2,
    "average_tenure_years": 3.5,
    "next_board_meeting": "2026-04-15"
}

# Ask Claude:
# 1. Build a 6-month onboarding checklist with milestones — printable, one page
# 2. Write a plain-language explanation of equity buy-in: what it is, where the money goes, what happens if you leave
# 3. Draft a "your rights and responsibilities as a worker-owner" one-pager — no legalese
# 4. Create a mentorship meeting template with suggested topics for weeks 1, 4, 8, 12
# 5. How many paychecks until equity is fully paid? What's the balance at probation end date?
# 6. Draft a welcome letter from the co-op that explains what makes this different from a regular job


2. Democratic Decision-Making Templates

# Co-op Governance Tracker
# Use before and during member meetings

proposal = {
    "title": "[Proposal title — e.g., Adopt new PTO policy]",
    "submitted_by": "[Member name]",
    "date_submitted": "2026-04-01",
    "category": "[operations / policy / financial / personnel / strategic]",
    "summary": "[2-3 sentence plain-language description of what's being proposed]",
    "problem_it_solves": "[What issue or need prompted this?]",
    "cost_impact": "[Estimated cost or savings, if any]",
    "who_it_affects": "[All members / specific roles / specific committees]",
    "alternatives_considered": [
        "[Alternative 1 and why it wasn't chosen]",
        "[Alternative 2 and why it wasn't chosen]"
    ],
    "decision_method": "consensus",  # or "majority vote" or "supermajority"
    "quorum_required": 9,  # number of members needed for valid decision
    "status": "discussion phase"
}

meeting_log = {
    "date": "2026-04-15",
    "facilitator": "[Name]",
    "notetaker": "[Name]",
    "members_present": ["[Name 1]", "[Name 2]", "[Name 3]"],
    "members_absent": ["[Name 4]"],
    "agenda_items": [
        {"topic": "[Topic 1]", "time_allocated_min": 15, "outcome": ""},
        {"topic": "[Topic 2]", "time_allocated_min": 20, "outcome": ""},
        {"topic": "Vote on [proposal title]", "time_allocated_min": 30, "outcome": ""}
    ],
    "votes_recorded": [
        {
            "proposal": "[Proposal title]",
            "in_favor": 0,
            "opposed": 0,
            "abstained": 0,
            "blocks": 0,  # for consensus process — a block stops the proposal
            "result": "pending"
        }
    ],
    "action_items": [
        {"task": "[Action item]", "assigned_to": "[Name]", "due_date": "2026-04-22"}
    ]
}

# Ask Claude:
# 1. Turn this proposal into a clear, one-page summary any member can understand in 5 minutes
# 2. Draft a facilitation script for this meeting — keep it on track, make sure quieter voices get heard
# 3. Explain our consensus process in plain language: what does "block" mean vs "stand aside" vs "agree"?
# 4. After the meeting: clean up raw notes into formal minutes with motions, votes, and action items
# 5. Create a proposal template we can reuse — simple enough that anyone feels comfortable submitting one
# 6. We've had the same 3 people dominating meetings. Suggest facilitation techniques to balance participation


3. Profit-Sharing & Patronage Calculator

# Worker-Owner Profit Sharing & Patronage Dividends
# NOT tax or legal advice — use this for modeling and board discussion
# Consult your co-op's accountant before finalizing distributions

financials = {
    "fiscal_year": "2025",
    "total_revenue": 820000,
    "total_expenses": 695000,
    "net_surplus": 125000,
    "allocation_policy": {
        "retained_earnings_percent": 40,   # stays in the business
        "patronage_dividend_percent": 50,   # distributed to worker-owners
        "education_fund_percent": 5,        # co-op principle: education
        "community_fund_percent": 5         # donations, local sponsorships
    }
}

worker_owners = [
    {"name": "[Member A]", "hours_worked_annual": 1950, "hourly_rate": 22.00, "tenure_years": 5, "equity_account_balance": 5000},
    {"name": "[Member B]", "hours_worked_annual": 1900, "hourly_rate": 20.00, "tenure_years": 3, "equity_account_balance": 3800},
    {"name": "[Member C]", "hours_worked_annual": 1200, "hourly_rate": 19.00, "tenure_years": 2, "equity_account_balance": 2400},
    {"name": "[Member D]", "hours_worked_annual": 1950, "hourly_rate": 24.00, "tenure_years": 7, "equity_account_balance": 5000},
    {"name": "[Member E]", "hours_worked_annual": 1800, "hourly_rate": 21.00, "tenure_years": 4, "equity_account_balance": 4600},
    {"name": "[Member F]", "hours_worked_annual": 1000, "hourly_rate": 18.00, "tenure_years": 1, "equity_account_balance": 1200}
]

# Patronage is typically allocated based on hours worked (labor patronage)
# Some co-ops use wages paid instead — adapt to your bylaws

# Ask Claude:
# 1. Calculate each member's patronage dividend based on hours worked as percentage of total hours
# 2. Show the full allocation: how much goes to retained earnings, patronage, education, community
# 3. If we pay 60% of patronage in cash and 40% in equity credits, what does each member actually receive?
# 4. Model what happens if we change retained earnings from 40% to 30% — how does that affect each member's payout?
# 5. Draft a one-page explanation of patronage dividends for members: what it is, how it's calculated, tax implications
# 6. Summarize tax basics: patronage dividends are taxable income for members, co-op deducts them — draft a reminder notice
# 7. Project each member's equity account balance in 3 years at current surplus levels
# NOTE: This is a planning tool. Your accountant handles the real numbers and tax filings.


4. Operations & Scheduling

# Worker-Owner Shift Planner
# Balances operational needs with equity — everyone shares the good and bad shifts

scheduling = {
    "business_hours": "7am-7pm, Monday-Saturday",
    "shifts": {
        "opening": {"time": "6:30am-2:30pm", "min_staff": 3, "desirability": "medium"},
        "closing": {"time": "1:30pm-7:30pm", "min_staff": 3, "desirability": "low"},
        "weekend": {"time": "7:00am-7:00pm", "min_staff": 2, "desirability": "low"},
        "admin_day": {"time": "flexible", "min_staff": 1, "desirability": "high"}
    },
    "week_of": "2026-04-06"
}

members = [
    {"name": "[Member A]", "max_hours_week": 40, "availability_restrictions": "no Saturdays (childcare)", "closing_shifts_this_month": 5, "weekend_shifts_this_month": 0, "skills": ["register", "inventory", "ordering", "training"]},
    {"name": "[Member B]", "max_hours_week": 40, "availability_restrictions": "none", "closing_shifts_this_month": 3, "weekend_shifts_this_month": 4, "skills": ["register", "stocking", "receiving"]},
    {"name": "[Member C]", "max_hours_week": 30, "availability_restrictions": "no mornings Mon/Wed (classes)", "closing_shifts_this_month": 6, "weekend_shifts_this_month": 2, "skills": ["register", "inventory", "social media"]},
    {"name": "[Member D]", "max_hours_week": 40, "availability_restrictions": "none", "closing_shifts_this_month": 2, "weekend_shifts_this_month": 1, "skills": ["register", "ordering", "bookkeeping", "maintenance"]},
    {"name": "[Member E]", "max_hours_week": 40, "availability_restrictions": "none", "closing_shifts_this_month": 4, "weekend_shifts_this_month": 3, "skills": ["register", "stocking", "receiving", "training"]},
    {"name": "[Member F]", "max_hours_week": 25, "availability_restrictions": "Tues/Thurs only", "closing_shifts_this_month": 2, "weekend_shifts_this_month": 0, "skills": ["register", "stocking"]}
]

skills_matrix = {
    "register": ["A", "B", "C", "D", "E", "F"],
    "ordering": ["A", "D"],
    "inventory": ["A", "C"],
    "receiving": ["B", "E"],
    "bookkeeping": ["D"],
    "training_new_members": ["A", "E"],
    "maintenance": ["D"],
    "social_media": ["C"],
    "stocking": ["B", "E", "F"]
}

# Ask Claude:
# 1. Build next week's schedule that covers all shifts and respects availability
# 2. Flag equity issues: who's carrying too many undesirable shifts this month?
# 3. Which skills are single points of failure? If Member D is out, who handles bookkeeping?
# 4. Create a cross-training plan so no skill depends on just one person
# 5. Member C wants to increase to 40 hours. Model the schedule impact
# 6. Draft a fair rotation system for weekend and closing shifts — put it in writing so it's transparent
# 7. We want to hire a new member. Based on skills gaps, what should we prioritize in the job posting?


5. Business Development & Growth

# Worker-Owned Co-op Growth Planner
# Use for strategic planning sessions and board discussions

current_state = {
    "business_type": "[bakery / print shop / cleaning service / tech consultancy / etc.]",
    "years_operating": 4,
    "current_worker_owners": 6,
    "annual_revenue": 820000,
    "annual_expenses": 695000,
    "net_surplus": 125000,
    "profit_margin_percent": 15.2,
    "customers_served_monthly": 1200,
    "geographic_reach": "[city/neighborhood/region]",
    "capacity_utilization_percent": 78
}

growth_scenario = {
    "option": "[e.g., open second location / add product line / expand hours / serve new market]",
    "estimated_startup_cost": "[amount]",
    "additional_members_needed": "[number]",
    "projected_new_revenue_annual": "[amount]",
    "projected_new_expenses_annual": "[amount]",
    "timeline_months": "[number]",
    "funding_sources_considered": [
        {"source": "retained earnings", "amount": "[amount]", "terms": "internal"},
        {"source": "[local CDFI or credit union]", "amount": "[amount]", "terms": "[rate and term]"},
        {"source": "new member equity buy-ins", "amount": "[amount]", "terms": "equity"},
        {"source": "[cooperative fund — e.g., Shared Capital Cooperative]", "amount": "[amount]", "terms": "[rate and term]"}
    ]
}

recruitment = {
    "positions_to_fill": [
        {"role": "[Role 1]", "skills_required": "[list]", "full_or_part_time": "full-time"},
        {"role": "[Role 2]", "skills_required": "[list]", "full_or_part_time": "part-time"}
    ],
    "equity_buyin_amount": 5000,
    "probationary_period_months": 6,
    "recruitment_channels": [
        "[local co-op network]",
        "[workforce development program]",
        "[community job board]",
        "[word of mouth from current members]"
    ]
}

# Ask Claude:
# 1. Run a break-even analysis on the growth scenario: when do we recoup the startup cost?
# 2. If we fund expansion with a loan at [X]%, what's our monthly payment and how does it affect surplus?
# 3. Can we grow without taking on debt? Model a slower self-funded timeline using retained earnings only
# 4. Draft a one-page feasibility summary for the full membership to review and vote on
# 5. Write a recruitment posting that explains what worker-ownership means — attract people who want to own their work
# 6. Compare funding sources: cooperative lender vs credit union vs member equity — total cost of each over 5 years
# 7. What's our risk if the expansion underperforms by 25%? Can we absorb the loss without cutting current member pay?


6. Financial Transparency & Reporting

# Open-Book Management Dashboard
# Worker-owners deserve to see the numbers. This helps make them understandable.
# Update monthly, paste into Claude

monthly_financials = {
    "month": "March 2026",
    "revenue": {
        "product_sales": 58000,
        "service_income": 14000,
        "other_income": 500,
        "total_revenue": 72500
    },
    "expenses": {
        "wages_and_benefits": 42000,
        "rent": 4200,
        "utilities": 1100,
        "supplies_and_materials": 8500,
        "insurance": 1400,
        "loan_payments": 2200,
        "marketing": 600,
        "professional_services": 500,  # accountant, lawyer
        "maintenance_and_repairs": 800,
        "miscellaneous": 400,
        "total_expenses": 61700
    },
    "net_surplus": 10800
}

budget_comparison = {
    "revenue_budgeted": 70000,
    "revenue_actual": 72500,
    "revenue_variance": 2500,
    "expenses_budgeted": 60000,
    "expenses_actual": 61700,
    "expenses_variance": -1700,
    "surplus_budgeted": 10000,
    "surplus_actual": 10800,
    "surplus_variance": 800
}

cash_flow = {
    "opening_cash_balance": 45000,
    "cash_in": 68000,     # actual cash received (some revenue not collected yet)
    "cash_out": 59500,    # actual cash paid out
    "closing_cash_balance": 53500,
    "accounts_receivable": 8200,
    "accounts_payable": 4800,
    "loan_balance_remaining": 62000,
    "reserve_fund": 25000,
    "target_reserve_months_expenses": 3  # how many months of expenses we want in reserve
}

year_to_date = {
    "months_completed": 3,
    "ytd_revenue": 210000,
    "ytd_expenses": 182500,
    "ytd_surplus": 27500,
    "annual_budget_revenue": 860000,
    "annual_budget_expenses": 730000,
    "on_track": True
}

# Ask Claude:
# 1. Turn these numbers into a one-page monthly summary any worker-owner can understand — no accounting jargon
# 2. Where are we over budget and why might that be? Flag anything that needs attention
# 3. At current cash flow, how many months of runway do we have if revenue dropped 20%?
# 4. Are we on track to hit our annual targets? Project year-end based on current trends
# 5. Create a simple bar chart description comparing budget vs actuals (for someone to build in a spreadsheet)
# 6. Draft the financial update talking points for our next all-hands meeting — honest, clear, no sugarcoating
# 7. Our reserve fund target is 3 months of expenses. How far away are we and when do we hit it at current savings rate?
# 8. Model next quarter's cash flow: are there any months where we might be tight?


Built for worker-owners. Built to be shared. Pass it on.
