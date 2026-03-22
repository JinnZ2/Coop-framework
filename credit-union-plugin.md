Credit Union Co-op Plug-ins
1. Loan Document Summarizer

# Credit Union Loan Agreement Analyzer
# Paste any loan agreement into Claude alongside this template

loan_context = {
    "credit_union": "[Your Credit Union Name]",
    "loan_type": "[auto / mortgage / personal / business / student]",
    "loan_amount": "[dollar amount]",
    "member_name": "[member name or 'general review']",
    "current_market_rates": {
        "auto_36mo": 5.49,
        "auto_60mo": 5.99,
        "mortgage_30yr_fixed": 6.75,
        "mortgage_15yr_fixed": 6.10,
        "personal_unsecured": 10.50,
        "home_equity": 7.25
    }
}

# Ask Claude:
# 1. Summarize this loan agreement in plain English — no legal jargon, like you're explaining it to the member across the desk
# 2. What is the total cost of this loan over its full term (principal + interest + fees)?
# 3. Flag any clauses that could surprise the member: prepayment penalties, rate adjustment triggers, balloon payments, cross-default provisions
# 4. Compare the rate and terms to our current market rates above — is this competitive?
# 5. Identify anything that conflicts with our credit union's member-first philosophy
# 6. Draft a one-page "Loan Summary Sheet" we can hand the member with key terms, payment schedule, and total cost


Example filled in:

loan_context = {
    "credit_union": "Driftless Federal Credit Union",
    "loan_type": "auto",
    "loan_amount": 28500,
    "term_months": 60,
    "rate_offered": 6.24,
    "current_market_rates": {
        "auto_60mo_national_avg": 7.10,
        "auto_60mo_our_cu": 5.99,
        "auto_60mo_competitor_bank": 7.49
    }
}

# Paste loan agreement text below this line, then ask Claude:
# 1. Plain-English summary a member can understand in 2 minutes
# 2. Total cost breakdown: how much of each payment goes to interest vs principal?
# 3. Any red flags in the fine print?
# 4. How does this rate compare to what we could offer in-house?
# 5. Draft a talking-points card for loan officers to walk members through the key terms


2. Member Communication Drafts

Help me write member communications for [Credit Union Name].

Our details:
- Charter type: [federal / state]
- Asset size: [approximate]
- Members: [number]
- Field of membership: [community / employer / association]
- Branches: [number and locations]

Draft the following communications:

1. RATE CHANGE NOTICE
   We're [raising/lowering] our [savings/CD/loan] rates effective [date].
   Old rate: [X]%  New rate: [Y]%
   Reason: [Federal Reserve action / market conditions / competitive positioning]
   Tone: Transparent. Members own this place — tell them why, not just what.
   Include comparison to big bank rates in the area.

2. NEW PRODUCT ANNOUNCEMENT
   Product: [describe — e.g., "Skip-a-Pay program for December"]
   Who it benefits: [target members]
   How to sign up: [process]
   Tone: Helpful, not salesy. Credit unions don't sell — we serve.

3. ANNUAL MEETING INVITATION
   Date: [date]
   Location: [venue]
   Agenda items: [board elections, financial report, guest speaker, door prizes]
   Include: Why attending matters (you're an owner, not a customer)
   Make people actually want to come.

4. DELINQUENCY NOTICE — 30 DAYS
   Member is [30/60/90] days past due on [loan type].
   Amount past due: [amount]
   Tone: Empathetic and firm. We're not a collection agency.
   Acknowledge that life happens. Offer options:
   - Payment plan modification
   - Skip-a-pay if eligible
   - Financial counseling referral
   - Direct line to a person (not a phone tree)
   End with: "We'd rather help you keep your [car/home] than report to collections."

5. COMMUNITY IMPACT REPORT (annual)
   Summarize: loans made, members helped, scholarships given,
   financial literacy events, community sponsorships.
   Format: One-page, visual-friendly, suitable for lobby display or mailing.
   Remind members: every dollar deposited here stays in [community name].


3. Financial Health Dashboard

# Credit Union Financial Health Monitor
# Update monthly, paste into Claude for analysis

financial_data = {
    "credit_union": "[Your Credit Union Name]",
    "reporting_period": "[month/year]",
    "assets": {
        "total_assets": 85000000,
        "total_loans": 52000000,
        "total_shares_deposits": 74000000,
        "investments": 18000000,
        "cash_and_equivalents": 8500000,
        "allowance_for_loan_losses": 520000
    },
    "capital": {
        "net_worth": 9350000,
        "net_worth_ratio_percent": 11.0,  # NCUA well-capitalized threshold: 7%
        "risk_based_capital_ratio": 14.2
    },
    "loan_performance": {
        "total_delinquent_loans": 1040000,
        "delinquency_rate_percent": 2.0,
        "net_charge_offs_ytd": 185000,
        "net_charge_off_rate_percent": 0.36
    },
    "earnings": {
        "net_income_ytd": 425000,
        "return_on_assets_percent": 0.50,
        "net_interest_margin_percent": 3.15,
        "operating_expense_ratio_percent": 3.85,
        "efficiency_ratio_percent": 82.0
    },
    "membership": {
        "total_members": 8200,
        "new_members_ytd": 340,
        "closed_accounts_ytd": 210,
        "net_member_growth_percent": 1.58,
        "avg_member_relationship": 10200  # average total balance per member
    },
    "liquidity": {
        "loan_to_share_ratio_percent": 70.3,
        "available_borrowing_capacity": 12000000,
        "cash_to_assets_percent": 10.0
    }
}

ncua_peer_benchmarks = {
    "asset_class": "$50M-$100M",
    "net_worth_ratio_avg": 10.8,
    "delinquency_rate_avg": 1.5,
    "roa_avg": 0.55,
    "net_interest_margin_avg": 3.25,
    "operating_expense_ratio_avg": 3.70,
    "loan_to_share_avg": 72.0,
    "member_growth_avg": 1.2
}

# Ask Claude:
# 1. How do we compare to NCUA peer benchmarks? Where are we strong, where are we lagging?
# 2. Is our capital position strong enough to absorb a 50% increase in charge-offs?
# 3. Our delinquency rate is above peers — break down what loan categories are driving it
# 4. Trend our net worth ratio over [6/12] months — are we gaining or losing ground?
# 5. Draft the financial summary section of our board report in plain language
# 6. Flag any ratios approaching NCUA watch-list thresholds
# 7. If we grow loans by 10% next quarter, what happens to our liquidity and capital ratios?


4. Compliance & Audit Prep

# Credit Union Compliance Tracker
# Update quarterly, paste into Claude for review

compliance_status = {
    "credit_union": "[Your Credit Union Name]",
    "last_ncua_exam": "[date]",
    "next_ncua_exam_expected": "[date or 'TBD']",
    "camel_rating": "[if known, or 'not disclosed']",
    "bsa_aml": {
        "bsa_officer": "[name]",
        "last_independent_bsa_audit": "[date]",
        "ctrs_filed_ytd": 12,
        "sars_filed_ytd": 3,
        "ofac_screening": "automated — [vendor name]",
        "cdd_enhanced_due_diligence_cases": 5,
        "member_risk_rating_system": "[high/medium/low tiering in place? yes/no]",
        "training_last_completed": "[date]",
        "training_next_due": "[date]"
    },
    "policy_review_schedule": {
        "lending_policy": {"last_reviewed": "2025-06", "next_due": "2026-06", "board_approved": True},
        "investment_policy": {"last_reviewed": "2025-03", "next_due": "2026-03", "board_approved": True},
        "alm_policy": {"last_reviewed": "2024-12", "next_due": "2025-12", "board_approved": True, "status": "OVERDUE"},
        "collections_policy": {"last_reviewed": "2025-09", "next_due": "2026-09", "board_approved": True},
        "bsa_aml_policy": {"last_reviewed": "2025-01", "next_due": "2026-01", "board_approved": True},
        "information_security": {"last_reviewed": "2025-04", "next_due": "2026-04", "board_approved": True},
        "disaster_recovery": {"last_reviewed": "2024-08", "next_due": "2025-08", "board_approved": True, "status": "OVERDUE"},
        "fair_lending": {"last_reviewed": "2025-07", "next_due": "2026-07", "board_approved": True},
        "privacy_policy": {"last_reviewed": "2025-02", "next_due": "2026-02", "board_approved": True}
    },
    "board_reporting": {
        "financial_statements": "monthly",
        "delinquency_report": "monthly",
        "bsa_report": "quarterly",
        "alm_report": "quarterly",
        "audit_findings_tracking": "quarterly",
        "policy_review_calendar": "annually"
    }
}

# Ask Claude:
# 1. Flag every overdue policy review and draft a board resolution to update them
# 2. Build a complete NCUA exam prep checklist — what do examiners look at first?
# 3. Generate a BSA/AML self-assessment: are we doing the minimum or best practice?
# 4. Draft a 12-month compliance calendar with all recurring deadlines
# 5. Create a board-ready compliance summary report for this quarter
# 6. Review our SAR filing count against peer norms — are we under-reporting?
# 7. Summarize the top 5 regulatory changes from the past year that affect credit unions under $[X] in assets
# NOTE: This is an internal planning tool, not legal advice. Consult your examiner and compliance counsel.


5. Community Development & Outreach

Our credit union serves [community/county name] and we want to deepen our impact.

Credit union details:
- Name: [name]
- CDFI certified: [yes/no]
- Low-income designated: [yes/no]
- Underserved areas in field of membership: [describe]
- Current community programs: [list any existing programs]
- Annual community development budget: [amount]

Help me with:

1. FINANCIAL LITERACY WORKSHOP SERIES
   Design a 4-session series for [audience: high school seniors / new homebuyers / small business owners / retirees]:
   - Session topics and learning objectives
   - Handout outlines (one page each, no jargon)
   - Discussion questions and real-world exercises
   - How to promote it — flyers for [laundromats / churches / community centers / schools]
   - Track attendance and outcomes for NCUA community development reporting

2. UNDERSERVED COMMUNITY OUTREACH PLAN
   We want to reach [specific community: immigrant families / rural elderly / unbanked workers / tribal members].
   Current barriers: [language / transportation / distrust of financial institutions / documentation]
   Draft:
   - Outreach strategy that meets people where they are
   - Partnership list: which local organizations should we work with?
   - Products that address their specific needs (second-chance accounts, small-dollar loans, remittances)
   - Staff cultural competency training outline
   - Success metrics that go beyond account openings

3. CDFI GRANT APPLICATION SUPPORT
   We're applying to [CDFI Fund / USDA / state program] for:
   - Project: [describe — e.g., "expand small-dollar lending program to reduce payday loan dependency"]
   - Amount requested: [amount]
   - Community need: [describe the problem]
   - Expected impact: [number of people served, dollars deployed]

   Draft the narrative sections:
   - Statement of need with local data
   - Project description and implementation timeline
   - Community impact projections
   - Sustainability plan after grant period ends
   - How this aligns with our credit union's mission

4. LOCAL PARTNERSHIP DEVELOPMENT
   Map connections between our credit union and:
   - [Food co-op name] — member discount program, financial education at their store
   - [Electric co-op name] — energy efficiency loans, joint billing assistance fund
   - [School district] — youth savings accounts, classroom financial literacy
   - [Employer partners] — payroll deduction, employer-sponsored emergency loans

   Draft partnership proposals for each with mutual benefits clearly stated.

5. IMPACT REPORTING
   Compile our community development activities for the year into:
   - NCUA community development narrative
   - One-page member-facing impact report (lobby display / annual report insert)
   - Board presentation showing ROI of community programs
   - Press release for local newspaper highlighting key numbers


6. Board Reporting & Strategic Planning

# Credit Union Board Packet Generator
# Update monthly, paste into Claude

monthly_board_data = {
    "credit_union": "[Your Credit Union Name]",
    "reporting_month": "[month year]",
    "prepared_by": "[CEO/CFO name]",
    "financials": {
        "total_assets": 85000000,
        "asset_change_from_prior_month": 420000,
        "asset_change_ytd_percent": 3.2,
        "total_loans": 52000000,
        "loan_growth_ytd_percent": 4.8,
        "total_shares": 74000000,
        "share_growth_ytd_percent": 2.1,
        "net_income_month": 38000,
        "net_income_ytd": 425000,
        "net_worth_ratio": 11.0
    },
    "loan_portfolio": {
        "new_loans_funded_month": {"count": 45, "amount": 1850000},
        "loan_types_funded": {
            "auto": {"count": 22, "amount": 680000, "avg_rate": 5.85},
            "mortgage": {"count": 5, "amount": 875000, "avg_rate": 6.50},
            "personal": {"count": 12, "amount": 185000, "avg_rate": 10.25},
            "credit_card": {"count": 6, "amount": 110000, "avg_rate": 14.90}
        },
        "delinquency_30_plus": 1040000,
        "delinquency_rate": 2.0,
        "charge_offs_month": 22000
    },
    "membership": {
        "total_members": 8200,
        "new_members_month": 42,
        "closed_accounts_month": 28,
        "net_growth": 14
    },
    "operations": {
        "branch_transactions": 12500,
        "digital_banking_logins": 34000,
        "call_center_volume": 2800,
        "avg_wait_time_minutes": 3.2,
        "member_complaints": 8,
        "compliments_received": 15
    }
}

strategic_plan_goals = {
    "goal_1": {
        "description": "Grow membership by 5% annually",
        "target": 8600,
        "current": 8200,
        "status": "on track",
        "initiatives": ["SEG development", "community events", "referral program"]
    },
    "goal_2": {
        "description": "Reduce delinquency rate below 1.5%",
        "target": 1.5,
        "current": 2.0,
        "status": "behind",
        "initiatives": ["early intervention program", "financial counseling", "loan modification outreach"]
    },
    "goal_3": {
        "description": "Increase digital adoption to 60% of members",
        "target": 60,
        "current": 41.5,
        "status": "behind",
        "initiatives": ["mobile app upgrade", "in-branch digital coaching", "online loan applications"]
    },
    "goal_4": {
        "description": "Maintain net worth ratio above 10%",
        "target": 10.0,
        "current": 11.0,
        "status": "exceeding",
        "initiatives": ["controlled growth", "earnings retention"]
    }
}

peer_comparison = {
    "peer_group": "federally chartered, $50M-$100M assets, [state]",
    "our_roa": 0.50,
    "peer_roa": 0.55,
    "our_delinquency": 2.0,
    "peer_delinquency": 1.5,
    "our_member_growth": 1.58,
    "peer_member_growth": 1.2,
    "our_loan_to_share": 70.3,
    "peer_loan_to_share": 72.0,
    "our_operating_expense_ratio": 3.85,
    "peer_operating_expense_ratio": 3.70
}

# Ask Claude:
# 1. Generate a complete board packet narrative: financial highlights, concerns, and recommended actions
# 2. Summarize loan production trends — are we lending enough? Too much? Right mix?
# 3. Strategic plan scorecard: red/yellow/green status on each goal with recommended course corrections
# 4. Peer benchmarking analysis: where are we winning, where are we falling behind, and why?
# 5. Draft CEO report to the board — 1 page, plain language, honest about challenges
# 6. Identify the 3 most important decisions the board needs to make this quarter
# 7. Project year-end financials based on current trends — any surprises coming?
# 8. Draft the annual meeting presentation: 10-minute overview of credit union performance for members


How to Use Any of These
1. Go to claude.ai
2. Copy any template above
3. Replace the [brackets] with your real information
4. Hit enter
5. Claude gives you a ready-to-use result
6. Modify, ask follow-ups, refine

No app to install. No training required. No data leaves your conversation.

Built for credit unions. Built to be shared. Pass it on.
