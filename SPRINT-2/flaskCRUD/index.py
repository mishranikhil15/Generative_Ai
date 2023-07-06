from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Data stored in memory
contacts = []

@app.route('/')
def index():
    return render_template('index.html', contacts=contacts)

@app.route('/api/contacts', methods=['GET'])
def get_contacts():
    return jsonify(contacts)

@app.route('/api/contacts', methods=['POST'])
def create_contact():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    contact = {'name': name, 'email': email, 'phone': phone}
    contacts.append(contact)
    return jsonify(contact), 201

@app.route('/api/contacts/<int:index>', methods=['GET'])
def get_contact(index):
    if index < len(contacts):
        return jsonify(contacts[index])
    else:
        return jsonify({'error': 'Contact not found'}), 404

@app.route('/api/contacts/<int:index>', methods=['PATCH'])
def update_contact(index):
    if index < len(contacts):
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        contact = contacts[index]
        contact['name'] = name if name else contact['name']
        contact['email'] = email if email else contact['email']
        contact['phone'] = phone if phone else contact['phone']
        return jsonify(contact)
    else:
        return jsonify({'error': 'Contact not found'}), 404

@app.route('/api/contacts/<int:index>', methods=['DELETE'])
def delete_contact(index):
    if index < len(contacts):
        contact = contacts.pop(index)
        return jsonify(contact)
    else:
        return jsonify({'error': 'Contact not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
