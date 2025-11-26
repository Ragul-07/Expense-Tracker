import sqlite3

DB_NAME = "expenses.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    """Create the expenses table if it doesn't exist"""
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT,
            date TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_expense(name, amount, category, date):
    conn = get_connection()
    c = conn.cursor()
    c.execute(
        "INSERT INTO expenses (name, amount, category, date) VALUES (?, ?, ?, ?)",
        (name, amount, category, date)
    )
    conn.commit()
    conn.close()

def get_all_expenses():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM expenses")
    expenses = c.fetchall()
    conn.close()
    return expenses

def update_expense(expense_id, name, amount, category, date):
    conn = get_connection()
    c = conn.cursor()
    c.execute(
        "UPDATE expenses SET name = ?, amount = ?, category = ?, date = ? WHERE id = ?",
        (name, amount, category, date, expense_id)
    )
    conn.commit()
    conn.close()

def delete_expense(expense_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()
