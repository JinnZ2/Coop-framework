Fishing Co-op Plug-ins
1. Catch Tracking & Quota Management

# Fishing Co-op Catch Dashboard
# Update daily during season, paste into Claude

daily_catch = {
    "co_op": "[Your Fishing Co-op Name]",
    "date": "2026-06-18",
    "port": "[home port]",
    "season": "[salmon / crab / halibut / groundfish / shrimp / lobster]",
    "fleet_status": {
        "active_vessels": 24,
        "total_member_vessels": 32,
        "vessels_in_port": 8,
        "vessels_in_drydock": 2
    },
    "catch_today": {
        "species_1": {
            "species": "[e.g., sockeye salmon]",
            "pounds_landed": 18500,
            "number_of_landings": 8,
            "avg_size_lbs": 6.2,
            "price_per_lb": 4.85,
            "grade_breakdown": {
                "premium": {"percent": 65, "price_per_lb": 5.50},
                "standard": {"percent": 30, "price_per_lb": 4.25},
                "utility": {"percent": 5, "price_per_lb": 2.10}
            }
        },
        "species_2": {
            "species": "[e.g., pink salmon]",
            "pounds_landed": 12200,
            "number_of_landings": 6,
            "avg_size_lbs": 4.1,
            "price_per_lb": 1.45,
            "grade_breakdown": {
                "premium": {"percent": 40, "price_per_lb": 1.85},
                "standard": {"percent": 50, "price_per_lb": 1.30},
                "utility": {"percent": 10, "price_per_lb": 0.65}
            }
        }
    },
    "season_totals": {
        "species_1_lbs_ytd": 485000,
        "species_1_quota_total": 750000,
        "species_1_quota_remaining": 265000,
        "species_2_lbs_ytd": 320000,
        "species_2_quota_total": "no cap",
        "bycatch_lbs_ytd": 8500,
        "bycatch_limit": 15000
    },
    "processing": {
        "plant_capacity_lbs_per_day": 40000,
        "processed_today": 28000,
        "cold_storage_capacity_lbs": 200000,
        "cold_storage_current_lbs": 145000,
        "cold_storage_available_lbs": 55000,
        "backlog_lbs_awaiting_processing": 18000
    }
}

# Ask Claude:
# 1. At current catch rate, how many days until we hit our quota? Should we slow the fleet down?
# 2. Bycatch is at 8,500 of 15,000 limit — project when we hit the cap and what that means for the season
# 3. Cold storage is 72.5% full — at current landing rate, when do we run out of space?
# 4. Compare today's grade breakdown to season average — is quality trending up or down?
# 5. Revenue per vessel today vs season average — who's outperforming and what are they doing differently?
# 6. Draft a fleet advisory: quota status, processing capacity, any changes to delivery schedule
# 7. Model the revenue impact if we shift 10% of catch from standard to premium grade through better handling


2. Direct-to-Consumer & Market Sales

# Fish Market & Sales Tracker
# Update weekly, paste into Claude

sales_channels = {
    "co_op": "[Your Fishing Co-op Name]",
    "week_ending": "[date]",
    "wholesale": {
        "buyers": [
            {"name": "[Buyer A — processor]", "species": "[salmon]", "lbs_shipped": 25000, "price_per_lb": 4.50, "payment_terms": "net 30"},
            {"name": "[Buyer B — distributor]", "species": "[salmon]", "lbs_shipped": 15000, "price_per_lb": 4.75, "payment_terms": "net 15"},
            {"name": "[Buyer C — export]", "species": "[salmon]", "lbs_shipped": 20000, "price_per_lb": 5.10, "payment_terms": "net 45"}
        ],
        "total_wholesale_revenue": 280000
    },
    "direct_to_consumer": {
        "farmers_market_sales": {
            "markets_attended": 3,
            "lbs_sold": 1200,
            "avg_price_per_lb": 14.50,
            "revenue": 17400
        },
        "csa_fish_shares": {
            "active_subscribers": 85,
            "share_price_monthly": 95,
            "lbs_per_share": 8,
            "monthly_revenue": 8075,
            "retention_rate_percent": 88,
            "waitlist": 22
        },
        "online_orders": {
            "orders_shipped": 45,
            "avg_order_value": 78,
            "shipping_cost_avg": 18,
            "revenue": 3510,
            "repeat_customer_percent": 62
        },
        "restaurant_direct": {
            "restaurant_accounts": 12,
            "lbs_delivered": 800,
            "avg_price_per_lb": 11.25,
            "revenue": 9000
        },
        "total_dtc_revenue": 37985
    },
    "inventory": {
        "fresh_on_hand_lbs": 4500,
        "frozen_in_storage_lbs": 85000,
        "smoked_finished_lbs": 1200,
        "value_added_products": [
            {"product": "[smoked salmon]", "lbs_available": 800, "price_per_lb": 22.00},
            {"product": "[salmon jerky]", "lbs_available": 200, "price_per_lb": 35.00},
            {"product": "[canned salmon]", "cases_available": 500, "price_per_case": 48.00}
        ]
    }
}

# Ask Claude:
# 1. Direct-to-consumer is $14.50/lb vs wholesale at $4.50/lb — model what happens if we shift 5% more volume to DTC
# 2. CSA has a waitlist of 22 — should we expand? What's the processing and logistics capacity needed?
# 3. Which sales channel gives us the best margin after shipping and handling costs?
# 4. Draft a seasonal CSA fish share marketing email for new subscriber recruitment
# 5. Restaurant accounts: which ones are growing, which are declining? Draft a re-engagement pitch
# 6. Build a pricing strategy for our value-added products — are we leaving money on the table?
# 7. Create a 12-month sales forecast by channel with seasonal adjustments


3. Cold Chain & Processing Logistics

# Cold Chain Management
# Update daily during peak season, paste into Claude

cold_chain = {
    "co_op": "[Your Fishing Co-op Name]",
    "date": "[date]",
    "dock_operations": {
        "offload_capacity_lbs_per_hour": 5000,
        "offload_crew_available": 6,
        "vessels_waiting_to_offload": 3,
        "estimated_total_lbs_waiting": 35000,
        "ice_supply_tons_available": 15,
        "ice_machine_capacity_tons_per_day": 8,
        "dock_temperature_f": 42
    },
    "processing_plant": {
        "lines_operational": 2,
        "lines_total": 3,
        "line_down_reason": "[maintenance / staffing / not needed]",
        "workers_on_shift": 18,
        "workers_needed_full_capacity": 26,
        "processing_rate_lbs_per_hour": 2500,
        "hours_remaining_today": 8,
        "capacity_remaining_today_lbs": 20000,
        "products_in_process": {
            "fresh_fillet": {"lbs": 8000, "yield_percent": 45},
            "headed_gutted": {"lbs": 12000, "yield_percent": 72},
            "whole_frozen": {"lbs": 5000, "yield_percent": 95}
        }
    },
    "cold_storage": {
        "blast_freezer_capacity_lbs": 10000,
        "blast_freezer_current_lbs": 7500,
        "blast_freezer_temp_f": -30,
        "cold_room_1": {"capacity_lbs": 100000, "current_lbs": 78000, "temp_f": 0},
        "cold_room_2": {"capacity_lbs": 100000, "current_lbs": 67000, "temp_f": 0},
        "refrigerated_truck_available": True,
        "next_shipment_date": "[date]",
        "next_shipment_destination": "[city/buyer]",
        "next_shipment_lbs": 25000
    },
    "quality_control": {
        "temp_checks_passed_today": 12,
        "temp_checks_failed_today": 0,
        "product_holds": 0,
        "last_health_inspection": "[date]",
        "haccp_plan_current": True
    }
}

# Ask Claude:
# 1. Three vessels waiting — build an offload priority schedule that minimizes wait time and quality degradation
# 2. We're 8 workers short of full capacity. At current staffing, what's our max throughput and backlog projection?
# 3. Cold storage is 72.5% across both rooms — when do we hit capacity? Should we schedule an early shipment?
# 4. Blast freezer is 75% full — prioritize what goes in next based on product value and shelf life
# 5. Build a daily processing schedule: what gets filleted, what gets frozen whole, what ships fresh
# 6. Calculate our yield rates — are we losing product in processing? Compare to industry benchmarks
# 7. Draft a HACCP monitoring log template for our processing line


4. Vessel Maintenance & Fleet Coordination

Help me manage our fishing co-op fleet operations.

Co-op details:
- Name: [co-op name]
- Fleet size: [number] member vessels
- Vessel types: [seiner / troller / gillnetter / longliner / trawler / pot boat]
- Home port: [port]
- Fishing grounds: [area description]
- Season: [dates and target species]

Help me with:

1. FLEET MAINTENANCE TRACKER
   Build a maintenance schedule template for our fleet covering:
   - Hull inspection and bottom paint (annual)
   - Engine service intervals (hours-based)
   - Safety equipment certification dates (USCG requirements)
   - Electronics and navigation equipment calibration
   - Refrigeration system maintenance
   - Net and gear repair/replacement schedule
   - Insurance renewal dates

   For each vessel, track:
   - Vessel name: [name]
   - Owner/captain: [name]
   - Last haul-out: [date]
   - Engine hours: [hours]
   - Next USCG inspection: [date]
   - Insurance expiration: [date]
   - Known issues: [list]

2. FUEL COST MANAGEMENT
   Current diesel price: $[X]/gallon at our dock
   Average fuel consumption by vessel type:
   - [Vessel type A]: [gallons per trip]
   - [Vessel type B]: [gallons per trip]

   Model:
   - Fleet fuel cost per trip and per pound of fish landed
   - Break-even catch per trip at current fuel prices
   - Impact of a $0.50/gallon diesel increase on profitability
   - Should we negotiate a bulk fuel purchase for the season?

3. SAFETY & COMPLIANCE
   Generate:
   - Pre-departure safety checklist (USCG compliant)
   - Float plan template for all vessels
   - Emergency procedures card (laminated, posted in wheelhouse)
   - Annual USCG documentation checklist
   - Crew safety training log template
   - Man-overboard drill schedule and documentation

4. SEASON PLANNING
   Draft a season plan covering:
   - Fleet deployment schedule: which vessels fish which openings
   - Delivery rotation: stagger landings to match processing capacity
   - Weather window decision framework: when to go, when to stay in
   - Communication protocol: VHF channels, satellite check-in schedule
   - End-of-season haul-out and winterization timeline


5. Regulatory Compliance & Sustainability

# Fishing Co-op Regulatory Tracker
# Update as needed, paste into Claude

regulatory_status = {
    "co_op": "[Your Fishing Co-op Name]",
    "state": "[state]",
    "federal_permits": {
        "limited_entry_permits": [
            {"fishery": "[e.g., Bristol Bay sockeye]", "permit_type": "[seine / gillnet / troll]", "permits_held": 24, "permits_leased": 3, "annual_fee": 500}
        ],
        "ifq_quota_shares": {
            "species": "[e.g., halibut]",
            "total_ifq_lbs": 85000,
            "owned_by_co_op": 45000,
            "leased_in": 25000,
            "leased_out": 0,
            "lease_rate_per_lb": 1.85,
            "quota_utilization_percent": 92
        }
    },
    "state_licenses": {
        "processor_license": {"expiration": "[date]", "status": "current"},
        "fish_buyer_license": {"expiration": "[date]", "status": "current"},
        "vessel_licenses": {"total": 32, "current": 30, "expired": 2}
    },
    "observer_program": {
        "coverage_requirement_percent": "[percent]",
        "observer_days_ytd": 45,
        "observer_days_required": 60,
        "observer_cost_per_day": 350,
        "electronic_monitoring": "[yes/no]"
    },
    "sustainability_certifications": {
        "msc_certified": "[yes/no/in process]",
        "fishery_improvement_project": "[yes/no]",
        "community_supported_fishery": "[yes/no]",
        "fair_trade_certified": "[yes/no]"
    },
    "reporting_requirements": {
        "fish_tickets": "per landing",
        "vessel_logbooks": "daily",
        "processor_reports": "weekly",
        "annual_catch_report": "[due date]",
        "economic_data_report": "[due date]"
    }
}

# Ask Claude:
# 1. Two vessel licenses are expired — flag all compliance gaps and draft a remediation checklist
# 2. Observer coverage at 75% of requirement — project cost to finish the year and draft a schedule
# 3. Build a complete regulatory calendar: every filing, renewal, and reporting deadline for the year
# 4. We're considering MSC certification — outline the process, timeline, costs, and market premium
# 5. Draft our annual catch report summary from season data
# 6. IFQ utilization is 92% — should we lease more quota or is that leaving enough buffer?
# 7. Summarize any regulatory changes from the last council meeting that affect our fishery
# 8. Create a permit transfer/lease tracking system for the co-op
# NOTE: Consult your fisheries attorney and state agency for legal compliance questions.


6. Member Settlement & Revenue Distribution

# Fishing Co-op Settlement Calculator
# Run at end of delivery period, paste into Claude

settlement_data = {
    "co_op": "[Your Fishing Co-op Name]",
    "settlement_period": "[dates]",
    "pool_type": "[price pooling / individual settlement / hybrid]",
    "total_revenue": {
        "gross_fish_sales": 1250000,
        "value_added_sales": 85000,
        "ice_and_fuel_sales_to_members": 42000,
        "other_income": 8000,
        "total_gross": 1385000
    },
    "operating_costs": {
        "processing_labor": 145000,
        "plant_overhead": 68000,
        "cold_storage_and_utilities": 35000,
        "packaging_and_shipping": 42000,
        "ice_production": 18000,
        "fuel_purchased": 38000,
        "dock_and_equipment": 25000,
        "insurance": 32000,
        "management_and_admin": 55000,
        "marketing": 12000,
        "observer_program": 21000,
        "loan_payments": 45000,
        "reserve_fund_contribution": 35000,
        "total_costs": 571000
    },
    "net_available_for_settlement": 814000,
    "member_deliveries": [
        {"vessel": "[Vessel A]", "captain": "[name]", "lbs_delivered": 85000, "species_mix": {"sockeye": 62000, "pink": 18000, "chum": 5000}, "quality_grade_avg": "premium"},
        {"vessel": "[Vessel B]", "captain": "[name]", "lbs_delivered": 72000, "species_mix": {"sockeye": 50000, "pink": 20000, "chum": 2000}, "quality_grade_avg": "standard"},
        {"vessel": "[Vessel C]", "captain": "[name]", "lbs_delivered": 68000, "species_mix": {"sockeye": 55000, "pink": 10000, "chum": 3000}, "quality_grade_avg": "premium"}
    ],
    "price_pool_weights": {
        "sockeye_premium": 1.00,
        "sockeye_standard": 0.85,
        "pink_premium": 0.30,
        "pink_standard": 0.25,
        "chum": 0.15
    },
    "advances_paid": {
        "Vessel A": 35000,
        "Vessel B": 28000,
        "Vessel C": 30000
    }
}

# Ask Claude:
# 1. Calculate each member's settlement payment using the pool weights and deducting advances already paid
# 2. Break down the price-per-pound each member earned by species and grade
# 3. Compare this settlement to last period — are members earning more or less per pound?
# 4. Generate individual settlement statements for each vessel (printable, one page each)
# 5. What percentage of gross revenue went to operating costs? Is that healthy for a fishing co-op?
# 6. Model what happens to settlements if we cut processing costs by 10% vs if we get 10% better prices
# 7. Draft the settlement letter to members explaining how payments were calculated
# 8. Reserve fund contribution at $35K — is that enough for off-season expenses and equipment replacement?


How to Use Any of These
1. Go to claude.ai
2. Copy any template above
3. Replace the [brackets] with your real information
4. Hit enter
5. Claude gives you a ready-to-use result
6. Modify, ask follow-ups, refine

No app to install. No training required. No data leaves your conversation.

Built for fishing co-ops. From the dock to the market. Pass it on.
