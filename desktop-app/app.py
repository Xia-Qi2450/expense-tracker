import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Initialize the database
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    description TEXT
)
""")
conn.commit()

# Create the main app class
class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        # Create a frame for inputs
        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)

        # Labels and entry fields
        tk.Label(input_frame, text="Date (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = tk.Entry(input_frame)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Amount:").grid(row=1, column=0, padx=5, pady=5)
        self.amount_entry = tk.Entry(input_frame)
        self.amount_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Category:").grid(row=2, column=0, padx=5, pady=5)
        self.category_entry = tk.Entry(input_frame)
        self.category_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Description:").grid(row=3, column=0, padx=5, pady=5)
        self.description_entry = tk.Entry(input_frame)
        self.description_entry.grid(row=3, column=1, padx=5, pady=5)

        # Add buttons
        tk.Button(input_frame, text="Add Expense", command=self.add_expense).grid(row=4, column=0, padx=5, pady=10)
        tk.Button(input_frame, text="View Expenses", command=self.load_expenses).grid(row=4, column=1, padx=5, pady=10)

        # Create a treeview for displaying expenses
        self.tree = ttk.Treeview(root, columns=("Date", "Amount", "Category", "Description"), show="headings")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Amount", text="Amount")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Description", text="Description")
        self.tree.pack(pady=10)

    def add_expense(self):
        date = self.date_entry.get()
        amount = self.amount_entry.get()
        category = self.category_entry.get()
        description = self.description_entry.get()

        if not date or not amount or not category:
            messagebox.showwarning("Input Error", "Please fill in all required fields!")
            return

        try:
            amount = float(amount)  # Ensure the amount is numeric
        except ValueError:
            messagebox.showerror("Input Error", "Amount must be a number!")
            return

        # Save to database
        cursor.execute("INSERT INTO expenses (date, amount, category, description) VALUES (?, ?, ?, ?)",
                       (date, amount, category, description))
        conn.commit()

        # Clear input fields
        self.date_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)

        # Refresh treeview
        self.load_expenses()

    def load_expenses(self):
        # Clear the current treeview
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Fetch data from the database
        cursor.execute("SELECT date, amount, category, description FROM expenses")
        for row in cursor.fetchall():
            self.tree.insert("", tk.END, values=row)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()
