import mysql.connector
import tkinter as tk
from tkinter import messagebox
# Function to establish connection to MySQL server
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mithran2!",
            database="STUDENT"
        )
        messagebox.showinfo("Success", "Connected to the database successfully!")
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error connecting to the database: {err}")
        return None

# Function to create Student table
def create_student_table(conn):
    try:
        cursor = conn.cursor()
        create_student_query = """
        CREATE TABLE IF NOT EXISTS Student (
            Std_id INT PRIMARY KEY,
            Stfname VARCHAR(25),
            Stlname VARCHAR(25),
            Stcontact VARCHAR(10),
            Styear INT,
            Stbirthdate DATE,
            Stgender CHAR(1),
            Stage VARCHAR(25)
        )
        """
        cursor.execute(create_student_query)
        conn.commit()
        cursor.close()
        messagebox.showinfo("Success", "Student table created successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error creating Student table: {err}")
# Function to create Course Offered table
def create_course_offered_table(conn):
    try:
        cursor = conn.cursor()
        create_course_query = """
        CREATE TABLE IF NOT EXISTS Course_Offered (
            Course_id INT PRIMARY KEY,
            C_name VARCHAR(25),
            units INT
        )
        """
        cursor.execute(create_course_query)
        conn.commit()
        cursor.close()
        messagebox.showinfo("Success", "Course Offered table created successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error creating Course Offered table: {err}")

# Function to create Staff Department table
def create_staff_department_table(conn):
    try:
        cursor = conn.cursor()
        create_department_query = """
        CREATE TABLE IF NOT EXISTS Staff_Department (
            Dept_id INT PRIMARY KEY,
            D_name VARCHAR(25)
        )
        """
        cursor.execute(create_department_query)
        conn.commit()
        cursor.close()
        messagebox.showinfo("Success", "Staff Department table created successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error creating Staff Department table: {err}")

# Function to create Staff table
def create_staff_table(conn):
    try:
        cursor = conn.cursor()
        create_staff_query = """
        CREATE TABLE IF NOT EXISTS Staff (
            Dept_id INT,
            Staff_id INT PRIMARY KEY,
            Contact VARCHAR(10),
            Fname VARCHAR(25),
            Lname VARCHAR(25),
            Address VARCHAR(300),
            Gender CHAR(1),
            FOREIGN KEY (Dept_id) REFERENCES Staff_Department(Dept_id)
        )
        """
        cursor.execute(create_staff_query)
        conn.commit()
        cursor.close()
        messagebox.showinfo("Success", "Staff table created successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error creating Staff table: {err}")

# Function to create Student Registration table
def create_student_registration_table(conn):
    try:
        cursor = conn.cursor()
        create_registration_query = """
        CREATE TABLE IF NOT EXISTS Student_Registration_map (
            Registration_id INT  KEY,
            rname VARCHAR(25),
            Course_id INT,
            Date DATE,
            Std_id  INT,
            Staff_id INT,
            FOREIGN KEY (Course_id) REFERENCES Course_Offered(Course_id),
            FOREIGN KEY (Std_id ) REFERENCES Student(Std_id ),
            FOREIGN KEY (Staff_id) REFERENCES Staff(Staff_id)
        )
        """
        cursor.execute(create_registration_query)
        conn.commit()
        cursor.close()
        messagebox.showinfo("Success", "Student Registration table created successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error creating Student Registration table: {err}")
# Function to create all tables
def create_all_tables():
    conn = connect_to_database()
    if conn:
        create_student_table(conn)
        create_course_offered_table(conn)
        create_staff_department_table(conn)
        create_staff_table(conn)
        create_student_registration_table(conn)
        conn.close()

# Function to insert data into tables
def insert_data():
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            # Insert data into tables here
            insert_student_data = """
            INSERT INTO Student (Std_id, Stfname, Stlname, Stcontact, Styear, Stbirthdate, Stgender, Stage)
            VALUES 
            (1, 'John', 'Doe', '1234567890', 2024, '2000-01-01', 'M', 'Freshman'),
            (2, 'Alice', 'Smith', '9876543210', 2023, '2001-05-15', 'F', 'Sophomore'),
            (3, 'Bob', 'Johnson', '5555555555', 2022, '1999-09-30', 'M', 'Junior'),
            (4, 'Emily', 'Brown', '7777777777', 2021, '1998-03-20', 'F', 'Senior'),
            (5, 'David', 'Lee', '9999999999', 2020, '1997-11-10', 'M', 'Senior')
            """
            cursor.execute(insert_student_data)

            insert_course_data = """
            INSERT INTO Course_Offered (Course_id, C_name, units)
            VALUES 
            (1, 'Mathematics', 3),
            (2, 'Physics', 4),
            (3, 'Biology', 3),
            (4, 'Chemistry', 4),
            (5, 'English', 3)
            """
            cursor.execute(insert_course_data)

            insert_staff_department_data = """
            INSERT INTO Staff_Department (Dept_id, D_name)
            VALUES 
            (1, 'Math'),
            (2, 'Science'),
            (3, 'Literature'),
            (4, 'Computer Science'),
            (5, 'History')
            """
            cursor.execute(insert_staff_department_data)

            insert_staff_data = """
            INSERT INTO Staff (Dept_id, Staff_id, Contact, Fname, Lname, Address, Gender)
            VALUES 
            (1, 101, '1234567890', 'Jane', 'Dane', '123 Main St', 'F'),
            (2, 102, '9876543210', 'John', 'Don', '456 Elm St', 'M'),
            (3, 103, '5555555555', 'Alice', 'John', '789 Oak St', 'F'),
            (4, 104, '7777777777', 'Bob', 'Black', '101 Maple St', 'M'),
            (5, 105, '9999999999', 'Emily', 'Ray', '202 Pine St', 'F')
            """
            cursor.execute(insert_staff_data)

            insert_student_registration_data = """
            INSERT INTO Student_Registration_map (Registration_id ,rname, Course_id, Date, Std_id, Staff_id)
            VALUES 
            (1,'John Doe', 1, '2024-04-15', 1, 101),
            (2,'Alice Smith', 2, '2023-10-20', 2, 102),
            (3,'Bob Johnson', 3, '2022-08-05', 3, 103),
            (4,'Emily Brown', 4, '2021-06-30', 4, 104),
            (5,'David Lee', 5, '2020-12-25', 5, 105)
            """
            cursor.execute(insert_student_registration_data)
            conn.commit()
            cursor.close()
            messagebox.showinfo("Success", "Data inserted successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error inserting data: {err}")
        conn.close()

# Function for commands
def db_commands() :
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            # Run DB Commands
            # 1. Select and display all student details
            select_students = """
            SELECT * 
            FROM Student;
            """
            cursor.execute(select_students)
            students_names = cursor.fetchall()
            print("\n1. Select and display all student details:")
            for row in students_names:
                print(row)


            # Performing commands with joins
            # 2. Select students and their corresponding staff members' names
            select_students_staff_names = """
            SELECT DISTINCT s.Std_id, s.Stfname, s.Stlname, st.Fname AS Staff_FirstName, st.Lname AS Staff_LastName
            FROM Student s
            INNER JOIN Student_Registration_map sr ON s.Std_id = sr.Std_id
            INNER JOIN Staff st ON sr.Staff_id = st.Staff_id;
            """
            cursor.execute(select_students_staff_names)
            students_staff_names = cursor.fetchall()
            print("\n2. Select students and their corresponding staff members' names:")
            for row in students_staff_names:
                print(row)

            # 3. Select all students along with the courses they are registered for
            select_students_courses = """
            SELECT DISTINCT s.Stfname, s.Stlname, co.C_name AS Course_Name
            FROM Student s
            INNER JOIN Student_Registration_map sr ON s.Std_id = sr.Std_id
            INNER JOIN Course_Offered co ON sr.Course_id = co.Course_id;
            """
            cursor.execute(select_students_courses)
            students_courses = cursor.fetchall()
            print("\n3. Select all students along with the courses they are registered for:")
            for row in students_courses:
                print(row)

            # 4. Select staff members and their corresponding departments
            select_staff_departments = """
            SELECT DISTINCT st.Fname AS Staff_FirstName, st.Lname AS Staff_LastName, sd.D_name AS Department
            FROM Staff st
            INNER JOIN Staff_Department sd ON st.Dept_id = sd.Dept_id;
            """
            cursor.execute(select_staff_departments)
            staff_departments = cursor.fetchall()
            print("\n4.Selected staff members and their corresponding departments:")
            for row in staff_departments:
                print(row)

            # 5. Select students and their registration details
            select_student_reg_details = """
            SELECT DISTINCT s.Stfname AS Student_FirstName, s.Stlname AS Student_LastName, sr.rname AS Registration_Name, sr.Date AS Registration_Date
            FROM Student s
            INNER JOIN Student_Registration_map sr ON s.Std_id = sr.Std_id;
            """
            cursor.execute(select_student_reg_details)
            student_reg_details = cursor.fetchall()
            print("\n5.Selected students and their registration details:")
            for row in student_reg_details:
                print(row)

            # 6. Select staff members who are teaching a specific course
            select_staff_course = """
            SELECT st.Fname AS Staff_FirstName, st.Lname AS Staff_LastName, co.C_name AS Course_Name
            FROM Staff st
            INNER JOIN Student_Registration_map sr ON st.Staff_id = sr.Staff_id
            INNER JOIN Course_Offered co ON sr.Course_id = co.Course_id
            GROUP BY st.Fname, st.Lname, co.C_name;
            """
            cursor.execute(select_staff_course)
            staff_course = cursor.fetchall()
            print("\n6. Selected staff members teaching a specific course:")
            for row in staff_course:
                print(row)
            # 7. Select students and their corresponding staff members' names for a specific course
            select_students_staff_course = """
            SELECT DISTINCT s.Stfname, s.Stlname, st.Fname AS Staff_FirstName, st.Lname AS Staff_LastName, co.C_name AS Course_Name
            FROM Student s
            INNER JOIN Student_Registration_map sr ON s.Std_id = sr.Std_id
            INNER JOIN Staff st ON sr.Staff_id = st.Staff_id
            INNER JOIN Course_Offered co ON sr.Course_id = co.Course_id
            WHERE co.C_name = 'Biology';
            """
            cursor.execute(select_students_staff_course)
            students_staff_course = cursor.fetchall()
            print("\n7. Selected students and their corresponding staff members' names for Biology:")
            for row in students_staff_course:
                print(row)
            # 8. Select students who are taught by female staff members
            select_students_female_staff = """
            SELECT s.Stfname, s.Stlname, st.Fname AS Staff_FirstName, st.Lname AS Staff_LastName
            FROM Student s
            INNER JOIN Student_Registration_map sr ON s.Std_id = sr.Std_id
            INNER JOIN Staff st ON sr.Staff_id = st.Staff_id
            WHERE st.Gender = 'F';
            """
            cursor.execute(select_students_female_staff)
            students_female_staff = cursor.fetchall()
            print("\n8.Selected students who are taught by female staff members:")
            for row in students_female_staff:
                print(row)
            #9.Register Alice smith to course 3
            print("\n9.Register Alice smith to course 3:")
            insert_student_registration_data_additional="""
            INSERT INTO  Student_Registration_map (Registration_id,rname, Course_id, Date, Std_id, Staff_id)
            VALUES 
            (8,'Alice Smith', 3, '2024-04-20', 2, 102);"""
            cursor.execute(insert_student_registration_data_additional)
            print("\nInserted additional student registration record.")
            # 10. Select students who are registered for more than one course
            select_students_multiple_courses = """
            SELECT s.Stfname, s.Stlname, COUNT(sr.Course_id) AS Num_Courses
            FROM Student s
            INNER JOIN Student_Registration_map sr ON s.Std_id = sr.Std_id
            GROUP BY s.Std_id
            HAVING COUNT(sr.Course_id) > 1;
            """
            cursor.execute(select_students_multiple_courses)
            students_multiple_courses = cursor.fetchall()
            print("\n10.Selected students registered for more than one course:")
            for row in students_multiple_courses:
                print(row)
            # 11. change no of units for physics to 5
            print("\n11. change no of units for physics to 5:")
            update_course_units = """
            UPDATE Course_Offered
            SET units = 5
            WHERE C_name = 'Physics';
            """
            cursor.execute(update_course_units)
            print("\nUpdated course units for 'Physics'.")
            # 12 Select staff members who are teaching courses with more than 5 units
            select_staff_courses_units = """
            SELECT st.Fname AS Staff_FirstName, st.Lname AS Staff_LastName, co.C_name AS Course_Name, co.units
            FROM Staff st
            INNER JOIN Student_Registration_map sr ON st.Staff_id = sr.Staff_id
            INNER JOIN Course_Offered co ON sr.Course_id = co.Course_id
            WHERE co.units >=5;
            """
            cursor.execute(select_staff_courses_units)
            staff_courses_units = cursor.fetchall()
            print("\n12.Selected staff members teaching courses with more than 5 units:")
            for row in staff_courses_units:
                print(row)
            #13.delete record of john doe from student registration table
            print("\n13.delete record of john doe from student registration table:")
            delete_student_registration_data = """
            DELETE FROM Student_Registration_map
            WHERE rname = 'John Doe';"""
            cursor.execute(delete_student_registration_data)
            print("\nDeleted student registration record for 'John Doe'.")
            conn.commit()
            cursor.close()
            messagebox.showinfo("Success", "Data displayed successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error displaying data: {err}")
        conn.close()

# Function to close the application
def close_app():
    root.destroy()

# Create main application window
root = tk.Tk()
root.title("Database Management System")

# Create buttons for operations
create_tables_button = tk.Button(root, text="Create Tables", command=create_all_tables)
create_tables_button.pack()

insert_data_button = tk.Button(root, text="Insert Data", command=insert_data)
insert_data_button.pack()

db_commands_button = tk.Button(root, text="Run Commands", command=db_commands)
db_commands_button.pack()

exit_button = tk.Button(root, text="Exit", command=close_app)
exit_button.pack()

root.mainloop()