import sqlite3
import datetime

def create_table():
    conn = sqlite3.connect('sheep_health.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sheep_health (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sheep_id TEXT NOT NULL,
            date DATE NOT NULL,
            weight REAL,
            health_status TEXT
        )
    ''')
    conn.commit()
    conn.close()

create_table()

def add_health_record(sheep_id, date, weight, health_status):
    conn = sqlite3.connect('sheep_health.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO sheep_health (sheep_id, date, weight, health_status)
        VALUES (?, ?, ?, ?)
    ''', (sheep_id, date, weight, health_status))
    conn.commit()
    conn.close()

def modify_health_record(record_id, sheep_id, date, weight, health_status):
    conn = sqlite3.connect('sheep_health.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE sheep_health
        SET sheep_id = ?, date = ?, weight = ?, health_status = ?
        WHERE id = ?
    ''', (sheep_id, date, weight, health_status, record_id))
    conn.commit()
    conn.close()

def delete_health_record(record_id):
    conn = sqlite3.connect('sheep_health.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM sheep_health WHERE id = ?', (record_id,))
    conn.commit()
    conn.close()

while True:
    print("\nOptions:")
    print("1. Add Health Record")
    print("2. Modify Health Record")
    print("3. Delete Health Record")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        sheep_id = input("Enter sheep ID: ")
        date = input("Enter date (YYYY-MM-DD): ")
        weight = float(input("Enter weight: "))
        health_status = input("Enter health status: ")
        add_health_record(sheep_id, date, weight, health_status)
        print("Health record added successfully.")

    elif choice == "2":
        record_id = int(input("Enter the record ID to modify: "))
        sheep_id = input("Enter sheep ID: ")
        date = input("Enter date (YYYY-MM-DD): ")
        weight = float(input("Enter weight: "))
        health_status = input("Enter health status: ")
        modify_health_record(record_id, sheep_id, date, weight, health_status)
        print("Health record modified successfully.")

    elif choice == "3":
        record_id = int(input("Enter the record ID to delete: "))
        delete_health_record(record_id)
        print("Health record deleted successfully.")

    elif choice == "4":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")
