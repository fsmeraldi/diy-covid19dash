"""
Generate sample measles data in UKHSA API format
This provides initial data for the dashboard to work offline
"""
import json
import random
from datetime import datetime, timedelta

# Generate weekly measles cases data (time series)
print("Generating measles weekly cases data...")
measles_weekly = []
start_date = datetime(2020, 1, 6)  # First Monday of 2020

# Simulate measles outbreak patterns over 4 years
for week in range(200):  # About 4 years of weekly data
    date = start_date + timedelta(weeks=week)

    # Simulate seasonal pattern with outbreak in 2023-2024
    base_value = 2 + 3 * abs(week % 52 - 26) / 26  # Seasonal variation
    if 150 < week < 180:  # Simulate outbreak
        base_value *= 5

    # Add some randomness
    cases = max(0, base_value + random.gauss(0, 2))

    measles_weekly.append({
        "date": date.strftime("%Y-%m-%d"),
        "metric": "Measles_cases_countByWeek",
        "metric_value": round(cases, 1),
        "theme": "infectious_disease",
        "sub_theme": "vaccine_preventable",
        "topic": "Measles",
        "geography_type": "Nation",
        "geography": "England"
    })

with open("measles_weekly.json", "wt") as f:
    json.dump(measles_weekly, f, indent=2)
print(f"Generated {len(measles_weekly)} weekly data points")

# Generate age distribution data
print("\nGenerating measles age distribution data...")
age_groups = ["0_to_4", "5_to_9", "10_to_14", "15_to_19", "20_to_24",
              "25_to_44", "45_to_64", "65+"]
measles_age = []

for week in range(200):
    date = start_date + timedelta(weeks=week)

    for age in age_groups:
        # Different age groups have different susceptibility
        if age in ["0_to_4", "5_to_9", "10_to_14"]:
            base = 40  # Higher in unvaccinated children
        elif age in ["15_to_19", "20_to_24"]:
            base = 25
        elif age == "25_to_44":
            base = 20
        else:
            base = 10  # Lower in older adults

        # Add outbreak effect
        if 150 < week < 180:
            base *= 3

        value = max(0, base + random.gauss(0, 5))

        measles_age.append({
            "date": date.strftime("%Y-%m-%d"),
            "metric": "Measles_cases_ageBreakdown",
            "metric_value": round(value, 1),
            "stratum": age,
            "theme": "infectious_disease",
            "sub_theme": "vaccine_preventable",
            "topic": "Measles",
            "geography_type": "Nation",
            "geography": "England"
        })

with open("measles_age.json", "wt") as f:
    json.dump(measles_age, f, indent=2)
print(f"Generated {len(measles_age)} age distribution data points")

# Generate regional data
print("\nGenerating regional measles data...")
regions = ["London", "South East", "South West", "East of England",
           "West Midlands", "East Midlands", "Yorkshire and The Humber",
           "North West", "North East"]
measles_regional = []

for week in range(200):
    date = start_date + timedelta(weeks=week)

    for region in regions:
        # Different regions have different case rates
        base = random.uniform(1, 5)

        # London has higher rates
        if region == "London":
            base *= 1.5

        # Outbreak affects all regions but more in urban areas
        if 150 < week < 180:
            multiplier = 4 if region in ["London", "West Midlands"] else 3
            base *= multiplier

        value = max(0, base + random.gauss(0, 1))

        measles_regional.append({
            "date": date.strftime("%Y-%m-%d"),
            "metric": "Measles_cases_countByWeek",
            "metric_value": round(value, 1),
            "stratum": region,
            "theme": "infectious_disease",
            "sub_theme": "vaccine_preventable",
            "topic": "Measles",
            "geography_type": "Region",
            "geography": region
        })

with open("measles_regional.json", "wt") as f:
    json.dump(measles_regional, f, indent=2)
print(f"Generated {len(measles_regional)} regional data points")

print("\nData generation complete!")
print("Files created:")
print("  - measles_weekly.json (time series)")
print("  - measles_age.json (age distribution)")
print("  - measles_regional.json (regional breakdown)")
