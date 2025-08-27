import sqlite3

def create_db():
    con = sqlite3.connect("enrollment.db")
    cur = con.cursor()


    cur.execute("DROP TABLE IF EXISTS enrollment_tbl")

    cur.execute("""
        CREATE TABLE enrollment_tbl (
            EnrollID TEXT PRIMARY KEY,
            StudentName TEXT,
            StudentEmail TEXT,
            StudentPhone TEXT,
            CourseName TEXT,
            CourseCode TEXT,
            DepartmentName TEXT,
            DepartmentHead TEXT,
            InstructorName TEXT,
            InstructorEmail TEXT
        )
    """)

    cur.executemany("INSERT INTO enrollment_tbl VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", [
        ("E001", "Mark Reyes", "mark@email.com", "9171234567",
         "Database Systems", "CS101", "Computer Science", "Ana Rivera",
         "Carlo Santos", "carlo@school.edu"),

        ("E002", "Liza Cruz", "liza@email.com", "9981231234",
         "Web Development", "CS102", "Computer Science", "Ana Rivera",
         "Maria Lopez", "maria@school.edu"),

        ("E003", "John Dela", "john@email.com", "9227654321",
         "Data Structures", "CS103", "Computer Science", "Ana Rivera",
         "Carlo Santos", "carlo@school.edu")
    ])

    con.commit()
    con.close()


def add_record():
    con = sqlite3.connect("enrollment.db")
    cur = con.cursor()

    eid = input("Enter Enroll ID: ")
    sname = input("Enter Student Name: ")
    semail = input("Enter Student Email: ")
    sphone = input("Enter Student Phone: ")
    cname = input("Enter Course Name: ")
    ccode = input("Enter Course Code: ")
    dname = input("Enter Department Name: ")
    dhead = input("Enter Department Head: ")
    iname = input("Enter Instructor Name: ")
    iemail = input("Enter Instructor Email: ")

    cur.execute("INSERT INTO enrollment_tbl VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (eid, sname, semail, sphone, cname, ccode, dname, dhead, iname, iemail))

    con.commit()
    con.close()
    print("Record added successfully!")


def view_records():
    con = sqlite3.connect("enrollment.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM enrollment_tbl")
    rows = cur.fetchall()

    print("\n--- Enrollment Records ---")
    for row in rows:
        print(row)

    con.close()


def update_record():
    con = sqlite3.connect("enrollment.db")
    cur = con.cursor()

    eid = input("Enter Enroll ID to update: ")
    new_course = input("Enter new Course Name: ")

    cur.execute("UPDATE enrollment_tbl SET CourseName=? WHERE EnrollID=?", (new_course, eid))

    con.commit()
    con.close()
    print("Record updated successfully!")


def delete_record():
    con = sqlite3.connect("enrollment.db")
    cur = con.cursor()

    eid = input("Enter Enroll ID to delete: ")

    cur.execute("DELETE FROM enrollment_tbl WHERE EnrollID=?", (eid,))

    con.commit()
    con.close()
    print("Record deleted successfully!")


def menu():
    create_db()
    while True:
        print("\n--- Enrollment System ---")
        print("1. Add Record")
        print("2. View Records")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_record()
        elif choice == "2":
            view_records()
        elif choice == "3":
            update_record()
        elif choice == "4":
            delete_record()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")


menu()
