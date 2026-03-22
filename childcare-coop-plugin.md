Childcare Co-op Plug-ins
1. Enrollment & Waitlist Management

# Childcare Co-op Enrollment Dashboard
# Update monthly, paste into Claude

enrollment = {
    "co_op": "[Your Childcare Co-op Name]",
    "date": "[date]",
    "license_type": "[family childcare / center-based / school-age]",
    "licensed_capacity": 48,
    "classrooms": {
        "infants": {
            "age_range": "6 weeks - 12 months",
            "capacity": 8,
            "enrolled": 8,
            "staff_required_ratio": "1:4",
            "staff_assigned": 2,
            "monthly_tuition": 1450,
            "openings_expected_next_90_days": 2,
            "reason": "aging up to toddler room"
        },
        "toddlers": {
            "age_range": "12 - 24 months",
            "capacity": 10,
            "enrolled": 9,
            "staff_required_ratio": "1:5",
            "staff_assigned": 2,
            "monthly_tuition": 1300,
            "openings_expected_next_90_days": 1
        },
        "twos": {
            "age_range": "24 - 36 months",
            "capacity": 12,
            "enrolled": 12,
            "staff_required_ratio": "1:6",
            "staff_assigned": 2,
            "monthly_tuition": 1200,
            "openings_expected_next_90_days": 3,
            "reason": "moving to preschool room in fall"
        },
        "preschool": {
            "age_range": "3 - 5 years",
            "capacity": 18,
            "enrolled": 16,
            "staff_required_ratio": "1:9",
            "staff_assigned": 2,
            "monthly_tuition": 1050,
            "openings_expected_next_90_days": 0
        }
    },
    "waitlist": {
        "infants": 14,
        "toddlers": 8,
        "twos": 5,
        "preschool": 3,
        "total": 30,
        "avg_wait_time_months": 9,
        "longest_wait_months": 18
    },
    "subsidy_families": {
        "receiving_state_subsidy": 8,
        "subsidy_rate_vs_tuition_gap": 185,  # monthly shortfall per subsidized child
        "subsidy_reimbursement_delay_days": 45
    },
    "parent_participation": {
        "volunteer_hours_required_monthly": 4,
        "avg_hours_contributed": 3.2,
        "families_below_requirement": 6,
        "committee_roles_filled": 12,
        "committee_roles_total": 15
    }
}

# Ask Claude:
# 1. With 30 on the waitlist and projected openings, build an offer schedule for the next 6 months
# 2. Infant room is always full with 14 waiting — model the revenue case for expanding by 4 spots (need 1 more staff)
# 3. Subsidy gap is $185/child/month — total annual shortfall? Options to close the gap without raising tuition
# 4. 6 families below volunteer hours — draft a friendly reminder that explains why co-op participation matters
# 5. Staff ratios: are we one sick call away from being out of compliance in any room?
# 6. Project enrollment and revenue for the next 12 months accounting for age-ups and graduations
# 7. Draft waitlist offer letters with enrollment packets and deadline to accept


2. Parent Scheduling & Volunteer Coordination

Help me coordinate parent participation in our childcare co-op.

Co-op details:
- Name: [co-op name]
- Type: [parent participation required / volunteer-supplemented / fully staffed with parent board]
- Families: [number]
- Parent hours required: [hours per month/week per family]
- Operating hours: [hours]
- Days open: [Monday-Friday / other]

Help me with:

1. VOLUNTEER SCHEDULE BUILDER
   We need parents to cover:
   - Classroom assistance: [hours/day needed, which rooms]
   - Meal prep and cleanup: [breakfast / lunch / snack times]
   - Playground supervision: [times]
   - Laundry and cleaning: [frequency]
   - Field trip drivers: [frequency]
   - Committee work: [finance / enrollment / facilities / fundraising / hiring]

   Build a monthly schedule template that:
   - Distributes shifts fairly across all families
   - Accounts for working parents (evening/weekend options for non-classroom hours)
   - Tracks hours automatically
   - Flags families falling behind on commitments
   - Allows shift swaps between families

2. PARENT COMMUNICATION
   Draft:
   - Weekly classroom update email from teachers to parents
   - Monthly co-op newsletter with operational updates, upcoming events, volunteer recognition
   - Gentle reminder for families behind on volunteer hours
   - Annual meeting notice with election of board officers and budget review
   - Snow day / closure notification template
   - Tuition increase announcement — empathetic, transparent about costs

3. NEW FAMILY ORIENTATION
   Create an orientation packet covering:
   - How our co-op works (governance, parent roles, decision-making)
   - Volunteer expectations and scheduling process
   - Tuition and fee structure
   - Daily routine and what to pack
   - Illness policy and pickup requirements
   - Emergency procedures
   - How to raise concerns (who to talk to, grievance process)
   - Why we're a co-op, not just a daycare — the philosophy matters


3. Budget & Tuition Modeling

# Childcare Co-op Financial Model
# Update monthly, paste into Claude

financials = {
    "co_op": "[Your Childcare Co-op Name]",
    "fiscal_year": "[year]",
    "month": "[month]",
    "revenue": {
        "tuition_collected": 42500,
        "tuition_outstanding": 3200,
        "state_subsidy_payments": 6800,
        "subsidy_pending": 2400,
        "fundraising_ytd": 8500,
        "grants_received_ytd": 15000,
        "registration_fees": 600,
        "late_pickup_fees": 150,
        "total_monthly_revenue": 50050
    },
    "expenses": {
        "staff_wages": 28000,
        "payroll_taxes_benefits": 7000,
        "substitute_teachers": 1200,
        "rent_mortgage": 4500,
        "utilities": 850,
        "insurance_liability": 1200,
        "insurance_workers_comp": 600,
        "food_program": 2800,
        "supplies_classroom": 600,
        "supplies_cleaning": 250,
        "curriculum_materials": 200,
        "maintenance_repairs": 400,
        "licensing_fees": 50,
        "accounting_bookkeeping": 350,
        "total_monthly_expenses": 48000
    },
    "net_monthly": 2050,
    "operating_reserve": 24000,
    "months_of_reserve": 0.5,
    "target_months_reserve": 3,
    "enrollment_break_even": 42,  # children needed at current tuition to cover costs
    "current_enrollment": 45
}

staff_compensation = {
    "lead_teachers": {"count": 4, "avg_hourly": 16.50, "market_rate": 18.00, "turnover_last_year": 1},
    "assistant_teachers": {"count": 4, "avg_hourly": 13.50, "market_rate": 14.50, "turnover_last_year": 2},
    "director": {"count": 1, "salary": 45000, "market_rate": 52000},
    "cook": {"count": 1, "avg_hourly": 14.00, "hours_per_week": 30},
    "benefits_offered": "[health insurance / PTO days / professional development stipend / none]"
}

# Ask Claude:
# 1. We have 0.5 months of reserves — build a 12-month plan to reach 3 months without raising tuition more than 5%
# 2. Staff wages are below market — model the cost of matching market rates and how much tuition increases to cover it
# 3. We're 3 kids above break-even — what happens if 2 families leave? How fast does the budget collapse?
# 4. Subsidy reimbursement is 45 days delayed — calculate the cash flow impact and options (line of credit? reserve draw?)
# 5. Build a tuition increase scenario: 3%, 5%, 8% — impact on each family and risk of losing enrollments
# 6. Draft the annual budget for board approval with line-item justifications
# 7. What grants are available for childcare co-ops in [state]? USDA CACFP, state quality grants, local foundations?
# 8. Model adding a before/after school program: revenue potential, staffing needs, licensing requirements


4. Licensing & Health/Safety Compliance

# Childcare Licensing Tracker
# Update quarterly, paste into Claude

licensing = {
    "co_op": "[Your Childcare Co-op Name]",
    "state": "[state]",
    "license_number": "[number]",
    "license_type": "[center-based / family / school-age]",
    "license_expiration": "[date]",
    "licensed_capacity": 48,
    "licensing_agency": "[state department name]",
    "last_inspection": "[date]",
    "inspection_result": "[compliant / citations issued / corrective action plan]",
    "citations_open": [
        {"citation": "[describe if any]", "date_issued": "[date]", "corrective_deadline": "[date]", "status": "[corrected / in progress / overdue]"}
    ],
    "staff_requirements": {
        "background_checks": {
            "fbi_fingerprint": {"staff_current": 9, "staff_due_renewal": 1, "renewal_deadline": "[date]"},
            "state_criminal": {"staff_current": 9, "staff_due_renewal": 0},
            "child_abuse_registry": {"staff_current": 9, "staff_due_renewal": 1},
            "sex_offender_registry": {"staff_current": 9, "staff_due_renewal": 0}
        },
        "training_hours": {
            "annual_requirement_hours": 24,
            "avg_hours_completed_ytd": 16,
            "staff_behind_schedule": 2,
            "cpr_first_aid_current": 8,
            "cpr_first_aid_expiring_90_days": 2
        },
        "qualifications": {
            "cda_or_higher_required_percent": 50,
            "cda_or_higher_current_percent": 62.5,
            "director_qualification": "[CDA / AA / BA in ECE / state credential]"
        }
    },
    "health_safety": {
        "fire_inspection_current": "[yes/no]",
        "fire_inspection_date": "[date]",
        "fire_drills_completed_ytd": 8,
        "fire_drills_required_ytd": 8,
        "tornado_drills_completed_ytd": 2,
        "lockdown_drills_completed_ytd": 2,
        "health_inspection_current": "[yes/no]",
        "playground_inspection_date": "[date]",
        "lead_paint_test_date": "[date or N/A]",
        "radon_test_date": "[date or N/A]",
        "water_test_date": "[date if well water]"
    },
    "food_program": {
        "cacfp_enrolled": "[yes/no]",
        "cacfp_sponsor": "[sponsor name or self-sponsored]",
        "meals_served_daily": "[breakfast, lunch, snack]",
        "menu_reviewed_by": "[nutritionist / sponsor / self]",
        "last_cacfp_review": "[date]"
    }
}

# Ask Claude:
# 1. Flag every upcoming deadline in the next 90 days: renewals, training, background checks, inspections
# 2. Two staff are behind on training hours — build a catch-up plan with available workshop dates
# 3. Draft a complete licensing renewal checklist for our state — what do inspectors look for?
# 4. Create a monthly health and safety walk-through checklist (printable, one page)
# 5. Build a staff credential tracking spreadsheet template with renewal reminders
# 6. We got a citation for [issue] — draft the corrective action plan response
# 7. Are we meeting CACFP meal pattern requirements? Review our sample weekly menu
# 8. Draft emergency procedures manual: fire, tornado, lockdown, medical emergency, missing child
# NOTE: Always verify requirements with your state licensing agency. Regulations vary by state.


5. Staff Retention & Professional Development

Help me keep our childcare co-op staff from leaving for better-paying jobs.

Our situation:
- Co-op name: [name]
- Location: [city, state]
- Staff size: [number]
- Avg teacher pay: $[X]/hour
- Market rate in our area: $[X]/hour
- Turnover last year: [number of staff who left]
- Biggest competitor for our staff: [public schools / corporate centers / other co-ops / retail]
- Current benefits: [list what you offer]
- Annual professional development budget: $[amount]

Help me with:

1. COMPENSATION ANALYSIS
   We can't match public school pay, but we can compete on total value.
   - Calculate total compensation including benefits, PTO, professional development
   - Compare to competitors on total package, not just hourly rate
   - Identify low-cost, high-value benefits we could add:
     - Childcare discount for staff's own children
     - Flexible scheduling
     - Professional development stipends
     - Tuition reimbursement for ECE degrees
     - Mental health days
   - Draft a "total compensation statement" showing each staff member what their full package is worth

2. PROFESSIONAL DEVELOPMENT PLAN
   Build individual development tracks for:
   - Assistant teacher → Lead teacher (CDA pathway)
   - Lead teacher → Master teacher (BA pathway)
   - Teacher → Director track
   - Include: training resources, timeline, cost, how the co-op supports each step
   - Map to state quality rating system (QRIS) improvement goals

3. RETENTION STRATEGY
   Our [number] departures last year cost us:
   - Estimate the true cost per departure (recruitment, training, lost enrollment during transition)
   - Compare that cost to what a raise/benefit would have cost to keep them
   - Draft a stay interview template — ask current staff what keeps them and what might make them leave
   - Build a 12-month retention action plan

4. RECRUITMENT
   We need to hire [position].
   - Draft a job posting that highlights co-op culture, not just pay
   - List where to post: ECE programs, community boards, workforce agencies
   - Interview questions that assess fit with cooperative values
   - Onboarding checklist for new staff: licensing paperwork, training schedule, mentor assignment


6. Fundraising & Community Support

Help me raise money and build community support for our childcare co-op.

Co-op details:
- Name: [name]
- Location: [community]
- Families served: [number]
- Annual budget: $[amount]
- Fundraising goal: $[amount]
- What the funds are for: [scholarships / playground / staff raises / building repairs / expansion]

Help me with:

1. ANNUAL FUNDRAISING PLAN
   Design a 12-month fundraising calendar:
   - Fall: [back-to-school event / annual appeal letter]
   - Winter: [holiday auction / giving Tuesday / year-end campaign]
   - Spring: [plant sale / community dinner / fun run]
   - Summer: [enrollment drive / alumni event]
   For each event: estimated revenue, volunteer hours needed, planning timeline

2. GRANT APPLICATIONS
   We're applying to [foundation / government program / community fund] for:
   - Project: [describe — e.g., "scholarship fund for low-income families"]
   - Amount: $[amount]
   Draft:
   - Statement of need with local childcare data (desert stats, waitlist numbers, cost burden on families)
   - Program description and impact metrics
   - Budget narrative
   - Sustainability plan

3. ANNUAL APPEAL LETTER
   Draft a year-end fundraising letter to:
   - Current families: emphasize community investment, specific needs
   - Alumni families: nostalgia, legacy, "pay it forward"
   - Local businesses: partnership opportunity, visibility, tax deduction
   - Community members: childcare as infrastructure, workforce impact

4. EMPLOYER PARTNERSHIPS
   Local employers benefit when their workers have reliable childcare.
   - Draft a partnership proposal for [employer name]:
     - Reserved spots for employee children
     - Employer contributes to tuition subsidy
     - Co-op provides backup care days
     - Joint recruitment for staff positions
   - Model the ROI for the employer: reduced absenteeism, improved retention


How to Use Any of These
1. Go to claude.ai
2. Copy any template above
3. Replace the [brackets] with your real information
4. Hit enter
5. Claude gives you a ready-to-use result
6. Modify, ask follow-ups, refine

No app to install. No training required. No data leaves your conversation.

Built for childcare co-ops. Because the people who raise our kids deserve better tools. Pass it on.
