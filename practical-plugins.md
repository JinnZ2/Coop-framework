Claude for Co-ops: Practical Code Plug-ins
How to Use These
These are prompts and lightweight scripts you can paste directly into Claude. No coding experience needed. Just copy, paste, and modify the parts in [brackets] with your own information.

1. Vendor Order Generator
Paste this into Claude:

I run a food co-op. Here are my vendors and what we typically order monthly:

[Vendor 1]: [Product list with quantities]
[Vendor 2]: [Product list with quantities]
[Vendor 3]: [Product list with quantities]

Generate individual purchase order emails for each vendor for this month.
Adjust quantities: [up 10% for seasonal demand / down 15% because of surplus / keep same].
Format each as a ready-to-send email with subject line, itemized list, and requested delivery date of [date].


Example filled in:

I run a food co-op. Here are my vendors and what we typically order monthly:

Harmony Valley Farm: 40 cases mixed greens, 20 cases root vegetables, 15 cases seasonal fruit
Driftless Provisions: 200 lbs cheddar, 100 lbs gouda, 50 lbs butter
North Country Bakery: 60 loaves sourdough, 40 loaves whole wheat, 30 dozen rolls

Generate individual purchase order emails for each vendor for this month.
Adjust quantities: up 15% for spring demand.
Format each as a ready-to-send email with subject line, itemized list, and requested delivery date of March 15, 2026.


What Claude produces (example output):

---

**Email 1**

**Subject:** March 2026 Purchase Order — Viroqua Food Co-op

Hi Harmony Valley team,

Here's our order for March delivery. We've adjusted quantities up 15% for spring demand.

| Item | Quantity |
|---|---|
| Mixed greens | 46 cases |
| Root vegetables | 23 cases |
| Seasonal fruit | 17 cases |

**Requested delivery date:** March 15, 2026
**Delivery address:** 609 N Main St, Viroqua, WI 54665

Please confirm availability and let us know if any substitutions are needed. Thanks as always for the great product.

Best,
[Your name]
Viroqua Food Co-op

---

**Email 2**

**Subject:** March 2026 Purchase Order — Viroqua Food Co-op

Hi Driftless Provisions,

March order below, adjusted up 15% for spring:

| Item | Quantity |
|---|---|
| Cheddar | 230 lbs |
| Gouda | 115 lbs |
| Butter | 58 lbs |

**Requested delivery date:** March 15, 2026

Let me know if any items need a longer lead time. Thanks!

Best,
[Your name]
Viroqua Food Co-op

---

**Email 3**

**Subject:** March 2026 Purchase Order — Viroqua Food Co-op

Hi North Country Bakery,

Here's our March order with 15% seasonal increase:

| Item | Quantity |
|---|---|
| Sourdough loaves | 69 |
| Whole wheat loaves | 46 |
| Rolls | 35 dozen |

**Requested delivery date:** March 15, 2026

Looking forward to it. The sourdough has been flying off the shelves.

Best,
[Your name]
Viroqua Food Co-op

---

*You can then ask follow-ups like "add a note to Harmony Valley about switching to spring greens" or "make the tone more casual."*


2. Board Meeting Minutes Processor

Here are my raw notes from last night's board meeting. Clean them up into formal
minutes with the following sections:

- Date, attendees, call to order time
- Old business summary
- New business summary  
- Motions made (who moved, who seconded, vote result)
- Action items with assigned person and deadline
- Next meeting date

Raw notes:
[Paste your handwritten or rough notes here]


3. Seasonal Delivery Route Optimizer
Paste into Claude with your actual stops:

# Co-op Delivery Route Planner
# Paste this into Claude and replace with your actual delivery data

deliveries = {
    "Monday": [
        {"stop": "Vernon Electric Co-op", "address": "110 Saugstad Rd, Westby WI", "window": "8am-10am", "priority": "high"},
        {"stop": "Viroqua Food Co-op", "address": "609 N Main St, Viroqua WI", "window": "10am-12pm", "priority": "high"},
        {"stop": "Kickapoo Valley Reserve", "address": "S3661 WI-131, La Farge WI", "window": "flexible", "priority": "medium"},
    ],
    "Wednesday": [
        {"stop": "People's Food Co-op La Crosse", "address": "315 5th Ave S, La Crosse WI", "window": "7am-9am", "priority": "high"},
        {"stop": "Montessori School", "address": "[your address]", "window": "11am-1pm", "priority": "medium"},
    ]
}

# Ask Claude:
# 1. Sequence these stops to minimize backtracking
# 2. Flag any delivery window conflicts
# 3. Estimate fuel cost at [current diesel price] per gallon
# 4. Suggest what to do if a stop falls through


4. Grant Application Builder

Help me write a USDA Rural Development grant application.

Our co-op details:
- Name: [Co-op name]
- Type: [food/electric/agricultural/worker-owned]
- Location: [town, state]
- Years operating: [number]
- Members: [number]
- Annual revenue: [amount]
- Service area: [counties/region]

Project we need funding for:
[Describe what you need - cold storage, delivery vehicle, solar panels, etc.]

Estimated cost: [amount]
How it helps our community: [brief description]

Write the full narrative section addressing:
1. Statement of need
2. Project description  
3. Community impact
4. Sustainability plan
5. Budget justification

Use plain language. No jargon. These are real people doing real work.


5. Supplier Contract Analyzer

I'm going to paste a supplier contract below. Analyze it and give me:

1. Plain English summary of what we're agreeing to
2. Any clauses that limit our flexibility (exclusivity, minimum orders, auto-renewal)
3. Any clauses that let them change pricing without our approval
4. Any data sharing or IP clauses — flag anything where they get rights to our information
5. Recommended changes to protect our co-op
6. Red flags I should bring to our board

Contract text:
[Paste contract here]


6. Inventory Tracker & Reorder Alert System

# Co-op Inventory Monitor
# Update these numbers weekly, paste into Claude for analysis

inventory = {
    "dairy": {
        "whole_milk_gallons": {"current": 45, "min_threshold": 30, "weekly_usage": 60, "supplier": "Organic Valley", "lead_time_days": 3},
        "butter_lbs": {"current": 12, "min_threshold": 20, "weekly_usage": 25, "supplier": "Organic Valley", "lead_time_days": 3},
        "cheddar_lbs": {"current": 55, "min_threshold": 40, "weekly_usage": 35, "supplier": "Driftless Provisions", "lead_time_days": 5},
    },
    "produce": {
        "mixed_greens_cases": {"current": 8, "min_threshold": 15, "weekly_usage": 20, "supplier": "Harmony Valley", "lead_time_days": 2},
        "root_vegetables_cases": {"current": 22, "min_threshold": 10, "weekly_usage": 12, "supplier": "Harmony Valley", "lead_time_days": 2},
    },
    "bakery": {
        "sourdough_loaves": {"current": 18, "min_threshold": 25, "weekly_usage": 30, "supplier": "North Country Bakery", "lead_time_days": 1},
    }
}

# Ask Claude:
# 1. What needs reordering RIGHT NOW?
# 2. What will need reordering within 3 days?
# 3. Draft the reorder emails for anything urgent
# 4. Flag seasonal adjustments I should consider for [current month]
# 5. Calculate if I'm overordering anything based on usage patterns


What Claude produces (example output):

---

**URGENT — Reorder Now:**

| Item | Current | Min Threshold | Weekly Usage | Days Until Stockout |
|---|---|---|---|---|
| Butter | 12 lbs | 20 lbs | 25 lbs/week | **3 days** |
| Mixed greens | 8 cases | 15 cases | 20 cases/week | **2.8 days** |
| Sourdough | 18 loaves | 25 loaves | 30 loaves/week | **4.2 days** |

**Action needed:** Butter and mixed greens are below minimum threshold RIGHT NOW. Sourdough will be below threshold by tomorrow.

**Reorder within 3 days:**
- Butter — contact Organic Valley today (3-day lead time means you'll hit zero before delivery if you wait)
- Mixed greens — contact Harmony Valley today (2-day lead time, cutting it close)
- Sourdough — contact North Country Bakery tomorrow at latest (1-day lead time)

**You're fine on:**
- Whole milk: 45 gallons, ~5.25 days of supply, above threshold
- Cheddar: 55 lbs, ~11 days of supply, well above threshold
- Root vegetables: 22 cases, ~13 days of supply, comfortable

**Draft reorder email for Organic Valley:**

Subject: Urgent Reorder — Butter — Viroqua Food Co-op

Hi Organic Valley team, we need to reorder butter as soon as possible...

---


7. Member Newsletter Generator

Write our monthly co-op newsletter.

Co-op name: [name]
Month: [month]

Updates to include:
- [New product or vendor partnership]
- [Upcoming event — fair, workshop, seed swap, etc.]
- [Board decision or policy change]
- [Member spotlight or farmer profile]
- [Seasonal produce availability]

Tone: Warm, neighborly, like you're talking to someone at the counter.
Length: One page, printable. Many of our members don't use email.
Include a small section for: volunteer opportunities, upcoming dates, contact info.


8. Diesel & Operating Cost Modeler

# Co-op Operating Cost Monitor
# Plug in your real numbers

operations = {
    "routes": {
        "route_1": {"name": "Viroqua-La Crosse corridor", "miles_round_trip": 120, "frequency": "2x weekly", "stops": 6},
        "route_2": {"name": "Driftless loop", "miles_round_trip": 85, "frequency": "1x weekly", "stops": 4},
        "route_3": {"name": "La Farge-Westby run", "miles_round_trip": 45, "frequency": "3x weekly", "stops": 3},
    },
    "vehicle": {"mpg": 8, "type": "refrigerated box truck"},
    "diesel_price_per_gallon": 4.15,
    "monthly_fixed_costs": {
        "insurance": 1200,
        "maintenance_reserve": 500,
        "cold_storage_electricity": 800,
    }
}

# Ask Claude:
# 1. Calculate monthly fuel costs per route and total
# 2. Model what happens if diesel goes to $4.50 / $5.00 / $5.50
# 3. Which route is least cost-efficient per stop?
# 4. Where could I consolidate deliveries to save fuel?
# 5. At what diesel price does [route name] stop being viable?


9. Community Event Planner

Help me plan a [type of event: farmers market / seed swap / co-op fair / community workshop].

Details:
- Date: [date]
- Location: [venue]
- Expected attendance: [number]
- Budget: [amount]
- Vendors/participants confirmed: [list]
- Vendors/participants still needed: [list]

Generate:
1. Day-of timeline from setup to breakdown
2. Task assignments checklist (printable)
3. Promotional flyer text (keep it simple, printable on one page)
4. Social media post (3 versions: Facebook, simple text for email list, word-of-mouth script)
5. Supply list with quantities
6. Contingency plan for weather/low turnout


10. Knowledge Preservation Template

Our [role: operations manager / head farmer / founding member] is 
[retiring / reducing hours / moving on] after [X] years.

Help me build a knowledge transfer document. I'm going to share their 
answers to these questions — organize them into a searchable operations 
manual:

1. What do you do daily/weekly/monthly/seasonally that nobody else knows about?
2. Which vendor relationships depend on personal contact and what are the quirks?
3. What breaks regularly and how do you fix it?
4. What are the unwritten rules that keep things running?
5. Who do you call when [specific problem] happens?
6. What have you tried that didn't work — and why?
7. What would you change if you could?

Their answers:
[Paste responses here]

Format as a manual with:
- Table of contents
- Searchable sections by topic
- Emergency contacts section
- Seasonal calendar of critical tasks
- "If this breaks, do this" troubleshooting guide


11. Price Comparison & Margin Calculator

# Compare supplier pricing across co-op network
# Use this to negotiate better rates or find alternatives

suppliers = {
    "Organic Valley": {
        "whole_milk_gallon": 4.20,
        "butter_lb": 5.50,
        "cream_quart": 3.80,
        "delivery_fee": 25.00,
        "minimum_order": 200,
        "payment_terms": "net 30"
    },
    "Local Dairy Farm B": {
        "whole_milk_gallon": 3.95,
        "butter_lb": 6.00,
        "cream_quart": 3.50,
        "delivery_fee": 0,
        "minimum_order": 100,
        "payment_terms": "net 15"
    }
}

our_monthly_volume = {
    "whole_milk_gallon": 240,
    "butter_lb": 100,
    "cream_quart": 60
}

# Ask Claude:
# 1. Total monthly cost from each supplier including delivery fees
# 2. Break-even point where the cheaper per-unit price beats the delivery fee
# 3. What markup do we need at retail to maintain [target margin %]?
# 4. If we increase volume by 20%, who gives us a better deal?


How to Use Any of These
	1.	Go to claude.ai
	2.	Copy any template above
	3.	Replace the [brackets] with your real information
	4.	Hit enter
	5.	Claude gives you a ready-to-use result
	6.	Modify, ask follow-ups, refine
No app to install. No training required. No data leaves your conversation.

Built for co-ops. Built to be shared. Pass it on.



Electrical Co-op Plug-ins
1. Outage Response Coordinator

We're a rural electric co-op serving [number] members across [counties].
We just got reports of outages in these areas:

[Area 1]: [number] members affected, reported at [time]
[Area 2]: [number] members affected, reported at [time]
[Area 3]: [number] members affected, reported at [time]

Available crew: [number] line workers
Available trucks: [number]
Current weather: [conditions]
Known infrastructure issues: [any recent maintenance, aging lines, tree problems]

Help me:
1. Prioritize restoration sequence based on members affected and critical facilities (hospitals, schools, elderly/medical-dependent members)
2. Assign crews to maximize restoration speed
3. Draft member notification for each area with estimated restoration time
4. Draft social media update
5. Flag any safety concerns given current weather
6. Build a timeline for my board report


2. Load Forecasting & Peak Management

# Rural Electric Co-op Load Planner
# Replace with your actual meter and weather data

service_area = {
    "total_members": 3200,
    "residential": 2800,
    "agricultural": 280,
    "commercial": 100,
    "industrial": 20,
    "miles_of_line": 450,
    "substations": 4
}

seasonal_patterns = {
    "winter": {
        "peak_hours": "6am-9am, 4pm-9pm",
        "primary_load": "electric heat, grain dryers",
        "avg_daily_kwh": 85,
        "peak_demand_mw": 12.5
    },
    "summer": {
        "peak_hours": "2pm-7pm",
        "primary_load": "irrigation, AC, dairy cooling",
        "avg_daily_kwh": 62,
        "peak_demand_mw": 9.8
    },
    "spring_fall": {
        "peak_hours": "6am-8am, 5pm-8pm",
        "primary_load": "grain drying, general",
        "avg_daily_kwh": 48,
        "peak_demand_mw": 7.2
    }
}

wholesale_rate = {
    "off_peak_per_kwh": 0.04,
    "on_peak_per_kwh": 0.09,
    "demand_charge_per_kw": 12.50,
    "peak_penalty_threshold_mw": 11.0
}

# Ask Claude:
# 1. When are we most likely to hit peak penalty this season?
# 2. If we shift [X load type] off-peak, how much do we save monthly?
# 3. Which member category is driving peak demand?
# 4. Model a 10% increase in agricultural load — do we need substation upgrades?
# 5. Draft a member notice about voluntary load reduction during peak events
# 6. Compare cost of peak shaving battery vs demand response program


3. Line Maintenance Scheduler

# Preventive Maintenance Tracker
# Update quarterly, paste into Claude for analysis

line_segments = {
    "segment_A": {
        "name": "County Road J - Hilltop substation",
        "miles": 18,
        "pole_count": 145,
        "age_years": 35,
        "last_inspection": "2025-06",
        "tree_encroachment_rating": "high",
        "outages_last_12_months": 7,
        "critical_facilities_served": ["Westby hospital", "Vernon Manor nursing home"]
    },
    "segment_B": {
        "name": "Ridge Road - Valley loop",
        "miles": 12,
        "pole_count": 98,
        "age_years": 22,
        "last_inspection": "2025-09",
        "tree_encroachment_rating": "medium",
        "outages_last_12_months": 2,
        "critical_facilities_served": []
    },
    "segment_C": {
        "name": "Kickapoo bottoms feeder",
        "miles": 8,
        "pole_count": 65,
        "age_years": 42,
        "last_inspection": "2024-11",
        "tree_encroachment_rating": "high",
        "outages_last_12_months": 12,
        "critical_facilities_served": ["La Farge elementary"]
    }
}

annual_maintenance_budget = 180000
crew_day_rate = 2800  # fully loaded cost per crew per day
tree_trimming_cost_per_mile = 3500

# Ask Claude:
# 1. Rank segments by failure risk (age + outage frequency + tree rating)
# 2. Build a 12-month maintenance calendar that fits the budget
# 3. Which segment gives the best reliability improvement per dollar spent?
# 4. Draft a right-of-way clearing notice for affected landowners
# 5. Project when segment C needs full rebuild vs continued maintenance
# 6. What's our liability exposure on segments serving critical facilities?


4. Member Rate Communication

We need to raise residential rates by [X]% effective [date].

Reasons:
- [Wholesale power cost increase of X%]
- [Infrastructure upgrade requirements]
- [Regulatory compliance costs]

Our members include:
- Fixed-income elderly: [number/percentage]
- Agricultural operations: [number/percentage]  
- General residential: [number/percentage]

Write three versions of the rate increase notice:
1. Formal letter for mailing (plain language, empathetic, explains why)
2. One-page FAQ addressing common concerns
3. Board presentation talking points for the annual meeting

Include:
- Comparison to investor-owned utility rates in the region
- Reminder that as member-owners, this is THEIR decision
- Available assistance programs for hardship cases
- How to attend the board meeting to voice concerns


5. Solar & Distributed Generation Manager

# Community Solar & Net Metering Tracker

member_solar = {
    "installations": [
        {"member_id": "M-1042", "name": "Peterson Farm", "capacity_kw": 25, "install_date": "2024-03", "annual_generation_kwh": 32000, "net_metering": True},
        {"member_id": "M-0887", "name": "Hillside Dairy", "capacity_kw": 50, "install_date": "2023-08", "annual_generation_kwh": 61000, "net_metering": True},
        {"member_id": "M-2201", "name": "Village of [name]", "capacity_kw": 100, "install_date": "2025-01", "annual_generation_kwh": 120000, "net_metering": True},
    ],
    "community_solar_garden": {
        "total_capacity_kw": 500,
        "subscribers": 85,
        "percent_subscribed": 72,
        "annual_generation_kwh": 650000
    },
    "pending_applications": 12,
    "total_distributed_capacity_kw": 675,
    "co_op_peak_demand_kw": 12500
}

# Ask Claude:
# 1. What percentage of our peak demand is now covered by distributed generation?
# 2. At current application rate, when do we hit interconnection study thresholds?
# 3. Draft a community solar subscription pitch for the remaining 28% capacity
# 4. Model revenue impact if net metering policy changes to avoided cost rate
# 5. Which time of day does member solar reduce our wholesale peak purchases most?
# 6. Build a one-page handout for members asking about solar: costs, savings, process
