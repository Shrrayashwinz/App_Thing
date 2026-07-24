"""
Program Name: main.py
Author: Shrrayash Srinivasan
Purpose: Main file for the expense tracker.
Date: July 20, 2026

"""

import sqlite3

def init_db():
    conn = sqlite3.connect("ExPRNSE")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()



print("EEEE")