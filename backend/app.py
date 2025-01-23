from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Authentication
users = {"Jennifer": "330316", "Kevin": "671027"}

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

if __name__ == "__main__":
    app.run(debug=True)
