import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='your-password',   # 🔁 replace with your MySQL root password
    database='students'
)
cursor = conn.cursor()

def add_student():
    try:
        student_id = int(input("Enter student ID: "))
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        grade = input("Enter grade (e.g., 9A): ")
        query = "INSERT INTO student (student_id, Name, Age, Grade) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (student_id, name, age, grade))
        conn.commit()
        print("✅ Student added.")
    except Exception as e:
        print("❌ Error:", e)

def update_student():
    try:
        student_id = int(input("Enter student ID to update: "))
        name = input("Enter new name: ")
        age = int(input("Enter new age: "))
        grade = input("Enter new grade: ")
        query = "UPDATE student SET Name=%s, Age=%s, Grade=%s WHERE student_id=%s"
        cursor.execute(query, (name, age, grade, student_id))
        conn.commit()
        if cursor.rowcount == 0:
            print("⚠️ No student found with that ID.")
        else:
            print("✅ Student updated.")
    except Exception as e:
        print("❌ Error:", e)

def delete_student():
    try:
        student_id = int(input("Enter student ID to delete: "))
        cursor.execute("DELETE FROM student WHERE student_id = %s", (student_id,))
        conn.commit()
        if cursor.rowcount == 0:
            print("⚠️ No student found with that ID.")
        else:
            print("🗑️ Student deleted.")
    except Exception as e:
        print("❌ Error:", e)

def view_students():
    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()
    print("\n📋 All Students:")
    print("ID | Name              | Age | Grade")
    print("-" * 40)
    for row in rows:
        print(f"{row[0]:<3} | {row[1]:<17} | {row[2]:<3} | {row[3]}")
    print()

def main_menu():
    while True:
        print("\n🎓 Student Management Menu")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Students")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            update_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            view_students()
        elif choice == '5':
            print("👋 Exiting.")
            break
        else:
            print("❗ Invalid choice. Try again.")

# Run the menu
main_menu()

# Close connection
cursor.close()
conn.close()
