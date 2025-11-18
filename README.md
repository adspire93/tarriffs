# Zyppys Luxury Car Rental Dashboard

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/adspire93/tarriffs)

A premium luxury-themed dashboard displaying car rental tariffs for Zyppys Hyderabad. Features a sophisticated black and gold design with dedicated pages for each vehicle segment.

![Dashboard Preview](https://img.shields.io/badge/Vehicles-62-gold?style=for-the-badge) ![Segments](https://img.shields.io/badge/Segments-11-black?style=for-the-badge) ![Theme](https://img.shields.io/badge/Theme-Luxury%20Black-DAA520?style=for-the-badge)

## 🌟 Features

- **🎨 Luxury Black Theme** - Premium design with gold accents
- **🚗 62 Vehicle Models** - Comprehensive fleet coverage
- **📱 Fully Responsive** - Works on desktop, tablet, and mobile
- **🔄 Dual View Modes** - Grid view with images and Table view for comparison
- **📄 11 Dedicated Pages** - One page per vehicle segment
- **⚡ Fast Loading** - Optimized static site
- **🌍 Ready for Deployment** - Configured for Vercel

## 🚀 Quick Start

### View Locally

1. Clone the repository:
```bash
git clone https://github.com/adspire93/tarriffs.git
cd tarriffs
```

2. Open in browser:
```bash
# Option 1: Direct file access
open public/index.html

# Option 2: Local server
cd public
python3 -m http.server 8080
# Visit http://localhost:8080
```

### Deploy to Vercel (Recommended)

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/adspire93/tarriffs)

**Or manually:**

1. Fork/clone this repository
2. Sign up at [Vercel](https://vercel.com)
3. Import your repository
4. Set output directory to `public`
5. Deploy!

**Detailed deployment guide:** [VERCEL_DEPLOYMENT.md](VERCEL_DEPLOYMENT.md)

## 📋 Vehicle Segments

| Segment | Vehicles | Starting Price |
|---------|----------|----------------|
| 🏆 **Royale** | 4 | ₹18,900 |
| 🏎️ **Exotic/Sports** | 5 | ₹16,320 |
| 👔 **President** | 4 | ₹6,600 |
| 🚙 **Luxury SUV** | 9 | ₹5,400 |
| ⚡ **Electric** | 8 | ₹2,880 |
| 🚐 **MPV** | 7 | ₹3,240 |
| 🚌 **Luxury Vans** | 7 | ₹10,200 |
| 🚍 **Buses N/AC** | 3 | ₹5,400 |
| 🚌 **Buses A/C** | 10 | ₹5,760 |
| 🔧 **Ancilliary** | 2 | ₹6,000 |
| 💼 **Corporate** | 3 | ₹2,520 |

## 🎯 Pricing Information

Each vehicle displays:
- **8hrs/80kms** - Base rate for 8 hours and 80 kilometers
- **Extra Hour** - Additional hourly charges beyond 8 hours
- **Extra Km** - Per kilometer charge beyond 80 km
- **Airport Transfer** - Fixed airport transfer rate (~80km round trip)
- **Driver Bhatta** - Driver allowance per day
- **Intercity Minimum** - Minimum kilometers per day for intercity travel
- **Per Km Rate** - Per kilometer rate for intercity journeys

## 📁 Project Structure

```
tarriffs/
├── public/                    # Deployed to Vercel
│   ├── index.html            # Main dashboard (all vehicles)
│   ├── royale.html           # Royale segment page
│   ├── exotic.html           # Exotic/Sports segment page
│   ├── president.html        # President segment page
│   ├── luxury_suv.html       # Luxury SUV segment page
│   ├── electric.html         # Electric vehicles page
│   ├── mpv.html              # MPV segment page
│   ├── luxury_vans.html      # Luxury Vans page
│   ├── buses_nac.html        # Non-AC buses page
│   ├── buses_ac.html         # AC buses page
│   ├── ancilliary.html       # Ancilliary services page
│   ├── corporate.html        # Corporate vehicles page
│   ├── css/
│   │   └── styles.css        # Luxury black theme
│   ├── js/
│   │   └── app.js            # Dynamic functionality
│   ├── images/               # 62 vehicle images
│   ├── data.json             # Processed tariff data
│   └── image_mapping.json    # Vehicle-to-image mapping
├── dashboard/                # Original development folder
├── vercel.json               # Vercel configuration
├── package.json              # Project metadata
├── .vercelignore            # Deployment exclusions
└── README.md                 # This file
```

## 🛠️ Technical Stack

- **Frontend:** HTML5, CSS3, JavaScript (ES6+)
- **Styling:** Custom luxury theme with CSS gradients and animations
- **Data:** JSON-based static data
- **Images:** 62 custom-generated vehicle placeholders
- **Deployment:** Vercel (static hosting)
- **Data Processing:** Python (pandas, PIL)

## 🎨 Design Features

- **Color Scheme:**
  - Primary: Black (#0a0a0a, #1a1a1a)
  - Accent: Gold (#DAA520, #FFD700)
  - Text: Silver (#C0C0C0), White (#FFFFFF)

- **Typography:**
  - Headers: Bold, uppercase with letter-spacing
  - Body: Segoe UI, clean and readable

- **Layout:**
  - Responsive grid system
  - Card-based vehicle display
  - Sticky navigation
  - Smooth animations and transitions

## 📱 Browser Support

- ✅ Chrome (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## 🔧 Development

### Data Processing

The dashboard is built from `Zyppys HYD Rates(5).xlsx`:

```bash
# Process Excel data
python3 process_data.py

# Generate vehicle images
python3 create_placeholder_images.py

# Generate segment pages
python3 generate_pages.py
```

### Local Development

```bash
# Serve locally
cd public
python3 -m http.server 8080

# Or use Vercel CLI for exact production replica
vercel dev
```

## 📝 Important Notes

- All rates are in Indian Rupees (₹)
- **GST 18%** charged extra as per government norms
- Toll taxes, parking charges, and border taxes are extra at actuals
- Driver bhatta applicable on per calendar day basis
- Terms & Conditions apply (see footer on dashboard)

## 🚀 Deployment

### Vercel (Recommended)

1. Push code to GitHub
2. Connect repository to Vercel
3. Auto-deploys on every push
4. Get a free `.vercel.app` domain
5. Optional: Add custom domain

**Full Guide:** [VERCEL_DEPLOYMENT.md](VERCEL_DEPLOYMENT.md)

### Other Platforms

The dashboard is a static site and can be deployed anywhere:
- **Netlify:** Drag & drop the `public` folder
- **GitHub Pages:** Push `public` folder to gh-pages branch
- **AWS S3:** Upload `public` folder contents
- **Any static hosting:** FTP upload `public` folder

## 📊 Features Breakdown

| Feature | Status | Description |
|---------|--------|-------------|
| Luxury Theme | ✅ | Black & gold premium design |
| Vehicle Images | ✅ | 62 custom placeholder images |
| Segment Pages | ✅ | 11 dedicated HTML pages |
| Grid View | ✅ | Visual card layout |
| Table View | ✅ | Detailed comparison table |
| Responsive | ✅ | Mobile, tablet, desktop |
| Fast Loading | ✅ | Optimized static files |
| Navigation | ✅ | Sticky nav with smooth scroll |
| Data Accuracy | ✅ | From official Excel file |

## 📄 Documentation

- **[VERCEL_DEPLOYMENT.md](VERCEL_DEPLOYMENT.md)** - Complete Vercel deployment guide
- **[DASHBOARD_SUMMARY.md](DASHBOARD_SUMMARY.md)** - Project summary and features
- **[public/README.md](public/README.md)** - Dashboard user guide

## 🔗 Links

- **Live Demo:** [Deploy your own →](https://vercel.com/new/clone?repository-url=https://github.com/adspire93/tarriffs)
- **Repository:** [github.com/adspire93/tarriffs](https://github.com/adspire93/tarriffs)
- **Issues:** [Report bugs or request features](https://github.com/adspire93/tarriffs/issues)

## 📧 Contact

For inquiries about Zyppys car rentals:
- **Website:** [Visit Zyppys](#)
- **Location:** Hyderabad, India

## 📜 License

This project is created for Zyppys Hyderabad.

---

<div align="center">

**Built with ❤️ for Zyppys Hyderabad**

[⭐ Star this repo](https://github.com/adspire93/tarriffs) | [🚀 Deploy Now](https://vercel.com/new/clone?repository-url=https://github.com/adspire93/tarriffs) | [📖 Documentation](VERCEL_DEPLOYMENT.md)

</div>
