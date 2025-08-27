import sqlite3


def create_db():
    con = sqlite3.connect("enrollment.db")
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS students_tbl (
            EnrollID TEXT PRIMARY KEY,
            StudentName TEXT,
            StudentEmail TEXT,
            StudentPhone TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS courses_tbl (
            CourseCode TEXT PRIMARY KEY,
            CourseName TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS departments_tbl (
            DepartmentName TEXT PRIMARY KEY,
            DepartmentHead TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS instructors_tbl (
            InstructorID TEXT PRIMARY KEY,
            InstructorName TEXT,
            InstructorEmail TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS enrollment_tbl (
            EnrollID TEXT,
            CourseCode TEXT,
            InstructorID TEXT,
            FOREIGN KEY (EnrollID) REFERENCES students_tbl(EnrollID),
            FOREIGN KEY (CourseCode) REFERENCES courses_tbl(CourseCode),
            FOREIGN KEY (InstructorID) REFERENCES instructors_tbl(InstructorID)
        )
    """)

    con.commit()
    con.close()

def view_table(table):
    con = sqlite3.connect("enrollment.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM {table}")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    con.close()

def add_student():
    eid = input("EnrollID: ")
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    con = sqlite3.connect("enrollment.db")
    cur = con.cursor()
    cur.execute("INSERT INTO students_tbl VALUES (?, ?, ?, ?)", (eid, name, email, phone))
    con.commit()
    con.close()
    print("Student added")

def update_student():
    eid = input("Enter EnrollID to update: ")
    name = input("New Name: ")
    email = input("New Email: ")
    phone = input("New Phone: ")
    con = sqlite3.connect("enrollment.db")
    cur = con.cursor()
    cur.execute("UPDATE students_tbl SET StudentName=?, StudentEmail=?, StudentPhone=? WHERE EnrollID=?", 
                (name, email, phone, eid))
    con.commit()
    con.close()
    print("Student updated")

def delete_student():
    eid = input("Enter EnrollID to delete: ")
    con = sqlite3.connect("enrollment.db")
    cur = con.cursor()
    cur.execute("DELETE FROM students_tbl WHERE EnrollID=?", (eid,))
    con.commit()
    con.close()
    print("Student deleted")

def menu():
    while True:
        print("\n1. View Students")
        print("2. View Courses")
        print("3. View Departments")
        print("4. View Instructors")
        print("5. View Enrollments")
        print("6. Add Student")
        print("7. Update Student")
        print("8. Delete Student")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            view_table("students_tbl")
        elif choice == "2":
            view_table("courses_tbl")
        elif choice == "3":
            view_table("departments_tbl")
        elif choice == "4":
            view_table("instructors_tbl")
        elif choice == "5":
            view_table("enrollment_tbl")
        elif choice == "6":
            add_student()
        elif choice == "7":
            update_student()
        elif choice == "8":
            delete_student()
        elif choice == "9":
            break
        else:
            print("Invalid choice")

create_db()
menu()
