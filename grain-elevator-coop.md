Grain Elevator Co-op Plug-ins
1. Harvest Intake Tracker

# Grain Elevator Harvest Dashboard
# Update daily during harvest, paste into Claude

daily_intake = {
    "date": "2026-10-15",
    "commodity": {
        "corn": {
            "loads_received": 47,
            "bushels_today": 42300,
            "avg_moisture": 17.2,
            "avg_test_weight": 54.8,
            "target_moisture": 15.0,
            "bins_available": ["B3", "B7", "B12"],
            "bin_capacity_remaining_bu": 185000,
            "drying_capacity_bu_per_day": 25000
        },
        "soybeans": {
            "loads_received": 22,
            "bushels_today": 19800,
            "avg_moisture": 11.8,
            "avg_test_weight": 57.2,
            "target_moisture": 13.0,
            "bins_available": ["B1", "B5"],
            "bin_capacity_remaining_bu": 120000,
            "drying_capacity_bu_per_day": 0  # beans don't usually need drying at this moisture
        }
    },
    "wait_time_current": "45 minutes",
    "trucks_in_queue": 12,
    "operating_hours": "6am-10pm",
    "weather_next_48h": "rain likely Thursday afternoon"
}

current_prices = {
    "corn_cash_bu": 4.35,
    "corn_basis": -0.28,
    "corn_futures_dec": 4.63,
    "soybeans_cash_bu": 11.20,
    "soybeans_basis": -0.45,
    "soybeans_futures_nov": 11.65
}

# Ask Claude:
# 1. At current intake rate, when do we fill available bin space?
# 2. Drying backlog: how many days behind are we at 17.2% moisture?
# 3. Should we run dryers overnight given propane at $[X]/gallon?
# 4. Draft a text/radio message to members about wait times and rain forecast
# 5. If rain hits Thursday, model the moisture spike and drying cost increase
# 6. Current basis vs 3-year average — should we advise members to store or sell?


2. Basis & Pricing Advisor

# Grain Marketing Decision Support
# NOT financial advice — information tool for co-op board discussion

historical_basis = {
    "corn": {
        "current": -0.28,
        "30_day_avg": -0.25,
        "harvest_avg_3yr": -0.35,
        "spring_avg_3yr": -0.12,
        "widest_12mo": -0.52,
        "narrowest_12mo": -0.08
    },
    "soybeans": {
        "current": -0.45,
        "30_day_avg": -0.40,
        "harvest_avg_3yr": -0.55,
        "spring_avg_3yr": -0.20,
        "widest_12mo": -0.72,
        "narrowest_12mo": -0.15
    }
}

storage_costs = {
    "commercial_rate_per_bu_per_month": 0.04,
    "shrink_loss_percent_per_month": 0.1,
    "insurance_per_bu": 0.005,
    "interest_cost_per_bu_per_month": 0.02  # opportunity cost at current rates
}

# Ask Claude:
# 1. At current basis vs historical, are we at a normal harvest spread?
# 2. Break-even storage calculation: how many months can a farmer store corn before costs exceed expected basis improvement?
# 3. Build a simple one-page handout comparing "sell now" vs "store and sell in March" scenarios
# 4. Draft talking points for our grain merchandiser to share with members at the counter
# 5. Flag any unusual basis movements that might signal local supply/demand shifts
# NOTE: This is informational only. Not financial advice. Members make their own decisions.


# Grain Marketing Decision Support
# NOT financial advice — information tool for co-op board discussion

historical_basis = {
    "corn": {
        "current": -0.28,
        "30_day_avg": -0.25,
        "harvest_avg_3yr": -0.35,
        "spring_avg_3yr": -0.12,
        "widest_12mo": -0.52,
        "narrowest_12mo": -0.08
    },
    "soybeans": {
        "current": -0.45,
        "30_day_avg": -0.40,
        "harvest_avg_3yr": -0.55,
        "spring_avg_3yr": -0.20,
        "widest_12mo": -0.72,
        "narrowest_12mo": -0.15
    }
}

storage_costs = {
    "commercial_rate_per_bu_per_month": 0.04,
    "shrink_loss_percent_per_month": 0.1,
    "insurance_per_bu": 0.005,
    "interest_cost_per_bu_per_month": 0.02  # opportunity cost at current rates
}

# Ask Claude:
# 1. At current basis vs historical, are we at a normal harvest spread?
# 2. Break-even storage calculation: how many months can a farmer store corn before costs exceed expected basis improvement?
# 3. Build a simple one-page handout comparing "sell now" vs "store and sell in March" scenarios
# 4. Draft talking points for our grain merchandiser to share with members at the counter
# 5. Flag any unusual basis movements that might signal local supply/demand shifts
# NOTE: This is informational only. Not financial advice. Members make their own decisions.

3. Transportation & Logistics Coordinator

# Grain Shipping Planner

shipments = {
    "rail": {
        "shuttle_cars_allocated": 75,
        "loading_capacity_cars_per_day": 8,
        "current_tariff_per_car": 4800,
        "destination": "Pacific Northwest export terminal",
        "loading_window_start": "2026-11-01",
        "loading_window_end": "2026-11-10",
        "demurrage_per_car_per_day": 125
    },
    "truck": {
        "contract_carriers": [
            {"name": "Driftless Trucking", "trucks_available": 6, "rate_per_loaded_mile": 3.85, "max_bushels": 950},
            {"name": "Valley Transport", "trucks_available": 4, "rate_per_loaded_mile": 4.10, "max_bushels": 900},
            {"name": "Owner-operators (spot)", "trucks_available": "variable", "rate_per_loaded_mile": 4.50, "max_bushels": 1000}
        ],
        "destinations": {
            "ethanol_plant": {"distance_miles": 45, "current_bid_per_bu": 4.42},
            "river_terminal": {"distance_miles": 78, "current_bid_per_bu": 4.38},
            "feed_lot": {"distance_miles": 32, "current_bid_per_bu": 4.48}
        }
    },
    "inventory_to_move_bu": 450000,
    "target_completion": "2026-12-15"
}

# Ask Claude:
# 1. Build a shipping schedule that loads rail cars without incurring demurrage
# 2. Compare net revenue per bushel: rail to PNW vs truck to each local destination
# 3. If we lose 2 contract trucks, can we still hit our target date with spot market?
# 4. Model fuel surcharge impact if diesel goes up $0.50/gallon
# 5. Draft carrier confirmation emails with loading schedule and requirements
# 6. Contingency plan if rail loading window gets pushed back 5 days


4. Compliance & Reporting

Our grain elevator co-op needs help with regulatory compliance.

Facility details:
- Licensed capacity: [bushels]
- Number of bins: [number]
- Commodities handled: [corn, soybeans, wheat, etc.]
- State: [state]

Help me with:
1. Build a checklist for our annual [state] Warehouse License renewal
2. Draft our monthly position report showing physical inventory vs obligations
3. Summarize OSHA grain handling facility requirements in plain language
4. Create a bin entry safety protocol document (printable, post at every bin)
5. Organize our scale ticket records for auditor review
6. Draft our fumigation log template that meets [state] ag department requirements


5. Farmer Communication Hub

Draft communications for our grain elevator members:

Current situation:
- Harvest is [ahead/behind] schedule by [X] days
- Current wait time at elevator: [time]
- Price outlook: [brief summary]
- Weather concern: [if any]

Generate:
1. Daily text blast (under 160 characters) with cash price, wait time, and hours
2. Weekly email update with market summary, harvest progress, and operational notes
3. End-of-harvest summary letter with total bushels received, average quality, and storage options
4. Annual meeting presentation outline showing co-op performance, patronage dividend estimate, and capital improvement plans

Tone: Straightforward. These are farmers. No fluff. Numbers and facts.
