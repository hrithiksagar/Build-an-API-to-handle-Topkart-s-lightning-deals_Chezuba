from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)
# Store lightning deals in memory for simplicity but generally we'll use a database
lightning_deals = []

@app.route('/admin/create_deal', methods=['POST'])
def create_deal():
    data = request.get_json()
    product_name = data['product_name']
    actual_price = data['actual_price']
    final_price = data['final_price']
    total_units = data['total_units']
    expiry_time = datetime.utcnow() + timedelta(hours=12)  # Expiry time is 12 hours from now UTC 00
