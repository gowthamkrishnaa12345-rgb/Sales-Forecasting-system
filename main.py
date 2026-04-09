import sqlite3
import tkinter as tk
from tkinter import messagebox

# Database setup
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    price REAL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Sales (
    sale_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    quantity INTEGER,
    sale_date TEXT
)
''')

conn.commit()

# Functions
def add_product():
    pid = entry_pid.get()
    name = entry_name.get()
    cat = entry_cat.get()
    price = entry_price.get()

    cursor.execute("INSERT INTO Products VALUES (?, ?, ?, ?)",
                   (pid, name, cat, price))
    conn.commit()
    messagebox.showinfo("Success", "Product Added")

def add_sales():
    sid = entry_sid.get()
    pid = entry_spid.get()
    qty = entry_qty.get()
    date = entry_date.get()

    cursor.execute("INSERT INTO Sales VALUES (?, ?, ?, ?)",
                   (sid, pid, qty, date))
    conn.commit()
    messagebox.showinfo("Success", "Sales Added")

def forecast():
    pid = entry_fpid.get()
    cursor.execute("SELECT AVG(quantity) FROM Sales WHERE product_id=?", (pid,))
    result = cursor.fetchone()[0]

    if result:
        messagebox.showinfo("Forecast", f"Predicted Sales: {round(result,2)}")
    else:
        messagebox.showerror("Error", "No data found")

# UI
root = tk.Tk()
root.title("Sales Forecasting System")
root.geometry("400x500")

# Product Section
tk.Label(root, text="Add Product").pack()

entry_pid = tk.Entry(root)
entry_pid.pack()
entry_pid.insert(0, "Product ID")

entry_name = tk.Entry(root)
entry_name.pack()
entry_name.insert(0, "Name")

entry_cat = tk.Entry(root)
entry_cat.pack()
entry_cat.insert(0, "Category")

entry_price = tk.Entry(root)
entry_price.pack()
entry_price.insert(0, "Price")

tk.Button(root, text="Add Product", command=add_product).pack(pady=5)

# Sales Section
tk.Label(root, text="Add Sales").pack()

entry_sid = tk.Entry(root)
entry_sid.pack()
entry_sid.insert(0, "Sale ID")

entry_spid = tk.Entry(root)
entry_spid.pack()
entry_spid.insert(0, "Product ID")

entry_qty = tk.Entry(root)
entry_qty.pack()
entry_qty.insert(0, "Quantity")

entry_date = tk.Entry(root)
entry_date.pack()
entry_date.insert(0, "YYYY-MM-DD")

tk.Button(root, text="Add Sales", command=add_sales).pack(pady=5)

# Forecast Section
tk.Label(root, text="Forecast").pack()

entry_fpid = tk.Entry(root)
entry_fpid.pack()
entry_fpid.insert(0, "Product ID")

tk.Button(root, text="Predict Sales", command=forecast).pack(pady=10)

root.mainloop()