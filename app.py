from flask import Flask, render_template, request, jsonify
from database import init_db, add_expense, get_all_expenses, update_expense, delete_expense

app = Flask(__name__)

@app.route('/')
def home():
    expenses = get_all_expenses()
    return render_template("index.html", expenses=expenses)

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data received'}), 400

    amount = data.get('amount')
    category = data.get('category')
    note = data.get('note', '')

    if not amount or not category:
        return jsonify({'error': 'Amount and category are required'}), 400

    try:
        amount = float(amount)
    except ValueError:
        return jsonify({'error': 'Amount must be a number'}), 400

    id = add_expense(amount, category, note)
    return jsonify({
        'id': id,
        'amount': amount,
        'category': category,
        'note': note
    })

@app.route('/update/<int:expense_id>', methods=['POST'])
def update(expense_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data received'}), 400

    amount = data.get('amount')
    category = data.get('category')
    note = data.get('note', '')

    if not amount or not category:
        return jsonify({'error': 'Amount and category are required'}), 400

    try:
        amount = float(amount)
    except ValueError:
        return jsonify({'error': 'Amount must be a number'}), 400

    update_expense(expense_id, amount, category, note)
    return jsonify({'id': expense_id, 'amount': amount, 'category': category, 'note': note})

@app.route('/delete/<int:expense_id>', methods=['DELETE'])
def delete(expense_id):
    delete_expense(expense_id)
    return jsonify({'success': True})

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
