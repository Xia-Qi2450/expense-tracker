from flask import Flask, jsonify, request
import sqlite3

app = "https://expense-tracker-tjr9.onrender.com"
DB_NAME = "expenses.db"

# Authentication
users = {"Jennifer": "330316"}

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    if users.get(username) == password:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@app.route("/expenses", methods=["GET"])
def get_expenses():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT date, amount, category, description FROM expenses")
    expenses = cursor.fetchall()
    conn.close()
    return jsonify(expenses)

# Initialize database
def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            date TEXT,
                            amount REAL,
                            category TEXT,
                            description TEXT
                        )''')
    print("Database initialized!")

@app.route("/add_expense", methods=["POST"])
def add_expense():
    data = request.json
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO expenses (date, amount, category, description) VALUES (?, ?, ?, ?)",
                       (data['date'], data['amount'], data['category'], data['description']))
        conn.commit()
    return jsonify({"message": "Expense added successfully!"}), 201


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
