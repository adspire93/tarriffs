import json

# Load segment data
with open('dashboard/data.json', 'r') as f:
    segment_data = json.load(f)

# HTML template for segment pages
def create_segment_page(segment_name, segment_id):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{segment_name} - Zyppys Luxury Car Rentals</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <!-- Header -->
    <header>
        <div class="header-content">
            <h1>Zyppys Hyderabad</h1>
            <p class="tagline">Luxury Car Rental Tariffs</p>
        </div>
    </header>

    <!-- Navigation -->
    <nav>
        <div class="nav-content">
            <a href="index.html" class="nav-btn">All Vehicles</a>
            <a href="royale.html" class="nav-btn" {"class='nav-btn active'" if segment_id == "royale" else ""}>Royale</a>
            <a href="exotic.html" class="nav-btn" {"class='nav-btn active'" if segment_id == "exotic" else ""}>Exotic/Sports</a>
            <a href="president.html" class="nav-btn" {"class='nav-btn active'" if segment_id == "president" else ""}>President</a>
            <a href="luxury_suv.html" class="nav-btn" {"class='nav-btn active'" if segment_id == "luxury_suv" else ""}>Luxury SUV</a>
            <a href="electric.html" class="nav-btn" {"class='nav-btn active'" if segment_id == "electric" else ""}>Electric</a>
            <a href="mpv.html" class="nav-btn" {"class='nav-btn active'" if segment_id == "mpv" else ""}>MPV</a>
            <a href="luxury_vans.html" class="nav-btn" {"class='nav-btn active'" if segment_id == "luxury_vans" else ""}>Luxury Vans</a>
            <a href="buses_nac.html" class="nav-btn" {"class='nav-btn active'" if segment_id == "buses_nac" else ""}>Buses N/AC</a>
            <a href="buses_ac.html" class="nav-btn" {"class='nav-btn active'" if segment_id == "buses_ac" else ""}>Buses A/C</a>
            <a href="ancilliary.html" class="nav-btn" {"class='nav-btn active'" if segment_id == "ancilliary" else ""}>Ancilliary</a>
            <a href="corporate.html" class="nav-btn" {"class='nav-btn active'" if segment_id == "corporate" else ""}>Corporate</a>
        </div>
    </nav>

    <!-- Main Content -->
    <main>
        <div id="content">
            <!-- Content will be loaded dynamically -->
        </div>
    </main>

    <!-- Footer -->
    <footer>
        <div class="footer-content">
            <p>&copy; 2025 Zyppys Hyderabad. All rights reserved.</p>
            <p style="margin-top: 0.5rem; font-size: 0.8rem;">
                Terms & Conditions apply | GST 18% extra | Toll, Parking & Permit charges extra
            </p>
        </div>
    </footer>

    <script src="js/app.js"></script>
    <script>
        // Auto-load this segment
        document.addEventListener('DOMContentLoaded', async function() {{
            const dataResponse = await fetch('data.json');
            const data = await dataResponse.json();

            const imageResponse = await fetch('image_mapping.json');
            const images = await imageResponse.json();

            window.segmentData = data;
            window.imageMapping = images;

            displaySegment('{segment_name}');
        }});
    </script>
</body>
</html>
'''

# Segment mappings
segment_mapping = {
    'ROYALE': 'royale',
    'EXOTIC / SPORTS': 'exotic',
    'PRESIDENT': 'president',
    'LUXURY SUV': 'luxury_suv',
    'ELECTRIC': 'electric',
    'MPV': 'mpv',
    'LUXURY VANS': 'luxury_vans',
    'BUSES N/AC': 'buses_nac',
    'BUSES A/C': 'buses_ac',
    'ANCILLIARY SERVICES': 'ancilliary',
    'CORPORATE': 'corporate'
}

# Generate pages
for segment_name, segment_id in segment_mapping.items():
    filename = f'dashboard/{segment_id}.html'
    with open(filename, 'w') as f:
        f.write(create_segment_page(segment_name, segment_id))
    print(f"Created: {filename}")

print("\n✓ All segment pages created successfully!")
