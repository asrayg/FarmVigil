import sqlite3
import datetime

def create_table():
    conn = sqlite3.connect('horse_health.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS horse_health (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            horse_id TEXT NOT NULL,
            date DATE NOT NULL,
            weight REAL,
            health_status TEXT
        )
    ''')
    conn.commit()
    conn.close()

create_table()

def add_health_record(horse_id, date, weight, health_status):
    conn = sqlite3.connect('horse_health.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO horse_health (horse_id, date, weight, health_status)
        VALUES (?, ?, ?, ?)
    ''', (horse_id, date, weight, health_status))
    conn.commit()
    conn.close()

def modify_health_record(record_id, horse_id, date, weight, health_status):
    conn = sqlite3.connect('horse_health.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE horse_health
        SET horse_id = ?, date = ?, weight = ?, health_status = ?
        WHERE id = ?
    ''', (horse_id, date, weight, health_status, record_id))
    conn.commit()
    conn.close()

def delete_health_record(record_id):
    conn = sqlite3.connect('horse_health.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM horse_health WHERE id = ?', (record_id,))
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
        horse_id = input("Enter horse ID: ")
        date = input("Enter date (YYYY-MM-DD): ")
        weight = float(input("Enter weight: "))
        health_status = input("Enter health status: ")
        add_health_record(horse_id, date, weight, health_status)
        print("Health record added successfully.")

    elif choice == "2":
        record_id = int(input("Enter the record ID to modify: "))
        horse_id = input("Enter horse ID: ")
        date = input("Enter date (YYYY-MM-DD): ")
        weight = float(input("Enter weight: "))
        health_status = input("Enter health status: ")
        modify_health_record(record_id, horse_id, date, weight, health_status)
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
