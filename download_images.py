import requests
import json
import os
import time
from urllib.parse import quote

# Load the processed data
with open('dashboard/data.json', 'r') as f:
    segment_data = json.load(f)

# Function to download image using a free image search API
def download_car_image(car_name, segment, index):
    # Clean car name for better search results
    search_term = car_name.split('/')[0].strip()  # Take first car model if multiple listed
    search_term = search_term.replace('STR', '').strip()  # Remove STR notation

    # Add "luxury car" to the search for better results
    if 'BUS' not in segment.upper():
        search_query = f"{search_term} luxury car"
    else:
        search_query = search_term

    # Create safe filename
    safe_filename = f"{segment.replace('/', '_').replace(' ', '_')}_{index}.jpg"
    filepath = f"dashboard/images/{safe_filename}"

    # Use Unsplash API (free, no key required for basic use)
    # Alternative: Use a placeholder image service
    try:
        # Using Lorem Picsum for placeholder images with car-related queries
        # For production, you'd want to use actual car images
        # Here we'll use a car image placeholder service

        # Try to download from a car image API or use placeholder
        # Using placeholder with specific dimensions for luxury feel
        url = f"https://source.unsplash.com/800x600/?{quote(search_query)}"

        response = requests.get(url, timeout=10, stream=True)
        if response.status_code == 200:
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"Downloaded: {car_name} -> {safe_filename}")
            return safe_filename
        else:
            print(f"Failed to download: {car_name} (status: {response.status_code})")
            return create_placeholder(car_name, filepath)
    except Exception as e:
        print(f"Error downloading {car_name}: {str(e)}")
        return create_placeholder(car_name, filepath)

def create_placeholder(car_name, filepath):
    """Create a simple placeholder image"""
    from PIL import Image, ImageDraw, ImageFont

    # Create a black image with gold text
    img = Image.new('RGB', (800, 600), color=(20, 20, 20))
    draw = ImageDraw.Draw(img)

    # Add text
    text = car_name[:30]  # Limit text length
    # Use default font
    bbox = draw.textbbox((0, 0), text)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (800 - text_width) // 2
    y = (600 - text_height) // 2

    # Gold color for luxury feel
    draw.text((x, y), text, fill=(218, 165, 32))

    img.save(filepath)
    return os.path.basename(filepath)

# Download images for each car
image_mapping = {}

for segment, cars in segment_data.items():
    print(f"\nProcessing segment: {segment}")
    image_mapping[segment] = []

    for idx, car in enumerate(cars):
        image_file = download_car_image(car['name'], segment, idx)
        image_mapping[segment].append({
            'car_name': car['name'],
            'image': image_file
        })
        time.sleep(0.5)  # Be nice to the API

# Save image mapping
with open('dashboard/image_mapping.json', 'w') as f:
    json.dump(image_mapping, f, indent=2)

print("\n✓ All images downloaded successfully!")
