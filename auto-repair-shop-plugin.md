# Auto Repair Shop Plug-ins

You run a small shop. Maybe it's just you. Maybe it's you and a few techs. These
templates help you quote jobs, chase parts, and keep customers informed without
buying another monthly subscription.

Copy a block, replace the `[brackets]` with your real numbers, paste it into
Claude.

## 1. Job Tracking & Estimates

```python
# Shop Job Board
# Update daily, paste into Claude

current_jobs = {
    "bay_1": {
        "vehicle": "2018 Ford F-150",
        "owner": "Johnson",
        "complaint": "Check engine light, rough idle",
        "codes_pulled": ["P0301", "P0304"],
        "diagnosis": "Misfire cylinders 1 and 4",
        "parts_needed": [
            {"part": "Motorcraft SP-534 spark plugs x8", "cost": 62.00, "source": "AutoZone", "in_stock": True},
            {"part": "Ignition coil pack x2", "cost": 89.00, "source": "RockAuto", "in_stock": False, "eta": "2 days"}
        ],
        "labor_hours_estimated": 2.5,
        "labor_rate": 95,
        "status": "waiting on parts",
        "promised_date": "2026-03-04"
    },
    "bay_2": {
        "vehicle": "2015 Chevy Silverado 2500HD",
        "owner": "Martinez",
        "complaint": "Transmission slipping between 2nd and 3rd",
        "codes_pulled": ["P0733"],
        "diagnosis": "Pending - need to drop pan and inspect",
        "parts_needed": [],
        "labor_hours_estimated": "TBD",
        "labor_rate": 95,
        "status": "diagnosing",
        "promised_date": "TBD"
    },
    "bay_3": {
        "vehicle": "2020 Toyota Tacoma",
        "owner": "Nguyen",
        "complaint": "Brake squeal, pulling right",
        "codes_pulled": [],
        "diagnosis": "Warped right front rotor, pads at 2mm both sides",
        "parts_needed": [
            {"part": "Front rotors x2", "cost": 78.00, "source": "O'Reilly", "in_stock": True},
            {"part": "Ceramic brake pads front set", "cost": 45.00, "source": "O'Reilly", "in_stock": True}
        ],
        "labor_hours_estimated": 1.5,
        "labor_rate": 95,
        "status": "ready to start",
        "promised_date": "2026-03-02"
    }
}

# Ask Claude:
# 1. Generate customer-ready estimates for each job (parts + labor + tax + shop supplies)
# 2. Which jobs can I finish today based on parts availability?
# 3. Draft a text to Johnson about the parts delay — professional but human
# 4. The Silverado transmission job might be bigger than expected — draft a "here's what we found" call script for Martinez
# 5. Compare parts pricing: AutoZone vs RockAuto vs O'Reilly for everything on the board
# 6. End of week: generate invoice for completed jobs
```

## 2. Vendor & Parts Management

```python
# Parts Supplier Tracker
# Update when pricing or terms change, paste into Claude

suppliers = {
    "AutoZone": {
        "account": "commercial",
        "discount_off_retail": 0.20,
        "delivery": "twice daily, free over $50",
        "delivery_cutoff": "2pm for same-day",
        "returns": "90 days with receipt, no restock fee",
        "core_charges": "refunded on counter return",
        "strengths": ["fast delivery", "good on brakes and filters"],
        "weaknesses": ["thin on European parts", "higher price on electrical"]
    },
    "O'Reilly": {
        "account": "commercial",
        "discount_off_retail": 0.22,
        "delivery": "three times daily, free over $35",
        "delivery_cutoff": "3pm for same-day",
        "returns": "90 days, 15% restock on special order",
        "core_charges": "refunded within 30 days",
        "strengths": ["best hydraulic hose service", "loaner tool program"],
        "weaknesses": ["special orders slow"]
    },
    "RockAuto": {
        "account": "online",
        "discount_off_retail": 0.35,
        "delivery": "2-4 business days, shipping charged per warehouse",
        "delivery_cutoff": "n/a",
        "returns": "30 days, customer pays return shipping",
        "core_charges": "customer ships core back",
        "strengths": ["cheapest on OEM-equivalent", "wide catalog"],
        "weaknesses": ["no same-day", "split shipments add freight"]
    },
    "NAPA": {
        "account": "commercial",
        "discount_off_retail": 0.18,
        "delivery": "once daily",
        "delivery_cutoff": "11am",
        "returns": "60 days",
        "core_charges": "refunded on counter return",
        "strengths": ["heavy duty and farm equipment", "knowledgeable counter"],
        "weaknesses": ["only one delivery run per day"]
    }
}

open_orders = [
    {"part": "Ignition coil pack x2", "supplier": "RockAuto", "cost": 89.00,
     "ordered": "2026-03-01", "eta": "2026-03-03", "job": "bay_1", "status": "shipped"},
    {"part": "Transmission filter kit", "supplier": "NAPA", "cost": 42.00,
     "ordered": "2026-03-02", "eta": "2026-03-03", "job": "bay_2", "status": "ordered"}
]

cores_outstanding = [
    {"part": "Alternator core", "supplier": "O'Reilly", "value": 45.00, "days_held": 22},
    {"part": "Brake caliper core x2", "supplier": "AutoZone", "value": 80.00, "days_held": 8}
]

# Ask Claude:
# 1. For the parts on my job board, which supplier is cheapest once delivery fees and my discount are applied?
# 2. Which cores am I about to lose money on? Rank by deadline risk
# 3. I need a part by [date] — which suppliers can actually make that given their cutoffs?
# 4. Build a weekly ordering routine that minimizes freight and hits same-day cutoffs
# 5. Draft an email to [supplier] asking for better commercial pricing based on my monthly volume of [$amount]
# 6. Which parts should I stock on the shelf instead of ordering every time? Use my last 90 days of jobs
```

## 3. Customer Communication

```text
Help me communicate with customers at [Shop Name].

Shop details:
- Location: [city, state]
- Labor rate: $[rate]/hour
- Diagnostic fee: $[amount], [waived / applied] if work is approved
- Typical turnaround: [X] days
- Warranty offered: [months / miles]

Write the following, in plain language with no upsell pressure:

1. APPROVAL CALL SCRIPT
   Vehicle: [year make model]
   What they came in for: [original complaint]
   What we found: [actual diagnosis]
   Additional work needed: [description], $[amount]
   Safety urgency: [safe to drive / fix soon / do not drive]
   Goal: explain the "why" so they can make their own decision.

2. BAD NEWS ESTIMATE
   The repair costs $[amount] on a vehicle worth roughly $[value].
   Lay out the options honestly: repair, partial repair, or walk away.

3. DECLINED WORK FOLLOW-UP
   Customer declined [recommended repair] on [date].
   Write a short note for the file and a friendly reminder to send in [X] months.

4. DELAY NOTIFICATION
   Part is backordered until [date]. Vehicle is [drivable / not drivable].
   Apologize once, give a real new date, offer [loaner / ride / nothing].

5. REVIEW REQUEST
   Job completed: [description]. Send a short, non-pushy text asking for a review.
```

## 4. Shop Financials & Labor Rate

```python
# Shop Operating Model
# Update monthly, paste into Claude

shop = {
    "name": "[Your Shop Name]",
    "bays": 3,
    "technicians": 2,
    "labor_rate": 95,
    "tech_wages_hourly": [28, 24],
    "billable_hours_per_tech_per_week": 32,
    "shop_supply_fee_pct": 0.05
}

monthly_fixed_costs = {
    "rent": 2400,
    "utilities": 640,
    "insurance": 780,
    "software_subscriptions": 310,
    "equipment_loan": 425,
    "waste_disposal": 180,
    "advertising": 200
}

monthly_actuals = {
    "labor_revenue": 24320,
    "parts_revenue": 18700,
    "parts_cost": 13100,
    "comebacks": 2,
    "comeback_cost": 640,
    "jobs_completed": 71,
    "average_ticket": 605
}

# Ask Claude:
# 1. What is my true break-even in billable hours per month?
# 2. What is my effective labor rate after unbilled diagnostic and comeback time?
# 3. What parts margin am I actually running, and how does it compare to a typical independent shop?
# 4. Model raising my labor rate to $105 and $115 — what happens if I lose 5% or 10% of jobs?
# 5. Which fixed cost is most out of line for a 3-bay shop?
# 6. Draft a plain-language explanation of a rate increase I can hand to regular customers
```

## 5. Preventive Maintenance & Customer Retention

```python
# Customer Vehicle History
# Paste into Claude to find who is due for service

customers = [
    {"name": "Johnson", "vehicle": "2018 Ford F-150", "mileage_last_visit": 84200,
     "last_visit": "2026-03-04", "avg_miles_per_month": 1100,
     "services": ["oil change", "spark plugs", "coils"],
     "declined": ["front brake pads at 4mm"], "visits_per_year": 3},
    {"name": "Nguyen", "vehicle": "2020 Toyota Tacoma", "mileage_last_visit": 61500,
     "last_visit": "2026-03-02", "avg_miles_per_month": 900,
     "services": ["front rotors and pads"],
     "declined": [], "visits_per_year": 2},
    {"name": "Whitaker", "vehicle": "2014 Subaru Outback", "mileage_last_visit": 148000,
     "last_visit": "2025-09-18", "avg_miles_per_month": 700,
     "services": ["timing belt", "water pump", "oil change"],
     "declined": ["rear struts"], "visits_per_year": 1}
]

maintenance_intervals = {
    "oil_change_miles": 5000,
    "tire_rotation_miles": 7500,
    "brake_inspection_miles": 15000,
    "coolant_flush_miles": 60000,
    "transmission_service_miles": 60000
}

# Ask Claude:
# 1. Who is due or overdue for service right now based on estimated mileage?
# 2. Draft a reminder text for each — specific to their vehicle, not a form letter
# 3. Which declined repairs should I follow up on, and which have become safety issues?
# 4. Who has not been in for over 12 months? Draft a win-back message
# 5. Build a seasonal reminder calendar for my area: [state / climate]
# 6. Which customers are worth the most per year, and what keeps them coming back?
```

## 6. Diagnostic Notes & Shop Knowledge

```python
# Repair Knowledge Capture
# Log the jobs that took longer than they should have

hard_jobs = [
    {
        "vehicle": "2015 Chevy Silverado 2500HD",
        "symptom": "Slipping between 2nd and 3rd, no codes at first",
        "codes": ["P0733"],
        "what_we_tried": ["fluid and filter service", "pressure test", "dropped pan"],
        "actual_cause": "Debris in valve body, worn 3-4 clutch pack",
        "time_wasted_hours": 3.0,
        "lesson": "Pressure test before the fluid service on this platform — fresh fluid masked the symptom"
    },
    {
        "vehicle": "2018 Ford F-150 3.5 EcoBoost",
        "symptom": "Intermittent misfire, only under load when warm",
        "codes": ["P0301", "P0304"],
        "what_we_tried": ["plugs", "coil swap between cylinders"],
        "actual_cause": "Cracked coil boot arcing to head only at operating temp",
        "time_wasted_hours": 1.5,
        "lesson": "Inspect boots hot, not cold. Swap-and-retest only proves the coil, not the boot"
    }
]

# Ask Claude:
# 1. Turn these into a searchable shop reference organized by symptom
# 2. What diagnostic step, done first, would have saved the most time across these jobs?
# 3. Build a diagnostic flowchart for [common complaint at my shop]
# 4. Write a one-page checklist a new tech can follow for [system]
# 5. Which of these patterns should I quote extra diagnostic time for up front?
# 6. Interview me: ask the questions that get the rest of what I know out of my head and onto paper
```

---

Built for independent shops. Built to be shared. Pass it on.
