// Load data when page loads
let segmentData = {};
let imageMapping = {};
let currentView = 'grid'; // 'grid' or 'table'

// Initialize the dashboard
async function init() {
    try {
        // Load data
        const dataResponse = await fetch('data.json');
        segmentData = await dataResponse.json();

        const imageResponse = await fetch('image_mapping.json');
        imageMapping = await imageResponse.json();

        // Get current page segment from URL or show all
        const urlParams = new URLSearchParams(window.location.search);
        const segment = urlParams.get('segment');

        if (segment && segmentData[segment]) {
            displaySegment(segment);
        } else {
            displayAllSegments();
        }

        // Update active nav button
        updateActiveNav(segment);
    } catch (error) {
        console.error('Error loading data:', error);
        document.getElementById('content').innerHTML =
            '<p style="text-align: center; color: #DAA520; padding: 2rem;">Error loading data. Please refresh the page.</p>';
    }
}

// Display all segments (for home page)
function displayAllSegments() {
    const content = document.getElementById('content');
    let html = '';

    for (const [segmentName, cars] of Object.entries(segmentData)) {
        html += `
            <section class="segment-section" id="${segmentName.replace(/\s+/g, '-')}">
                <div class="segment-header">
                    <h2 class="segment-title">${segmentName}</h2>
                    <div class="segment-divider"></div>
                </div>
                ${generateCarGrid(segmentName, cars)}
            </section>
        `;
    }

    content.innerHTML = html;
}

// Display single segment
function displaySegment(segmentName) {
    const content = document.getElementById('content');
    const cars = segmentData[segmentName];

    if (!cars) {
        content.innerHTML = '<p style="text-align: center;">Segment not found.</p>';
        return;
    }

    let html = `
        <section class="segment-section">
            <div class="segment-header">
                <h2 class="segment-title">${segmentName}</h2>
                <div class="segment-divider"></div>
            </div>

            <div class="view-toggle">
                <button class="toggle-btn" onclick="toggleView()">
                    Switch to ${currentView === 'grid' ? 'Table' : 'Grid'} View
                </button>
            </div>

            <div id="grid-view">
                ${generateCarGrid(segmentName, cars)}
            </div>

            <div id="table-view" class="hidden">
                ${generateCarTable(segmentName, cars)}
            </div>
        </section>
    `;

    content.innerHTML = html;
}

// Generate car grid
function generateCarGrid(segmentName, cars) {
    const images = imageMapping[segmentName] || [];

    let html = '<div class="car-grid">';

    cars.forEach((car, index) => {
        const image = images[index]?.image || 'placeholder.jpg';

        html += `
            <div class="car-card">
                <img src="images/${image}" alt="${car.name}" class="car-image">
                <div class="car-info">
                    <h3 class="car-name">${car.name}</h3>
                    <table class="price-table">
                        <tr>
                            <td>8hrs / 80kms</td>
                            <td>₹${formatNumber(car.rate_8hrs_80kms)}</td>
                        </tr>
                        <tr>
                            <td>Extra Hour</td>
                            <td>₹${formatNumber(car.ext_hr)}</td>
                        </tr>
                        <tr>
                            <td>Extra Km</td>
                            <td>₹${formatNumber(car.ext_km)}</td>
                        </tr>
                        <tr>
                            <td>Airport Transfer</td>
                            <td>₹${formatNumber(car.airport_trf)}</td>
                        </tr>
                        <tr>
                            <td>Per Km (Intercity)</td>
                            <td>₹${formatNumber(car.per_km)}</td>
                        </tr>
                    </table>
                </div>
            </div>
        `;
    });

    html += '</div>';
    return html;
}

// Generate car table
function generateCarTable(segmentName, cars) {
    let html = `
        <div class="table-container">
            <table class="tariff-table">
                <thead>
                    <tr>
                        <th>Vehicle</th>
                        <th>8hrs/80kms</th>
                        <th>Extra Hour</th>
                        <th>Extra Km</th>
                        <th>Airport Transfer</th>
                        <th>Driver Bhatta</th>
                        <th>Intercity Min</th>
                        <th>Per Km</th>
                    </tr>
                </thead>
                <tbody>
    `;

    cars.forEach(car => {
        html += `
            <tr>
                <td>${car.name}</td>
                <td>₹${formatNumber(car.rate_8hrs_80kms)}</td>
                <td>₹${formatNumber(car.ext_hr)}</td>
                <td>₹${formatNumber(car.ext_km)}</td>
                <td>₹${formatNumber(car.airport_trf)}</td>
                <td>${car.driver_bhatta || '-'}</td>
                <td>${car.intercity_min || '-'}</td>
                <td>₹${formatNumber(car.per_km)}</td>
            </tr>
        `;
    });

    html += `
                </tbody>
            </table>
        </div>
    `;

    return html;
}

// Toggle between grid and table view
function toggleView() {
    const gridView = document.getElementById('grid-view');
    const tableView = document.getElementById('table-view');
    const toggleBtn = document.querySelector('.toggle-btn');

    if (currentView === 'grid') {
        gridView.classList.add('hidden');
        tableView.classList.remove('hidden');
        currentView = 'table';
        toggleBtn.textContent = 'Switch to Grid View';
    } else {
        gridView.classList.remove('hidden');
        tableView.classList.add('hidden');
        currentView = 'grid';
        toggleBtn.textContent = 'Switch to Table View';
    }
}

// Update active navigation button
function updateActiveNav(currentSegment) {
    const navButtons = document.querySelectorAll('.nav-btn');
    navButtons.forEach(btn => {
        const btnSegment = btn.getAttribute('data-segment');
        if (btnSegment === currentSegment || (!currentSegment && btnSegment === 'all')) {
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }
    });
}

// Format numbers with commas
function formatNumber(num) {
    if (num === null || num === undefined || num === 0 || isNaN(num)) {
        return '-';
    }
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', init);
