Rural Electric Co-op Plug-ins
1. Outage Management & Restoration Tracker

# Rural Electric Co-op Outage Dashboard
# Update during storm events, paste into Claude

outage_event = {
    "co_op": "[Your Electric Co-op Name]",
    "event_date": "2026-07-15",
    "event_type": "[storm / equipment failure / vehicle hit pole / wildlife / planned maintenance]",
    "weather_conditions": "severe thunderstorm, 60mph gusts, heavy rain",
    "affected_area": {
        "substations_out": ["[Substation A]", "[Substation B]"],
        "feeders_affected": ["[Feeder 12]", "[Feeder 15]", "[Feeder 22]"],
        "meters_without_power": 1847,
        "total_meters_served": 12500,
        "estimated_members_affected": 1650,
        "critical_accounts_affected": {
            "hospitals_clinics": 0,
            "nursing_homes": 1,
            "water_treatment": 1,
            "schools": 2,
            "fire_stations": 1,
            "cell_towers": 3,
            "grain_dryers_seasonal": 8
        }
    },
    "crew_status": {
        "in_house_crews": 4,
        "linemen_per_crew": 2,
        "mutual_aid_crews_requested": 3,
        "mutual_aid_arriving": "2026-07-15 14:00",
        "tree_crews_available": 2,
        "bucket_trucks_operational": 5,
        "digger_trucks_operational": 2
    },
    "damage_assessment": {
        "poles_broken": 12,
        "poles_leaning": 8,
        "crossarms_damaged": 22,
        "spans_of_wire_down": 15,
        "transformers_damaged": 6,
        "trees_on_lines": 34,
        "roads_blocked": 4
    },
    "inventory": {
        "poles_in_yard": 45,
        "crossarms_in_stock": 80,
        "transformers_25kva": 8,
        "transformers_50kva": 4,
        "wire_feet_available": 12000
    }
}

# Ask Claude:
# 1. Prioritize restoration: which feeders restore power to the most members per crew-hour?
# 2. Critical accounts first — map the fastest path to restore the nursing home and water treatment plant
# 3. Do we have enough materials in stock, or do we need an emergency order? What's short?
# 4. Build a crew dispatch plan: who goes where, in what order, with what equipment
# 5. Estimate restoration timeline by area — when can we tell members to expect power back?
# 6. Draft member notifications: automated phone/text for affected areas with estimated restoration times
# 7. After event: compile an outage report for the board with total cost, member-hours without power, and lessons learned


2. Load Forecasting & Demand Management

# Rural Electric Load Analysis
# Update monthly, paste into Claude for trend analysis

load_data = {
    "co_op": "[Your Electric Co-op Name]",
    "month": "[month year]",
    "system_stats": {
        "total_meters": 12500,
        "residential_meters": 10800,
        "commercial_meters": 1200,
        "industrial_meters": 85,
        "irrigation_meters": 415,
        "miles_of_line": 3200,
        "substations": 8,
        "system_peak_kw": 42000,
        "system_peak_date": "2026-07-22",
        "system_peak_hour": "15:00",
        "transformer_capacity_kw": 58000,
        "reserve_margin_percent": 38.1
    },
    "monthly_energy": {
        "kwh_purchased": 14200000,
        "kwh_sold": 12900000,
        "line_loss_percent": 9.15,
        "wholesale_cost_per_kwh": 0.062,
        "avg_retail_rate_per_kwh": 0.118,
        "revenue_this_month": 1522200,
        "power_cost_this_month": 880400
    },
    "seasonal_peaks": {
        "summer_peak_kw": 42000,
        "winter_peak_kw": 38500,
        "spring_shoulder_avg_kw": 22000,
        "fall_shoulder_avg_kw": 24000
    },
    "demand_response_programs": {
        "load_control_water_heaters": 2200,
        "load_control_hvac": 850,
        "interruptible_irrigation": 180,
        "peak_shaving_capacity_kw": 4800,
        "events_triggered_ytd": 6,
        "avg_reduction_per_event_kw": 3200
    }
}

wholesale_rate_structure = {
    "generation_cooperative": "[Your G&T Co-op Name]",
    "demand_charge_per_kw": 12.50,
    "energy_charge_per_kwh": 0.042,
    "transmission_charge_per_kw": 3.80,
    "coincident_peak_factor": True,  # billed on contribution to G&T system peak
    "monthly_minimum": 85000
}

# Ask Claude:
# 1. Where is our coincident peak likely to land this summer? What's the cost impact of each kW we can shave?
# 2. Line losses at 9.15% — is that normal for a system our size? Where should we investigate?
# 3. Model the impact of 200 new heat pumps on our winter peak — do we have capacity?
# 4. If wholesale rates increase 8% next year, what retail rate adjustment keeps us whole?
# 5. Rank our demand response programs by cost-effectiveness ($/kW avoided)
# 6. Build a one-page load forecast summary for the board showing 3-year trends and projections
# 7. Identify the top 10 commercial accounts driving our peak — would time-of-use rates help?


3. Right-of-Way & Vegetation Management

# Vegetation Management Planner
# Update annually, paste into Claude

vegetation_program = {
    "co_op": "[Your Electric Co-op Name]",
    "total_miles_of_line": 3200,
    "miles_requiring_tree_trimming": 1800,
    "cycle_target_years": 4,
    "miles_to_trim_annually": 450,
    "miles_completed_ytd": 280,
    "budget_annual": 680000,
    "spent_ytd": 425000,
    "contractors": [
        {"name": "[Tree Service A]", "rate_per_mile": 1400, "crews": 2, "quality_rating": "excellent"},
        {"name": "[Tree Service B]", "rate_per_mile": 1250, "crews": 1, "quality_rating": "good"},
        {"name": "[In-house crew]", "rate_per_mile": 1100, "crews": 1, "quality_rating": "good"}
    ],
    "problem_areas": [
        {"location": "[Road/Section name]", "miles": 12, "issue": "fast-growing silver maples, 2-year regrowth", "priority": "high"},
        {"location": "[Road/Section name]", "miles": 8, "issue": "member refuses access, certified letter sent [date]", "priority": "high"},
        {"location": "[Road/Section name]", "miles": 25, "issue": "mature hardwoods encroaching, some within 5ft of conductor", "priority": "critical"}
    ],
    "outages_tree_related_ytd": 28,
    "outages_total_ytd": 67,
    "tree_related_outage_percent": 41.8
}

# Ask Claude:
# 1. At current pace, will we finish our annual target? If not, how many additional crew-miles do we need?
# 2. 42% of our outages are tree-related — rank problem areas by outage frequency and prioritize them
# 3. Budget check: can we finish the year within budget, or do we need a supplemental request to the board?
# 4. Draft a member notification letter for the access-refusal situation — firm but professional
# 5. Build a 4-year rotation map: which miles get trimmed which year to stay on cycle
# 6. Compare contractor rates — at what volume does it make sense to add a second in-house crew?
# 7. Draft an RFP for tree trimming services for next year's program


4. Capital Credits & Member Equity

# Capital Credits Tracker
# Update annually before retirement decisions, paste into Claude

capital_credits = {
    "co_op": "[Your Electric Co-op Name]",
    "total_patronage_capital": 18500000,
    "allocation_method": "[per-kWh / revenue-based / margins-based]",
    "current_year_margins": 425000,
    "margins_allocated_to_members": 425000,
    "retirement_policy": "[FIFO / percentage of oldest year / board discretion]",
    "years_allocated_not_retired": {
        "2005": 380000,
        "2006": 395000,
        "2007": 410000,
        "2008": 285000,
        "2009": 310000,
        "2010": 340000,
        "2011": 365000,
        "2012": 390000,
        "2013": 420000,
        "2014": 445000,
        "2015": 460000,
        "2016": 480000,
        "2017": 510000,
        "2018": 525000,
        "2019": 540000,
        "2020": 390000,
        "2021": 520000,
        "2022": 485000,
        "2023": 450000,
        "2024": 410000,
        "2025": 425000
    },
    "estate_retirements_ytd": 145000,
    "general_retirements_last_year": 380000,
    "total_retired_all_time": 8200000,
    "equity_ratio_percent": 42.0,
    "minimum_equity_target_percent": 40.0,
    "rus_required_minimum_percent": 30.0,
    "members_with_unretired_credits": 14200,
    "former_members_with_credits": 3800
}

# Ask Claude:
# 1. If we retire the oldest year (2005), what's the impact on our equity ratio?
# 2. Can we afford to retire 2 years of credits and still stay above our 40% equity target?
# 3. How much does the average active member have in unretired capital credits?
# 4. Draft the annual capital credit notice letter explaining allocations and any retirements
# 5. Model a 20-year retirement schedule that balances member returns with system financial health
# 6. Estate retirements are $145K — is that trending up? What should we budget for next year?
# 7. Build a one-page explainer for new members: "What are capital credits and why do they matter?"
# 8. Compare our rotation cycle to peer co-ops — are we retiring fast enough to keep members engaged?


5. Rate Design & Cost-of-Service

# Rate Study Worksheet
# Paste into Claude when preparing for rate cases

rate_data = {
    "co_op": "[Your Electric Co-op Name]",
    "current_rates": {
        "residential": {
            "facility_charge_monthly": 32.00,
            "energy_charge_per_kwh": 0.118,
            "avg_monthly_bill_1000kwh": 150.00,
            "avg_monthly_usage_kwh": 1150
        },
        "small_commercial": {
            "facility_charge_monthly": 45.00,
            "energy_charge_per_kwh": 0.112,
            "demand_charge_per_kw": 0,
            "avg_monthly_bill": 285.00
        },
        "large_commercial": {
            "facility_charge_monthly": 75.00,
            "energy_charge_per_kwh": 0.095,
            "demand_charge_per_kw": 8.50,
            "avg_monthly_bill": 1850.00
        },
        "irrigation": {
            "facility_charge_monthly": 25.00,
            "energy_charge_per_kwh": 0.098,
            "seasonal": True,
            "months_active": "[May-September]"
        }
    },
    "cost_of_service": {
        "total_revenue_requirement": 18500000,
        "power_cost_percent": 58,
        "distribution_cost_percent": 22,
        "customer_service_percent": 8,
        "admin_general_percent": 7,
        "depreciation_percent": 5
    },
    "revenue_by_class": {
        "residential": {"percent_of_revenue": 62, "percent_of_cost": 65},
        "small_commercial": {"percent_of_revenue": 18, "percent_of_cost": 16},
        "large_commercial": {"percent_of_revenue": 14, "percent_of_cost": 13},
        "irrigation": {"percent_of_revenue": 6, "percent_of_cost": 6}
    },
    "proposed_increase_percent": 5.5,
    "last_rate_increase": "[date]",
    "last_increase_percent": 4.2
}

# Ask Claude:
# 1. Residential is paying 62% of revenue but causing 65% of cost — how do we close that gap fairly?
# 2. Design 3 rate increase options: (a) across-the-board, (b) facility charge increase, (c) restructured tiers
# 3. Model the bill impact of each option on a member using 500, 1000, and 2000 kWh/month
# 4. Draft the member notice for a 5.5% rate increase — transparent, empathetic, no corporate-speak
# 5. Build a board presentation showing why the increase is necessary with cost-of-service data
# 6. Compare our rates to neighboring co-ops and IOUs — where do we stand?
# 7. Should we add a demand charge for residential? Model the impact on high-use vs low-use members
# 8. Draft FAQ answers for the top 10 questions members will ask about a rate increase


6. Renewable Energy & Distributed Generation

# Distributed Generation Tracker
# Update quarterly, paste into Claude

distributed_generation = {
    "co_op": "[Your Electric Co-op Name]",
    "interconnection_policy": "[net metering / net billing / buy-all-sell-all / avoided cost]",
    "state_net_metering_cap": "[percentage or MW cap, or 'no state mandate']",
    "member_solar_installations": {
        "total_systems": 85,
        "total_capacity_kw": 680,
        "avg_system_size_kw": 8.0,
        "applications_pending": 12,
        "applications_denied_ytd": 1,
        "annual_generation_kwh_est": 850000,
        "percent_of_total_sales": 0.66
    },
    "community_solar": {
        "program_exists": "[yes/no]",
        "total_capacity_kw": 500,
        "subscribers": 120,
        "subscription_rate_per_kw_month": 8.50,
        "wait_list": 45,
        "annual_revenue": 51000,
        "annual_generation_kwh": 625000,
        "panels_remaining": 80
    },
    "battery_storage": {
        "utility_scale_projects": 0,
        "member_batteries_known": 8,
        "total_member_battery_kwh": 108
    },
    "ev_charging": {
        "public_stations_in_territory": 2,
        "ev_registrations_in_territory": 45,
        "ev_rate_available": "[yes/no]",
        "estimated_annual_ev_load_kwh": 135000
    },
    "cost_shift_analysis": {
        "solar_member_avg_bill_reduction": 68,  # percent
        "fixed_cost_not_recovered_per_solar_member_annually": 285,
        "total_annual_cost_shift_to_non_solar": 24225
    }
}

# Ask Claude:
# 1. Is our interconnection policy keeping up with demand? Model what happens at 200 solar systems
# 2. Cost shift analysis: are non-solar members subsidizing solar members? By how much per year?
# 3. Should we restructure rates to reduce the cost shift? Options and bill impact for both groups
# 4. Community solar waitlist is 45 — build a business case for expanding the program
# 5. Draft a member-facing FAQ: "Can I put solar on my home?" covering our interconnection process
# 6. Model the grid impact of 200 EVs in our territory — do we need infrastructure upgrades?
# 7. Compare our net metering policy to neighboring utilities — are we competitive?
# 8. Draft a board memo on our distributed generation strategy for the next 5 years


How to Use Any of These
1. Go to claude.ai
2. Copy any template above
3. Replace the [brackets] with your real information
4. Hit enter
5. Claude gives you a ready-to-use result
6. Modify, ask follow-ups, refine

No app to install. No training required. No data leaves your conversation.

Built for rural electric co-ops. Built to be shared. Pass it on.
