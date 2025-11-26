# database.py
import sqlite3

def init_db():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS expenses
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT NOT NULL,
                  amount REAL NOT NULL,
                  category TEXT,
                  date TEXT)''')
    conn.commit()
    conn.close()

def add_expense(title, amount, category, date):
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("INSERT INTO expenses (title, amount, category, date) VALUES (?, ?, ?, ?)",
              (title, amount, category, date))
    conn.commit()
    conn.close()

def get_all_expenses():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("SELECT * FROM expenses")
    rows = c.fetchall()
    conn.close()
    return rows

def update_expense(expense_id, title, amount, category, date):
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("UPDATE expenses SET title=?, amount=?, category=?, date=? WHERE id=?",
              (title, amount, category, date, expense_id))
    conn.commit()
    conn.close()

def delete_expense(expense_id):
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
    conn.commit()
    conn.close()
