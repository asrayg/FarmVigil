import sqlite3
import datetime

def create_table():
    conn = sqlite3.connect('cow_health.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cow_health (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cow_id TEXT NOT NULL,
            date DATE NOT NULL,
            weight REAL,
            health_status TEXT
        )
    ''')
    conn.commit()
    conn.close()

create_table()


def add_health_record(cow_id, date, weight, health_status):
    conn = sqlite3.connect('cow_health.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO cow_health (cow_id, date, weight, health_status)
        VALUES (?, ?, ?, ?)
    ''', (cow_id, date, weight, health_status))
    conn.commit()
    conn.close()

def modify_health_record(record_id, cow_id, date, weight, health_status):
    conn = sqlite3.connect('cow_health.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE cow_health
        SET cow_id = ?, date = ?, weight = ?, health_status = ?
        WHERE id = ?
    ''', (cow_id, date, weight, health_status, record_id))
    conn.commit()
    conn.close()

def delete_health_record(record_id):
    conn = sqlite3.connect('cow_health.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM cow_health WHERE id = ?', (record_id,))
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
        cow_id = input("Enter cow ID: ")
        date = input("Enter date (YYYY-MM-DD): ")
        weight = float(input("Enter weight: "))
        health_status = input("Enter health status: ")
        add_health_record(cow_id, date, weight, health_status)
        print("Health record added successfully.")

    elif choice == "2":
        record_id = int(input("Enter the record ID to modify: "))
        cow_id = input("Enter cow ID: ")
        date = input("Enter date (YYYY-MM-DD): ")
        weight = float(input("Enter weight: "))
        health_status = input("Enter health status: ")
        modify_health_record(record_id, cow_id, date, weight, health_status)
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
