import sqlite3

def createTables():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    
        # Создание таблицы SUBJECT
    query = """CREATE TABLE SUBJECT (
                subject_id INT,
                subject_name VARCHAR(50),
                semester INT,
                hours INT,
                PRIMARY KEY (subject_id));"""
    cursor.execute(query)

    # Создание таблицы EXAM_MARKS
    query = """CREATE TABLE EXAM_MARKS (
                exam_id INT,
                student_id INT,
                subj_id INT,
                mark INT,
                exam_date DATE,
                PRIMARY KEY (exam_id),
                FOREIGN KEY (subj_id) REFERENCES SUBJECT(subject_id));"""
    cursor.execute(query)
    
    # Создание таблицы UNIVERSITY
    query = """CREATE TABLE UNIVERSITY (
                univ_id INT,
                univ_name VARCHAR(50),
                rating INT,
                city VARCHAR(50),
                PRIMARY KEY (univ_id));"""
    cursor.execute(query)
    
    # Cоздание таблицы STUDENT
    query = """CREATE TABLE STUDENT (
        STUDENT_ID INT,
        SURNAME VARCHAR(50),
        NAME VARCHAR(50),
        STIPEND DECIMAL(10, 2),
        KURS INT,
        CITY VARCHAR(50),
        BIRTHDAY DATE,
        UNIV_ID INT,
        PRIMARY KEY (STUDENT_ID),
        FOREIGN KEY (UNIV_ID) REFERENCES UNIVERSITY (UNIV_ID));"""
    cursor.execute(query)

    # Вставка данных в таблицу SUBJECT
    query = """INSERT INTO SUBJECT (subject_id, subject_name, semester, hours)
               VALUES (1, 'Mathematics', 1, 60);"""
    cursor.execute(query)

    query = """INSERT INTO SUBJECT (subject_id, subject_name, semester, hours)
               VALUES (2, 'Physics', 2, 45);"""
    cursor.execute(query)
    
    query = """INSERT INTO SUBJECT (subject_id, subject_name, semester, hours)
    VALUES (5, 'Programming', 1, 180);"""
    cursor.execute(query)

    query = """INSERT INTO SUBJECT (subject_id, subject_name, semester, hours)
               VALUES (18, 'Chemistry', 1, 50);"""
    cursor.execute(query)

    # Вставка данных в таблицу EXAM_MARKS
    query = """INSERT INTO EXAM_MARKS (exam_id, student_id, subj_id, mark, exam_date)
               VALUES
               (1, 101, 1, 3, '2005-01-12'),
               (2, 102, 18, 4, '2005-01-30'),
               (3, 103, 3, 5, '2005-01-12'),
               (4, 101, 18, 5, '2005-01-20'),
               (5, 102, 1, 4, '2005-01-19'),
               (6, 103, 1, 4, '2005-01-19');"""
    cursor.execute(query)
    
    # Вставка данных в таблицу UNIVERSITY
    query = """ INSERT INTO UNIVERSITY (univ_id, univ_name, rating, city)
                VALUES
                (1, 'FEFU', 250, 'Vladivostok'),
                (2, 'VGEUS', 150, 'Vladivostok'),
                (3, 'MGU', 400, 'Moscow'),
                (4, 'NGU', 345, 'Novocibirsk'),
                (5, 'TGU', 373, 'Tomsk');"""
    cursor.execute(query)
    
    query = """INSERT INTO STUDENT (STUDENT_ID, SURNAME, NAME, STIPEND, KURS, CITY, BIRTHDAY, UNIV_ID)
                VALUES
        (101, 'Ivanov', 'Ivan', 1500.00, 2, 'Moscow', '1995-05-15', 2),
        (102, 'Petrov', 'Petr', 1200.50, 3, 'Vladivostok', '1996-08-22', 2),
        (103, 'Sidorov', 'Alex', 1800.75, 4, 'Vladivostok', '1994-12-10', 3);"""
    
    connection.commit()  # Применение изменений
    connection.close()
    
#createTables()
