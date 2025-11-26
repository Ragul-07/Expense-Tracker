from flask import Flask, render_template, request, redirect, url_for
from database import init_db, add_expense, get_all_expenses, update_expense, delete_expense

app = Flask(__name__)

# Initialize the database and create table if missing
init_db()

@app.route('/')
def home():
    expenses = get_all_expenses()
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    amount = float(request.form['amount'])
    category = request.form['category']
    date = request.form['date']
    add_expense(name, amount, category, date)
    return redirect(url_for('home'))

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    name = request.form['name']
    amount = float(request.form['amount'])
    category = request.form['category']
    date = request.form['date']
    update_expense(id, name, amount, category, date)
    return redirect(url_for('home'))

@app.route('/delete/<int:id>')
def delete(id):
    delete_expense(id)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
