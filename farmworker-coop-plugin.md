Farmworker Co-op Plug-ins
1. Crew Scheduling & Job Dispatch

# Farmworker Co-op Crew Scheduler
# Update weekly during season, paste into Claude

crew_schedule = {
    "co_op": "[Your Farmworker Co-op Name]",
    "week_of": "[date]",
    "total_members": 65,
    "members_available_this_week": 52,
    "members_unavailable": {
        "injured_workers_comp": 2,
        "personal_leave": 3,
        "training": 4,
        "between_contracts": 4
    },
    "active_contracts": [
        {
            "grower": "[Farm A — Smith Orchards]",
            "crop": "[apples]",
            "task": "[harvest / pruning / thinning / planting / irrigation / packing]",
            "location": "[address or area]",
            "workers_needed": 18,
            "workers_assigned": 18,
            "start_date": "[date]",
            "end_date": "[date]",
            "rate_type": "[hourly / piece rate / contract]",
            "rate": "[amount]",
            "housing_provided": "[yes/no]",
            "transportation_provided": "[yes/no]",
            "estimated_duration_weeks": 6
        },
        {
            "grower": "[Farm B — Valley Vineyards]",
            "crop": "[grapes]",
            "task": "[harvest]",
            "location": "[address]",
            "workers_needed": 12,
            "workers_assigned": 10,
            "start_date": "[date]",
            "end_date": "[date]",
            "rate_type": "piece rate",
            "rate": "[amount per bin/lug]",
            "housing_provided": "[yes/no]",
            "transportation_provided": "[yes/no]",
            "estimated_duration_weeks": 3
        }
    ],
    "upcoming_contracts": [
        {
            "grower": "[Farm C]",
            "crop": "[crop]",
            "task": "[task]",
            "workers_needed": 15,
            "start_date": "[date]",
            "rate_negotiated": "[yes/no]",
            "housing_available": "[yes/no]"
        }
    ],
    "transportation": {
        "co_op_vans": 3,
        "van_capacity": 12,
        "routes_running": 2,
        "fuel_cost_weekly": 450,
        "mileage_reimbursement_if_personal": 0.67
    }
}

# Ask Claude:
# 1. We're 2 workers short on Farm B — who's available and closest? Factor in transportation logistics
# 2. Build next week's crew assignments optimizing for: shortest commute, skill match, fair rotation
# 3. Farm C starts in 2 weeks and needs 15 — can we staff it without pulling from active contracts?
# 4. Transportation costs: is it cheaper to run a third van route or reimburse personal vehicles?
# 5. Draft the weekly crew schedule with assignments, report times, locations, and contact info
# 6. Track hours by member across all contracts — is work being distributed fairly?
# 7. Model the revenue impact if we negotiate $1/hour more on the Farm B contract


2. Contract Negotiation & Rate Setting

Help me negotiate fair contracts between our farmworker co-op and growers.

Co-op details:
- Name: [co-op name]
- Location: [region/state]
- Members: [number]
- Primary crops/tasks: [list]
- Current season: [crop and phase]

Help me with:

1. RATE ANALYSIS
   Current rates we're being offered:
   - [Crop A — task]: $[X] per [hour / piece / bin / acre]
   - [Crop B — task]: $[X] per [hour / piece / bin / acre]

   Research and compare:
   - State minimum wage: $[X]
   - Prevailing wage for this crop/task in our region (DOL/AEWR): $[X]
   - What other crews are getting paid in the area (if known): $[X]
   - Calculate: at the offered piece rate, what's the effective hourly rate for an average-speed worker?
   - Is the offered rate above or below the Adverse Effect Wage Rate?
   - Draft a counter-proposal with data supporting a higher rate

2. CONTRACT TEMPLATE
   Draft a standard service agreement between our co-op and a grower covering:
   - Scope of work: specific tasks, quality standards, acreage/volume
   - Crew size and scheduling: guaranteed minimum hours, rain day policy
   - Compensation: rate, payment schedule (weekly), overtime, piece rate guarantees
   - Housing: condition standards, occupancy limits, utilities, maintenance responsibility
   - Transportation: who provides, insurance requirements, mileage
   - Safety: equipment provided, training requirements, heat illness prevention, first aid
   - Worker protections: no retaliation, grievance process, right to organize
   - Insurance and liability: workers comp, general liability, vehicle insurance
   - Termination: notice requirements, completion bonuses, return of housing deposit

3. GROWER RELATIONSHIP MANAGEMENT
   We work with [number] growers regularly.
   Build a grower scorecard tracking:
   - Payment reliability and timeliness
   - Housing quality and condition
   - Safety record and incident response
   - Communication and respect toward workers
   - Rate competitiveness year over year
   - Contract volume and consistency
   Draft an annual review letter to our best growers acknowledging the partnership.
   Draft a concerns letter to growers where conditions need improvement.


3. Payroll & Benefits Administration

# Farmworker Co-op Payroll Tracker
# Update weekly, paste into Claude

weekly_payroll = {
    "co_op": "[Your Farmworker Co-op Name]",
    "pay_period": "[dates]",
    "state": "[state]",
    "member_hours": [
        {
            "member": "[Member A]",
            "contract": "[Farm A — apples]",
            "hours_worked": 48,
            "overtime_hours": 8,  # state agricultural overtime rules vary
            "piece_rate_units": 0,  # or number if piece rate
            "hourly_rate": 18.50,
            "overtime_rate": 27.75,
            "gross_pay": 1110.00,
            "deductions": {
                "federal_tax": 111.00,
                "state_tax": 55.50,
                "social_security": 68.82,
                "medicare": 16.10,
                "co_op_dues": 25.00,
                "transportation_fee": 15.00,
                "housing_if_applicable": 0
            },
            "net_pay": 818.58
        }
    ],
    "co_op_financials": {
        "total_billed_to_growers": 32000,
        "total_paid_to_members": 26500,
        "co_op_margin": 5500,
        "margin_percent": 17.2,
        "margin_covers": ["admin staff", "insurance", "transportation", "training", "reserve fund"],
        "workers_comp_premium_monthly": 1800,
        "general_liability_monthly": 450,
        "vehicle_insurance_monthly": 380,
        "admin_salary_monthly": 3500
    },
    "benefits": {
        "health_insurance_enrolled": "[number or 'not offered']",
        "health_insurance_co_op_contribution": "[amount per member per month]",
        "retirement_plan": "[type or 'none']",
        "paid_sick_leave_accrued_hours": "[per member]",
        "training_hours_paid_ytd": "[per member average]"
    }
}

# Ask Claude:
# 1. Calculate complete payroll for all members this week with proper tax withholding
# 2. Piece rate check: did every member earn at least minimum wage equivalent? Flag anyone below
# 3. Our margin is 17.2% — is that sustainable? What's the minimum margin to cover overhead?
# 4. Build an annual benefits comparison: what would it cost to offer health insurance to all members?
# 5. Overtime rules: summarize our state's agricultural overtime laws and flag any compliance issues
# 6. Draft individual pay stubs for each member (printable, bilingual English/Spanish)
# 7. Year-end: generate W-2 preparation summary for all members
# 8. Model what happens to member take-home pay if we raise the co-op margin from 17% to 20%


4. Housing & Transportation Coordination

Help me manage housing and transportation for our farmworker co-op members.

Co-op details:
- Name: [co-op name]
- Members: [number]
- Region: [area]
- Seasonal or year-round: [which]
- Members needing housing: [number]
- Members needing transportation: [number]

Help me with:

1. HOUSING INVENTORY & STANDARDS
   Our members live in:
   - Grower-provided housing at [Farm A]: [number] units, [condition: good/fair/poor]
   - Grower-provided housing at [Farm B]: [number] units, [condition]
   - Co-op rented housing: [number] units at [location], $[rent]/month
   - Members' own housing: [number]

   Generate:
   - Housing inspection checklist based on [state/federal] farmworker housing standards
   - Condition report template for documenting issues with photos
   - Complaint escalation process: who to contact at the grower, at the co-op, and at the state agency
   - Template letter to grower requesting housing repairs with deadline
   - Know-your-rights summary for members about housing standards (bilingual)

2. TRANSPORTATION SYSTEM
   - Map our daily routes: [pickup points to work sites]
   - Calculate cost per member per day for co-op van service
   - Vehicle maintenance schedule for co-op vans
   - Backup plan when a van breaks down
   - Insurance and licensing requirements for transporting workers
   - Draft a transportation policy: pickup times, no-show policy, rider expectations

3. EMERGENCY PREPAREDNESS
   - Heat illness prevention plan (required in most ag states)
   - Emergency contact system: how to reach all members quickly
   - Nearest hospitals and clinics to each work site
   - Workers' comp injury reporting procedures
   - Wildfire/natural disaster evacuation plan for housing sites
   - Template: emergency information card for each member (wallet-sized, bilingual)


5. Training & Workforce Development

# Farmworker Co-op Training Tracker
# Update quarterly, paste into Claude

training_program = {
    "co_op": "[Your Farmworker Co-op Name]",
    "total_members": 65,
    "training_budget_annual": 12000,
    "required_training": {
        "pesticide_safety_wps": {
            "description": "EPA Worker Protection Standard",
            "frequency": "annual",
            "members_current": 58,
            "members_due": 7,
            "cost_per_person": 0,  # provided by employer/extension
            "provider": "[county extension / employer / co-op trainer]"
        },
        "heat_illness_prevention": {
            "frequency": "annual",
            "members_current": 52,
            "members_due": 13,
            "cost_per_person": 0
        },
        "sexual_harassment_prevention": {
            "frequency": "[per state law]",
            "members_current": 48,
            "members_due": 17,
            "cost_per_person": 0
        },
        "first_aid_cpr": {
            "frequency": "every 2 years",
            "members_current": 22,
            "target": 30,
            "cost_per_person": 45
        }
    },
    "skill_development": {
        "forklift_certification": {"members_certified": 8, "target": 15, "cost": 150},
        "cdl_training": {"members_with_cdl": 3, "in_training": 2, "cost": 3500},
        "pesticide_applicator_license": {"members_licensed": 4, "target": 8, "cost": 200},
        "irrigation_technology": {"members_trained": 6, "target": 12, "cost": 0},
        "equipment_operation": {"members_trained": 18, "target": 30, "cost": 100},
        "pruning_grafting_specialist": {"members_certified": 10, "target": 20, "cost": 75}
    },
    "leadership_development": {
        "crew_leader_training": {"members_completed": 6, "target": 12},
        "cooperative_governance": {"members_completed": 15},
        "financial_literacy": {"members_completed": 22},
        "english_language_classes": {"members_enrolled": 18, "provider": "[community college / literacy council]"},
        "know_your_rights_workshop": {"members_attended": 45}
    }
}

# Ask Claude:
# 1. Flag all overdue required training and build a catch-up schedule for the next 60 days
# 2. Which skill certifications give our members the biggest pay bump? Prioritize training investments by ROI
# 3. CDL training costs $3,500 per person — model the revenue increase from having 5 CDL drivers (contract hauling)
# 4. Build an annual training calendar that doesn't conflict with peak harvest periods
# 5. Draft a training reimbursement policy: co-op pays for certification, member commits to [X] months of service
# 6. 17 members need harassment prevention training — schedule it and draft the attendance requirement notice
# 7. Create a skills matrix showing what each member is certified for — helps with crew assignment
# 8. Grant opportunity: workforce development funds for agricultural training — draft the application narrative


6. Member Rights & Cooperative Governance

Help me build a strong democratic governance structure for our farmworker co-op.

Co-op details:
- Name: [co-op name]
- Incorporated in: [state]
- Members: [number]
- Languages spoken: [list — e.g., Spanish, Mixteco, Haitian Creole, English]
- Governance structure: [board of directors elected by members / general assembly]
- How long in operation: [years]

Help me with:

1. BYLAWS & GOVERNANCE DOCUMENTS
   Draft or review our bylaws covering:
   - Membership: who can join, equity buy-in (if any), process for admission
   - Voting: one member one vote, quorum requirements, proxy voting rules
   - Board of directors: number, terms, election process, officer roles
   - Meetings: annual meeting, regular meetings, special meetings, notice requirements
   - Finances: fiscal year, audit requirements, surplus distribution, reserve funds
   - Amendments: process for changing bylaws
   - Dissolution: what happens to assets if the co-op closes

   ALL governance documents must be available in [languages spoken by members].

2. MEMBER RIGHTS HANDBOOK
   Create a bilingual handbook covering:
   - Your rights as a co-op member (voting, information access, surplus sharing)
   - Your rights as a worker (wages, safety, discrimination, retaliation)
   - How to file a grievance within the co-op
   - How to report wage theft or unsafe conditions to state/federal agencies
   - Workers' compensation: what it covers, how to file a claim
   - Immigration rights at work: what ICE can and cannot do at a worksite
   - Know your rights during a labor dispute
   - Legal aid resources: [local legal services organizations]
   - Emergency numbers: labor board, OSHA, legal aid, domestic violence hotline

3. DEMOCRATIC DECISION-MAKING
   We need to make a decision about [topic: rate negotiation strategy / new contract / equipment purchase / bylaw change].
   - Draft a proposal in plain language (bilingual)
   - Create a discussion guide for the membership meeting
   - Build a ballot template for formal votes
   - Draft meeting minutes template that records decisions, vote counts, and dissenting views
   - Ensure non-English-speaking members can fully participate: translation, visual aids, oral discussion

4. ANNUAL MEETING PLANNING
   Plan our annual membership meeting:
   - Agenda: board elections, financial report, year in review, upcoming season, open discussion
   - Financial summary in plain language and visual format (charts, not spreadsheets)
   - Board candidate statements (bilingual)
   - Childcare arrangements during the meeting
   - Food and community building
   - Transportation to meeting location
   - Draft all materials in [languages]

5. CONFLICT RESOLUTION
   When disputes arise between members, or between members and the co-op:
   - Draft a grievance procedure: informal conversation → mediation → formal hearing → appeal
   - Template for filing a written grievance
   - Mediator selection process (neutral, trusted by both parties)
   - When to involve outside support: legal aid, co-op development organizations
   - Emphasis: resolve disputes without anyone feeling silenced or punished


How to Use Any of These
1. Go to claude.ai
2. Copy any template above
3. Replace the [brackets] with your real information
4. Hit enter
5. Claude gives you a ready-to-use result
6. Modify, ask follow-ups, refine

No app to install. No training required. No data leaves your conversation.

Built for farmworker co-ops. By the workers, for the workers. Pass it on.
