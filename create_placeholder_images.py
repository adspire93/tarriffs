import json
import os
from PIL import Image, ImageDraw, ImageFont
import textwrap

# Load the processed data
with open('dashboard/data.json', 'r') as f:
    segment_data = json.load(f)

def create_luxury_placeholder(car_name, segment, filepath):
    """Create a luxury-themed placeholder image"""
    # Create a gradient-like black image
    img = Image.new('RGB', (800, 600), color=(15, 15, 15))
    draw = ImageDraw.Draw(img)

    # Add subtle gradient effect with rectangles
    for i in range(0, 600, 20):
        darkness = 15 + (i // 30)
        draw.rectangle([0, i, 800, i+20], fill=(darkness, darkness, darkness))

    # Add gold accent lines
    gold = (218, 165, 32)
    silver = (192, 192, 192)

    # Top border
    draw.rectangle([0, 0, 800, 5], fill=gold)
    # Bottom border
    draw.rectangle([0, 595, 800, 600], fill=gold)

    # Add segment name at top
    try:
        # Try to load a larger font, fallback to default if not available
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
        car_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)
        small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
    except:
        title_font = ImageFont.load_default()
        car_font = ImageFont.load_default()
        small_font = ImageFont.load_default()

    # Draw segment name
    segment_bbox = draw.textbbox((0, 0), segment, font=title_font)
    segment_width = segment_bbox[2] - segment_bbox[0]
    draw.text((400 - segment_width//2, 40), segment, fill=gold, font=title_font)

    # Draw car name (handle long names)
    car_display_name = car_name[:50]  # Limit length
    # Wrap text if too long
    if len(car_display_name) > 30:
        words = car_display_name.split()
        lines = []
        current_line = []
        for word in words:
            current_line.append(word)
            test_line = ' '.join(current_line)
            bbox = draw.textbbox((0, 0), test_line, font=car_font)
            if bbox[2] - bbox[0] > 700:
                current_line.pop()
                lines.append(' '.join(current_line))
                current_line = [word]
        if current_line:
            lines.append(' '.join(current_line))

        # Draw wrapped lines
        y_offset = 250
        for line in lines[:3]:  # Max 3 lines
            bbox = draw.textbbox((0, 0), line, font=car_font)
            line_width = bbox[2] - bbox[0]
            draw.text((400 - line_width//2, y_offset), line, fill=silver, font=car_font)
            y_offset += 45
    else:
        car_bbox = draw.textbbox((0, 0), car_display_name, font=car_font)
        car_width = car_bbox[2] - car_bbox[0]
        draw.text((400 - car_width//2, 280), car_display_name, fill=silver, font=car_font)

    # Add decorative elements
    # Corner accents
    accent_size = 40
    # Top left
    draw.line([20, 80, 20+accent_size, 80], fill=gold, width=2)
    draw.line([20, 80, 20, 80+accent_size], fill=gold, width=2)
    # Top right
    draw.line([780-accent_size, 80, 780, 80], fill=gold, width=2)
    draw.line([780, 80, 780, 80+accent_size], fill=gold, width=2)
    # Bottom left
    draw.line([20, 520-accent_size, 20, 520], fill=gold, width=2)
    draw.line([20, 520, 20+accent_size, 520], fill=gold, width=2)
    # Bottom right
    draw.line([780, 520-accent_size, 780, 520], fill=gold, width=2)
    draw.line([780-accent_size, 520, 780, 520], fill=gold, width=2)

    # Add luxury car icon/text at bottom
    tagline = "ZYPPYS LUXURY RENTALS"
    tagline_bbox = draw.textbbox((0, 0), tagline, font=small_font)
    tagline_width = tagline_bbox[2] - tagline_bbox[0]
    draw.text((400 - tagline_width//2, 540), tagline, fill=gold, font=small_font)

    img.save(filepath)
    print(f"Created placeholder: {car_name[:40]}...")

# Create images for each car
image_mapping = {}

for segment, cars in segment_data.items():
    print(f"\nCreating images for segment: {segment}")
    image_mapping[segment] = []

    for idx, car in enumerate(cars):
        safe_filename = f"{segment.replace('/', '_').replace(' ', '_')}_{idx}.jpg"
        filepath = f"dashboard/images/{safe_filename}"

        create_luxury_placeholder(car['name'], segment, filepath)

        image_mapping[segment].append({
            'car_name': car['name'],
            'image': safe_filename
        })

# Save image mapping
with open('dashboard/image_mapping.json', 'w') as f:
    json.dump(image_mapping, f, indent=2)

print("\n✓ All placeholder images created successfully!")
print(f"Total images created: {sum(len(cars) for cars in image_mapping.values())}")
