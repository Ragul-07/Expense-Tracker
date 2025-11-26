from flask import Flask, render_template, request, redirect, url_for
from database import init_db, add_expense, get_all_expenses, update_expense, delete_expense

app = Flask(__name__)

# Initialize DB and table on startup
init_db()

@app.route('/')
def home():
    expenses = get_all_expenses()
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        amount = float(request.form['amount'])
        category = request.form['category']
        date = request.form['date']
        add_expense(name, amount, category, date)
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route('/update/<int:expense_id>', methods=['GET', 'POST'])
def update(expense_id):
    if request.method == 'POST':
        name = request.form['name']
        amount = float(request.form['amount'])
        category = request.form['category']
        date = request.form['date']
        update_expense(expense_id, name, amount, category, date)
        return redirect(url_for('home'))
    # Pre-fill form with existing data
    expenses = get_all_expenses()
    expense = next((e for e in expenses if e[0] == expense_id), None)
    return render_template('add.html', expense=expense)

@app.route('/delete/<int:expense_id>')
def delete(expense_id):
    delete_expense(expense_id)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
