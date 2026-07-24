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
              CREATE TABLE IF NOT EXISTS ExPRNSE (
              id INTEGER PRIMARY KEY)
              """)



print("EEEE")