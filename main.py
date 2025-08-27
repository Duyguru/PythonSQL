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
                       email VARCHAR UNIQUE,
                       credits  INTEGER
                       
                   )
                   ''')

    conn = sqlite3.connect("students.db")






def main():
    conn, cursor = create_database()

    try:
        create_table(cursor)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

    finally:              #hep çalışır
        conn.close()

if __name__ == "__main__":
    main()