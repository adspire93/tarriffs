import pandas as pd
import requests
import json
import os
from urllib.parse import quote

# Read the Excel file
df = pd.read_excel('Zyppys HYD Rates(5).xlsx')

# Define segment ranges based on the data analysis
segments = {
    'ROYALE': (4, 7),
    'EXOTIC / SPORTS': (10, 14),
    'PRESIDENT': (17, 20),
    'LUXURY SUV': (23, 31),
    'ELECTRIC': (34, 41),
    'MPV': (45, 51),
    'LUXURY VANS': (54, 60),
    'BUSES N/AC': (63, 65),
    'BUSES A/C': (68, 77),
    'ANCILLIARY SERVICES': (80, 81),
    'CORPORATE': (84, 86)
}

# Process data for each segment
segment_data = {}

for segment_name, (start, end) in segments.items():
    segment_cars = []
    for idx in range(start, end + 1):
        car_name = str(df.iloc[idx, 0])
        if car_name and car_name != 'nan' and car_name.strip():
            car_data = {
                'name': car_name,
                'rate_8hrs_80kms': df.iloc[idx, 1],
                'ext_hr': df.iloc[idx, 2],
                'ext_km': df.iloc[idx, 3],
                'airport_trf': df.iloc[idx, 4],
                'driver_bhatta': df.iloc[idx, 5],
                'intercity_min': df.iloc[idx, 6],
                'per_km': df.iloc[idx, 7],
                'driver_bhatta_intercity': df.iloc[idx, 8]
            }
            segment_cars.append(car_data)

    if segment_cars:
        segment_data[segment_name] = segment_cars

# Save processed data as JSON
with open('dashboard/data.json', 'w') as f:
    json.dump(segment_data, f, indent=2)

print("Data processed successfully!")
print(f"Total segments: {len(segment_data)}")
for segment, cars in segment_data.items():
    print(f"  {segment}: {len(cars)} cars")
