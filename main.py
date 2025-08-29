import sqlite3
import os
def create_database():
 if os.path.exists("students.db"):
     os.remove("students.db")

 conn = sqlite3.connect("students.db") # db ile bağlantı
 cursor = conn.cursor() #imleç , sql komutlarını çalıştırmayı sağlar
 return conn, cursor


def create_table(cursor):
    cursor.execute(''' 
     CREATE TABLE Students (
         id INTEGER PRIMARY KEY,
         name VARCHAR NOT NULL,
         age INTEGER,
         email VARCHAR UNIQUE,
         city VARCHAR )    
      ''')

    cursor.execute('''
                   CREATE TABLE Courses 
                   (
                       id    INTEGER PRIMARY KEY,
                       course_name  VARCHAR NOT NULL,
                       instructor TEXT,
                       credits  INTEGER
                       
                   )
                   ''')

    conn = sqlite3.connect("students.db")

def insert_sample_data(cursor):
    students = [
        (1, 'Alice Johnson', 20, 'alice@gmail.com', 'New York'),
        (2, 'Bob Smith', 19, 'bob@gmail.com', 'Chicago'),
        (3, 'Carol White', 21, 'carol@gmail.com', 'Boston'),
        (4, 'David Brown', 20, 'david@gmail.com', 'New York'),
        (5, 'Emma Davis', 22, 'emma@gmail.com', 'Seattle')
    ]
    cursor.executemany('INSERT INTO Students VALUES (?, ?, ?, ?,?)', students)
    # column kadar ? yazılır
    # birden fazla olduğu için executemany

    courses = [
        (1, 'Python Programming', 'Dr. Anderson', 3),
        (2, 'Web Development', 'Prof. Wilson', 4),
        (3, 'Data Science', 'Dr. Taylor', 3),
        (4, 'Mobile Apps', 'Prof. Garcia', 2)
    ]
    cursor.executemany('INSERT INTO Courses VALUES (?, ?,?,?)', courses)
    print("Sample data inserted successfully")


def basic_sql_operations(cursor):
    # 1-select all
    cursor.execute("SELECT * FROM Students")
    records = cursor.fetchall() # dataları aldırır
    for row in records:
        print(row)

    # 2-select columns
    cursor.execute("SELECT name,age FROM Students")
    records = cursor.fetchall()
    print("\n")
    print(records)

    # where clause
    print("\n")
    cursor.execute("SELECT * FROM Students WHERE age=21")
    records = cursor.fetchall()
    for row in records:
        print(row)


def main():
    conn, cursor = create_database()

    try:
        create_table(cursor)
        insert_sample_data(cursor)
        basic_sql_operations(cursor)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

    finally:              #hep çalışır
        conn.close()

if __name__ == "__main__":
    main()