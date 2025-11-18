# Zyppys Luxury Car Rental Dashboard

A premium black-themed dashboard displaying luxury car rental tariffs for Zyppys Hyderabad.

## Features

- **Luxury Black Theme**: Premium design with gold accents representing luxury car rentals
- **Dedicated Segment Pages**: Each vehicle segment has its own dedicated page
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Dual View Modes**: Toggle between grid view (with car images) and table view (detailed comparison)
- **62 Vehicle Models**: Comprehensive coverage across 11 segments

## Segments

1. **Royale**: Premium sedans (BMW 740i, Mercedes S Class, etc.)
2. **Exotic/Sports**: High-performance vehicles (Porsche, Audi RS5, etc.)
3. **President**: Executive sedans (Mercedes E Class, Lexus, etc.)
4. **Luxury SUV**: Premium SUVs (Range Rover, Mercedes GLS, etc.)
5. **Electric**: Electric vehicles (BMW iX, Mercedes EQS, BYD, etc.)
6. **MPV**: Multi-purpose vehicles (Kia Carnival, Toyota Innova, etc.)
7. **Luxury Vans**: Premium vans (Mercedes V Class, Toyota Vellfire, etc.)
8. **Buses N/AC**: Non-AC buses
9. **Buses A/C**: Air-conditioned buses
10. **Ancilliary Services**: Recovery and support vehicles
11. **Corporate**: Economy corporate vehicles

## How to Use

### Option 1: Direct File Opening
1. Open `index.html` in your web browser
2. Navigate through different segments using the navigation bar
3. Click on any segment button to view dedicated page

### Option 2: Local Web Server (Recommended)
```bash
# Using Python 3
cd dashboard
python3 -m http.server 8000

# Then open http://localhost:8000 in your browser
```

### Option 3: Dedicated Segment Pages
Access individual segment pages directly:
- `royale.html` - Royale segment
- `exotic.html` - Exotic/Sports segment
- `president.html` - President segment
- `luxury_suv.html` - Luxury SUV segment
- `electric.html` - Electric vehicles
- `mpv.html` - MPV segment
- `luxury_vans.html` - Luxury Vans
- `buses_nac.html` - Non-AC buses
- `buses_ac.html` - AC buses
- `ancilliary.html` - Ancilliary services
- `corporate.html` - Corporate vehicles

## Tariff Information Displayed

Each vehicle shows:
- **8hrs/80kms**: Base rate for 8 hours and 80 kilometers
- **Extra Hour**: Charge per additional hour beyond 8 hours
- **Extra Km**: Charge per additional kilometer beyond 80 km
- **Airport Transfer**: Fixed rate for airport transfers (~80 km round trip)
- **Driver Bhatta**: Driver allowance
- **Intercity Minimum**: Minimum kilometers per day for intercity travel
- **Per Km**: Per kilometer rate for intercity travel

## Important Notes

- All rates are in Indian Rupees (₹)
- GST 18% is charged extra as per government norms
- Toll taxes, parking charges, and border taxes are extra at actuals
- Driver bhatta is applicable on a per calendar day basis
- Terms & Conditions apply

## File Structure

```
dashboard/
├── index.html          # Main dashboard page
├── royale.html         # Royale segment page
├── exotic.html         # Exotic/Sports segment page
├── president.html      # President segment page
├── luxury_suv.html     # Luxury SUV segment page
├── electric.html       # Electric segment page
├── mpv.html           # MPV segment page
├── luxury_vans.html   # Luxury Vans segment page
├── buses_nac.html     # Buses N/AC segment page
├── buses_ac.html      # Buses A/C segment page
├── ancilliary.html    # Ancilliary segment page
├── corporate.html     # Corporate segment page
├── css/
│   └── styles.css     # Luxury black theme styles
├── js/
│   └── app.js         # Dashboard functionality
├── images/            # Car images (62 images)
├── data.json          # Processed tariff data
└── image_mapping.json # Image-to-vehicle mapping
```

## Browser Compatibility

- Chrome (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers

## Credits

Created for Zyppys Hyderabad
Data source: Zyppys HYD Rates(5).xlsx
