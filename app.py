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
    
    deal = {
    'deal_id': len(lightning_deals) + 1,
    'product_name': product_name,
    'actual_price': actual_price,
    'final_price': final_price,
    'total_units': total_units,
    'expiry_time': expiry_time
}

    lightning_deals.append(deal)
    return jsonify({'message': 'Deal created successfully'})


@app.route('/admin/update_deal/<int:deal_id>', methods=['PUT'])
def update_deal(deal_id):
    data = request.get_json()
    # Find the deal with the given deal_id and update its attributes
    return jsonify({'message': 'Deal updated successfully'})



@app.route('/admin/approve_order/<int:order_id>', methods=['PUT'])
def approve_order(order_id):
    # Find the order with the given order_id and update its status to approved

    return jsonify({'message': 'Order approved successfully'})


@app.route('/customer/deals', methods=['GET'])
def get_deals():
    current_time = datetime.utcnow()
    unexpired_deals = [deal for deal in lightning_deals if deal['expiry_time'] > current_time]
    return jsonify({'deals': unexpired_deals})


@app.route('/customer/place_order', methods=['POST'])
def place_order():
    data = request.get_json()
    deal_id = data['deal_id']
    quantity = data['quantity']
    current_time = datetime.utcnow()
    deal = next((deal for deal in lightning_deals if deal['expiry_time'] > current_time and deal['deal_id'] == deal_id), None)
    if deal is None:
        return jsonify({'message': 'Deal not available or expired'})
    if quantity > deal['total_units']:
        return jsonify({'message': 'Not enough units available for the deal'})
    
    # Placing the order
    return jsonify({'message': 'Order placed successfully'})


@app.route('/customer/order_status/<int:order_id>', methods=['GET'])
def get_order_status(order_id):
    
    # Find the order with the given order_id and return its status
    return jsonify({'status': 'Order status'})


if __name__ == '__main__':
    app.run()
