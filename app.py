from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

# In-memory storage for property comparisons (in production, use a database)
saved_properties = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Get form data
        address = request.form.get('address', '')
        square_feet = float(request.form.get('square_feet', 0))
        arv = float(request.form.get('arv', 0))
        transaction_percent = float(request.form.get('transaction_percent', 0))
        investor_roi_percent = float(request.form.get('investor_roi_percent', 0))
        rehab_ppsf = float(request.form.get('rehab_ppsf', 0))
        wholesale_fee = float(request.form.get('wholesale_fee', 0))
        
        # Calculations
        transaction_cost = arv * (1 - transaction_percent / 100)
        investor_roi = arv * (1 - investor_roi_percent / 100)
        rehab_cost = rehab_ppsf * square_feet
        mao = arv - transaction_cost - investor_roi - rehab_cost - wholesale_fee
        buyer_entry_fee = mao + wholesale_fee
        
        # Additional calculations for charts
        total_costs = transaction_cost + investor_roi + rehab_cost
        profit_margin = (mao / arv) * 100 if arv > 0 else 0
        cost_per_sqft = total_costs / square_feet if square_feet > 0 else 0
        
        results = {
            'address': address,
            'square_feet': square_feet,
            'arv': arv,
            'transaction_cost': transaction_cost,
            'investor_roi': investor_roi,
            'rehab_cost': rehab_cost,
            'mao': mao,
            'wholesale_fee': wholesale_fee,
            'buyer_entry_fee': buyer_entry_fee,
            'total_costs': total_costs,
            'profit_margin': profit_margin,
            'cost_per_sqft': cost_per_sqft,
            'timestamp': datetime.now().isoformat()
        }
        
        return jsonify(results)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/save_property', methods=['POST'])
def save_property():
    try:
        data = request.json
        # Add unique ID
        data['id'] = len(saved_properties) + 1
        data['saved_at'] = datetime.now().isoformat()
        saved_properties.append(data)
        return jsonify({'success': True, 'id': data['id']})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/get_saved_properties')
def get_saved_properties():
    return jsonify(saved_properties)

@app.route('/delete_property/<int:property_id>', methods=['DELETE'])
def delete_property(property_id):
    global saved_properties
    saved_properties = [p for p in saved_properties if p['id'] != property_id]
    return jsonify({'success': True})

@app.route('/market_insights')
def market_insights():
    # Generate sample market data for charts
    market_data = {
        'avg_arv_by_sqft': [
            {'range': '500-1000', 'avg_arv': 120000, 'count': 15},
            {'range': '1000-1500', 'avg_arv': 180000, 'count': 25},
            {'range': '1500-2000', 'avg_arv': 240000, 'count': 20},
            {'range': '2000-2500', 'avg_arv': 300000, 'count': 18},
            {'range': '2500+', 'avg_arv': 400000, 'count': 12}
        ],
        'monthly_trends': [
            {'month': 'Jan', 'avg_mao': 85000, 'avg_profit': 25000},
            {'month': 'Feb', 'avg_mao': 87000, 'avg_profit': 26000},
            {'month': 'Mar', 'avg_mao': 90000, 'avg_profit': 28000},
            {'month': 'Apr', 'avg_mao': 92000, 'avg_profit': 27000},
            {'month': 'May', 'avg_mao': 95000, 'avg_profit': 29000},
            {'month': 'Jun', 'avg_mao': 98000, 'avg_profit': 31000}
        ],
        'roi_distribution': [
            {'range': '10-15%', 'count': 8, 'color': '#ff6b6b'},
            {'range': '15-20%', 'count': 15, 'color': '#4ecdc4'},
            {'range': '20-25%', 'count': 22, 'color': '#45b7d1'},
            {'range': '25-30%', 'count': 18, 'color': '#96ceb4'},
            {'range': '30%+', 'count': 12, 'color': '#ffeaa7'}
        ]
    }
    return jsonify(market_data)

if __name__ == '__main__':
    app.run(debug=True)
