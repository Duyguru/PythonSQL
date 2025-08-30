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

def sql_update_delete_insert_operations(conn, cursor):
    #1) Insert
    cursor.execute("INSERT INTO Students VALUES (6, 'Frank Miller', 23, 'frank@gmail.com','Miami')")
    conn.commit()

    #2) UPDATE
    cursor.execute("UPDATE Students SET age = 24 WHERE id = 6")
    conn.commit()

    #3) DELETE
    cursor.execute("DELETE FROM Students WHERE id = 6")
    conn.commit()

def aggregate_functions(cursor):
    #1) Count
    print("----------Aggregate Functions Count----------")
    cursor.execute("SELECT COUNT(*) FROM Students")
    result = cursor.fetchone() # tek sonuç veren işlemlerde tercih edilir
    print(result[0])

    # 2) Average
    print("----------Aggregate Functions Average----------")
    cursor.execute("SELECT AVG(age) FROM Students")
    result = cursor.fetchone()
    print(result[0])

    # 3) MAX - MIN
    print("----------Aggregate Functions Max-Min----------")
    cursor.execute("SELECT MAX(age), MIN(age) FROM Students")
    result = cursor.fetchone()
    max_age, min_age = result
    print(max_age)
    print(min_age)

    # 4) GROUP BY
    print("----------Aggregate Functions Group by----------")
    cursor.execute("SELECT city, COUNT(*) FROM Students GROUP BY city")
    result = cursor.fetchall()
    print(result)

def questions():
    '''
    1) Bütün kursların bilgilerini getirin
    2) Sadece eğitmenlerin ismini ve ders ismi bilgilerini getirin
    3) Sadece 21 yaşındaki öğrencileri getirin
    4) Sadece Chicago'da yaşayan öğrencileri getirin
    5) Sadece 'Dr. Anderson' tarafından verilen dersleri getirin
    6) Sadece ismi 'A' ile başlayan öğrencileri getirin
    7) Sadece 3 ve üzeri kredi olan dersleri getirin
    8) Öğrencileri alphabetic şekilde dizerek getirin
    9) 20 yaşından büyük öğrencileri, ismine göre sıralayarak getirin
    10) Sadece 'New York' veya 'Chicago' da yaşayan öğrencileri getirin
    11) Sadece 'New York' ta yaşamayan öğrencileri getirin
    '''
    pass

def answer(cursor):
    print("\n")
    print("----------Answers----------")
    print("1) Bütün kursların bilgilerini getirin")
    cursor.execute("SELECT * FROM Courses")
    result = cursor.fetchall()
    print(result)

    print("2) Sadece eğitmenlerin ismini ve ders ismi bilgilerini getirin")
    cursor.execute("SELECT instructor, course_name FROM Courses")
    result = cursor.fetchall()
    for row in result:
        print(row)

    print("3) Sadece 21 yaşındaki öğrencileri getirin")
    cursor.execute("SELECT * FROM Students WHERE age = 21")
    result = cursor.fetchall()
    for row in result:
        print(row)

    print("4) Sadece Chicago'da yaşayan öğrencileri getirin")
    cursor.execute("SELECT * FROM Students WHERE city = 'Chicago'")
    result = cursor.fetchall()
    for row in result:
        print(row)

    print("5) Sadece 'Dr. Anderson' tarafından verilen dersleri getirin")
    cursor.execute("SELECT * FROM Courses WHERE instructor = 'Dr. Anderson'")
    result = cursor.fetchall()
    for row in result:
        print(row)

    print("6) Sadece ismi 'A' ile başlayan öğrencileri getirin")
    cursor.execute("SELECT * FROM Students WHERE name LIKE  'A%'")
    print(cursor.fetchall())

    print(" 7) Sadece 3 ve üzeri kredi olan dersleri getirin")
    cursor.execute("SELECT * FROM Courses WHERE credits >=3")
    print(cursor.fetchall())

    print("8) Öğrencileri alphabetic şekilde dizerek getirin")
    cursor.execute("SELECT * FROM Students ORDER BY name")
    print(cursor.fetchall())

    print("9) 20 yaşından büyük öğrencileri, ismine göre sıralayarak getirin")
    cursor.execute("SELECT name age FROM Students WHERE age>20 ORDER BY name ASC")
    print(cursor.fetchall())

    print("10) Sadece 'New York' veya 'Chicago' da yaşayan öğrencileri getirin")
    cursor.execute("SELECT name,city FROM Students WHERE city = 'Chicago' or city = 'New York'")
                   #SELECT name, city FROM Students WHERE city IN ('New York', 'Chicago')
    print(cursor.fetchall())

    print("11) Sadece 'New York' ta yaşamayan öğrencileri getirin")
    cursor.execute("SELECT name,city FROM Students WHERE city != 'New York'")
    print(cursor.fetchall())


def main():
    conn, cursor = create_database()

    try:
        create_table(cursor)
        insert_sample_data(cursor)
        basic_sql_operations(cursor)
        sql_update_delete_insert_operations(conn, cursor)
        aggregate_functions(cursor)
        answer(cursor)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

    finally:              #hep çalışır
        conn.close()

if __name__ == "__main__":
    main()