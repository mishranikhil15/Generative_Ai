from flask import Flask, jsonify, request

app = Flask(__name__)

# Data structure to store menu items
menu = []

# Data structure to store orders
orders = []

# Counter for generating unique order IDs
order_id_counter = 1


@app.route('/menu', methods=['GET', 'POST'])
def get_menu():
    if request.method == 'GET':
        return jsonify(menu)
    elif request.method == 'POST':
        dish = request.get_json()
        menu.append(dish)
        return jsonify({'message': 'Dish added successfully.'})


@app.route('/menu/<dish_id>', methods=['PATCH', 'DELETE'])
def update_or_remove_dish(dish_id):
    if request.method == 'PATCH':
        availability = request.json.get('availability')
        for dish in menu:
            if dish['dish_id'] == dish_id:
                dish['availability'] = availability
                return jsonify({'message': 'Dish availability updated successfully.'})
        return jsonify({'message': 'Dish not found.'}), 404
    elif request.method == 'DELETE':
        for dish in menu:
            if dish['dish_id'] == dish_id:
                menu.remove(dish)
                return jsonify({'message': 'Dish removed successfully.'})
        return jsonify({'message': 'Dish not found.'}), 404


@app.route('/order', methods=['POST'])
def place_order():
    order = request.get_json()
    dish_ids = order.get('dish_ids', [])
    for dish_id in dish_ids:
        dish = next((dish for dish in menu if dish['dish_id'] == dish_id), None)
        if not dish or dish['availability'] != 'yes':
            return jsonify({'message': 'Invalid dish ID or dish not available.'}), 400
    global order_id_counter
    new_order = {
        'order_id': order_id_counter,
        'customer_name': order['customer_name'],
        'dish_ids': dish_ids,
        'status': 'received'
    }
    orders.append(new_order)
    order_id_counter += 1
    return jsonify({'message': 'Order placed successfully.', 'order_id': new_order['order_id']})


@app.route('/order/<order_id>', methods=['PATCH'])
def update_order_status(order_id):
    new_status = request.json.get('status')
    for order in orders:
        if order['order_id'] == int(order_id):
            order['status'] = new_status
            return jsonify({'message': 'Order status updated successfully.'})
    return jsonify({'message': 'Order not found.'}), 404


@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)


@app.route('/exit', methods=['GET'])
def exit_app():
    return jsonify({'message': 'Application exited.'})


if __name__ == '__main__':
    app.run(debug=True)
