Montessori School Co-op Plug-ins
1. Enrollment & Waitlist Manager

# Montessori School Enrollment Tracker

classrooms = {
    "infant": {
        "age_range": "6 weeks - 18 months",
        "capacity": 8,
        "current_enrolled": 8,
        "staff_ratio_required": "1:4",
        "current_staff": 2,
        "monthly_tuition": 1400,
        "waitlist": [
            {"name": "[Child A]", "dob": "2025-08-15", "applied": "2025-12-01", "siblings_enrolled": True},
            {"name": "[Child B]", "dob": "2025-06-22", "applied": "2026-01-10", "siblings_enrolled": False},
            {"name": "[Child C]", "dob": "2025-09-03", "applied": "2026-01-15", "siblings_enrolled": False},
        ]
    },
    "toddler": {
        "age_range": "18 months - 3 years",
        "capacity": 12,
        "current_enrolled": 11,
        "staff_ratio_required": "1:6",
        "current_staff": 2,
        "monthly_tuition": 1200,
        "waitlist": []
    },
    "primary": {
        "age_range": "3-6 years",
        "capacity": 24,
        "current_enrolled": 22,
        "staff_ratio_required": "1:10",
        "current_staff": 3,  # lead guide + 2 assistants
        "monthly_tuition": 950,
        "waitlist": [
            {"name": "[Child D]", "dob": "2023-03-10", "applied": "2026-02-01", "siblings_enrolled": True},
        ]
    },
    "elementary": {
        "age_range": "6-9 years",
        "capacity": 20,
        "current_enrolled": 16,
        "staff_ratio_required": "1:10",
        "current_staff": 2,
        "monthly_tuition": 850,
        "waitlist": []
    }
}

# Ask Claude:
# 1. Project when each classroom reaches capacity based on aging-up patterns
# 2. Which waitlist families should get first offers based on policy (siblings first, then date)?
# 3. If infant room loses 2 kids aging up in June, when do we offer waitlist spots?
# 4. Calculate monthly revenue per classroom and total
# 5. Are we in compliance with staff ratios if one teacher calls in sick per room?
# 6. Draft waitlist status update letters — warm, personal, Montessori-aligned tone


2. Curriculum Documentation & Parent Communication

I'm a Montessori guide in a [age level] classroom. 

Help me with:

1. Weekly parent newsletter that describes what we explored this week
   without using traditional school language. Use Montessori terminology
   naturally: "work" not "play," "guide" not "teacher," 
   "prepared environment" not "classroom setup."
   
   This week we focused on:
   - [Practical life: specific activities]
   - [Sensorial: specific materials used]
   - [Language: specific work]
   - [Math: specific materials]
   - [Cultural: specific topics — geography, science, nature]
   - [Outdoor observations or nature walks]

2. Individual child observation note for [child's name]:
   - What work they chose independently this week
   - Social interactions observed
   - New skills emerging
   - Areas of deep concentration noted
   - Suggested follow-up materials to introduce
   
   Format: Warm, specific, strengths-based. Parents should feel like 
   you truly see their child.

3. Upcoming parent education night outline on [topic]:
   Topics could include: "Why we don't use grades," 
   "Understanding the three-year cycle," "Montessori at home,"
   "The role of practical life," "Why your child 'just plays' 
   (and why that's everything)"


3. Budget & Tuition Modeler

# Montessori School Financial Planner

revenue = {
    "tuition_monthly": {
        "infant": {"enrolled": 8, "rate": 1400},
        "toddler": {"enrolled": 11, "rate": 1200},
        "primary": {"enrolled": 22, "rate": 950},
        "elementary": {"enrolled": 16, "rate": 850}
    },
    "enrollment_fee_annual": 250,  # per family
    "total_families": 48,
    "fundraising_annual": 15000,
    "grant_income_annual": 8000
}

expenses_monthly = {
    "staff_salaries": {
        "lead_guides": {"count": 4, "avg_monthly": 3800},
        "assistants": {"count": 5, "avg_monthly": 2400},
        "admin": {"count": 1, "avg_monthly": 3200},
        "substitutes_budget": 1500
    },
    "benefits_total": 4200,
    "rent_or_mortgage": 5500,
    "utilities": 1200,
    "insurance": 1800,
    "materials_and_supplies": 800,
    "food_program": 1500,
    "maintenance": 600,
    "professional_development": 400
}

# Ask Claude:
# 1. Are we operating at surplus or deficit at current enrollment?
# 2. What's our break-even enrollment per classroom?
# 3. If we raise tuition 5%, how many families can we afford to lose and still break even?
# 4. Model adding a second elementary classroom: startup cost vs revenue timeline
# 5. Draft a transparent budget summary for our parent board meeting
# 6. Compare our tuition to regional Montessori schools — are we priced right?
# 7. If we lose 3 families over summer, which classroom hits crisis first?


4. Licensing & Compliance Tracker


Our Montessori school is in [state]. Help me stay on top of licensing.

Current status:
- License type: [state license type]
- Last inspection: [date]
- Next renewal: [date]
- Any citations from last inspection: [list or "none"]
- Accreditation: [AMS / AMI / state only]

Generate:
1. Complete compliance checklist for [state] childcare licensing requirements
2. Staff credential tracking sheet:
   - Each staff member, their role, certifications, expiration dates
   - CPR/First Aid renewal dates
   - Background check renewal dates  
   - Professional development hours completed vs required
3. Health and safety monthly walkthrough checklist (printable)
4. Emergency drill log template (fire, tornado, lockdown) with required frequency
5. Immunization record tracking system for all enrolled children
6. Draft parent handbook section on our licensing, ratios, and safety policies

Make everything printable and inspector-ready.


5. Community Integration & Outreach

Our Montessori school is part of a co-op network that includes 
[food co-op name], [electric co-op name], and local farms.

Help us strengthen those connections:

1. Design a "farm to school" program outline:
   - Weekly produce delivery from [co-op/farm name]
   - Curriculum connections: where food comes from, seasons, soil
   - Monthly farm visit schedule
   - Cooking/practical life activities using seasonal ingredients
   - Budget estimate for local sourcing vs conventional supplier

2. Draft a partnership proposal to [food co-op name]:
   - Discounted produce for school lunch program
   - Student visits to co-op (field trips)
   - Co-op members get enrollment priority or discount
   - Joint community events (harvest festival, earth day, seed starts)
   - Mutual promotion in newsletters

3. Plan an open house that showcases the Montessori-co-op connection:
   - Tour stations showing how the prepared environment works
   - Local food tasting from partner farms/co-ops
   - Children demonstrating practical life work
   - Parent testimonials
   - Enrollment information
   - Timeline, supply list, promotional materials

4. Summer program concept:
   - Nature-based Montessori camp
   - Partnership with [local nature area/reserve]
   - Farm apprenticeship days for elementary children
   - Community garden project
   - Keep it affordable — co-op member rates


6. Staff Retention & Development

Montessori teacher retention is a crisis nationwide. Help our school 
build a plan to keep our guides.

Current staff situation:
- Lead guides: [number], average tenure: [years], average salary: [amount]
- Assistants: [number], average tenure: [years], average salary: [amount]
- Turnover last 2 years: [number left / reasons if known]
- Local competing schools: [names and approximate salary ranges if known]
- Our budget flexibility: [honest assessment]

Generate:
1. Compensation analysis: where do we stand vs regional averages?
2. Non-salary retention strategies that actually work:
   - Professional development funding
   - Montessori certification sponsorship (with service commitment)
   - Schedule flexibility
   - Decision-making authority
   - Classroom material budgets
3. Exit interview template — what to ask departing staff
4. Annual satisfaction survey for current staff
5. Draft a "why teach here" recruitment posting that's honest and compelling
6. 3-year staffing stability plan with budget implications


Connecting the Three: Cross-Co-op Integration

Map the connections between our electrical co-op, grain elevator, 
and Montessori school:

                    Vernon Electric Co-op
                   /                      \
          powers facility            powers facility
                 /                          \
    Grain Elevator Co-op  ←—supplies——→  Food Co-op
              |                              |
       farmer members                  feeds families
              |                              |
         their kids  ———enroll in———→  Montessori School
              |                              |
      co-op dividends ——fund tuition——→  affordable access

Ask Claude:
1. Map all resource flows between these co-ops
2. Where can we create mutual benefit agreements?
3. What shared services could reduce costs for all three?
   (Bookkeeping? Insurance pooling? Bulk purchasing? Shared newsletter?)
4. Draft a "co-op network" one-pager showing how membership in one 
   strengthens all
5. Model economic impact: $1 spent at the food co-op — how much 
   stays in the local economy through this network?


Three co-ops. One ecosystem. Every connection makes the whole thing stronger.
Pass it on.
