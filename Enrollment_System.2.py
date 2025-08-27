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

    cur.execute("SELECT COUNT(*) FROM students_tbl")
    if cur.fetchone()[0] == 0:
        cur.executemany("INSERT INTO students_tbl VALUES (?, ?, ?, ?)", [
            ("E001", "Mark Reyes", "mark@email.com", "9171234567"),
            ("E002", "Liza Cruz", "liza@email.com", "9981231234"),
            ("E003", "John Dela", "john@email.com", "9227654321")
        ])

        cur.executemany("INSERT INTO courses_tbl VALUES (?, ?)", [
            ("CS101", "Database Systems"),
            ("CS102", "Web Development"),
            ("CS103", "Data Structures")
        ])

        cur.executemany("INSERT INTO departments_tbl VALUES (?, ?)", [
            ("Computer Science", "Ana Rivera")
        ])

        cur.executemany("INSERT INTO instructors_tbl VALUES (?, ?, ?)", [
            ("I001", "Carlo Santos", "carlo@school.edu"),
            ("I002", "Maria Lopez", "maria@school.edu")
        ])

        cur.executemany("INSERT INTO enrollment_tbl VALUES (?, ?, ?)", [
            ("E001", "CS101", "I001"),
            ("E002", "CS102", "I002"),
            ("E003", "CS103", "I001")
        ])

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

def view_all():
    con = sqlite3.connect("enrollment.db")
    cur = con.cursor()
    cur.execute("""
        SELECT s.EnrollID, s.StudentName, s.StudentEmail, s.StudentPhone,
               c.CourseName, c.CourseCode,
               d.DepartmentName, d.DepartmentHead,
               i.InstructorName, i.InstructorEmail
        FROM enrollment_tbl e
        JOIN students_tbl s ON e.EnrollID = s.EnrollID
        JOIN courses_tbl c ON e.CourseCode = c.CourseCode
        JOIN departments_tbl d ON d.DepartmentName = 'Computer Science'
        JOIN instructors_tbl i ON e.InstructorID = i.InstructorID
    """)
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
        print("6. View All Records")
        print("7. Add Student")
        print("8. Update Student")
        print("9. Delete Student")
        print("10. Exit")

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
            view_all()
        elif choice == "7":
            add_student()
        elif choice == "8":
            update_student()
        elif choice == "9":
            delete_student()
        elif choice == "10":
            break
        else:
            print("Invalid choice")

create_db()
menu()
