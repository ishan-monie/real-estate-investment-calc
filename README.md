# Description

This project is a Real Estate Deal Analyzer built with Flask. It allows users to calculate the Maximum Allowable Offer (MAO) for a property based on After Repair Value (ARV), rehab costs, investor ROI requirements, transaction costs, and wholesale fees. The app provides additional metrics such as profit margin, cost per square foot, and buyer entry fees.

Users can:

Input property details and get investment calculations instantly.

Save, retrieve, and delete property records (in-memory, can be extended to a database).

View market insights with sample ARV ranges, monthly trends, and ROI distributions for visualization.

This tool is designed for real estate wholesalers, investors, and analysts who need a quick way to evaluate deals.

# README
Real Estate Deal Analyzer
1. Features

MAO Calculator: Enter property details to get wholesale calculations.

Save & Manage Properties: Save property analyses, retrieve them, or delete them.

Market Insights API: Provides sample data for charts (e.g., ARV per square foot, monthly trends, ROI distribution).

JSON Responses: All calculation and storage endpoints return JSON, making it easy to integrate with front-end charts and dashboards.

2. Installation
# Clone the repository
git clone https://github.com/your-username/deal-analyzer.git
cd deal-analyzer

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install flask

3. Usage

Run the app:

python app.py


Access it in the browser:

http://127.0.0.1:5000/

4. API Endpoints

/ → Renders index page (placeholder HTML).

/calculate [POST] → Calculates MAO and related metrics.

Input (form data):

address, square_feet, arv, transaction_percent,
investor_roi_percent, rehab_ppsf, wholesale_fee

Output (JSON): Property calculations and metrics.

/save_property [POST] → Save a property result.

Input: JSON payload (property data).

Output: { "success": true, "id": <property_id> }

/get_saved_properties [GET] → Retrieve all saved properties.

/delete_property/<id> [DELETE] → Delete a saved property by ID.

/market_insights [GET] → Returns mock data for ARV, trends, and ROI distribution.

5. Example API Request
curl -X POST http://127.0.0.1:5000/calculate \
  -d "address=123 Main St" \
  -d "square_feet=1500" \
  -d "arv=250000" \
  -d "transaction_percent=6" \
  -d "investor_roi_percent=20" \
  -d "rehab_ppsf=50" \
  -d "wholesale_fee=10000"


Response:

{
  "address": "123 Main St",
  "square_feet": 1500,
  "arv": 250000,
  "transaction_cost": 235000.0,
  "investor_roi": 200000.0,
  "rehab_cost": 75000.0,
  "mao": -260000.0,
  "wholesale_fee": 10000.0,
  "buyer_entry_fee": -250000.0,
  "total_costs": 510000.0,
  "profit_margin": -104.0,
  "cost_per_sqft": 340.0,
  "timestamp": "2025-09-19T10:00:00"
}

6. Notes

This version uses in-memory storage; data will reset on restart. For production, connect to a database (e.g., SQLite, PostgreSQL, MongoDB).

Add authentication and validation for real-world use.

Extend the /market_insights endpoint with live market data.
