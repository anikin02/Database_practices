from methods import executeQuery, executeQueryCommit, printTable

# Задача 11. База данных по учету успеваемости студентов.
#База данных должна содержать данные:
# о контингенте студентов — фамилия, имя, отчество, год поступления,
# форма обучения (дневная/вечерняя/заочная), номер или
# название группы;
# об учебном плане — название специальности, дисциплина, семестр,
# количество отводимых на дисциплину часов, форма отчетности (экзамен/зачет);
# о журнале успеваемости студентов — год/семестр, студент, дисциплина, оценка.

# Созадем таблицу студентов
query = """
    CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name VARCHAR(100),
    admission_year INTEGER,
    study_form VARCHAR(50),
    group_name VARCHAR(50)
    );
    """
#executeQueryCommit(query)

# Созадем таблицу учебных планов
query = """
    CREATE TABLE plans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    specialty VARCHAR(255),
    discipline VARCHAR(255),
    semester INTEGER,
    hours INTEGER,
    assessment_form VARCHAR(255)
    );
    """
#executeQueryCommit(query)

# Созадем таблицу успеваемости
query = """
    CREATE TABLE marks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    year INTEGER,
    semester INTEGER,
    student_id INTEGER,
    discipline_id INTEGER,
    mark INTEGER,
    FOREIGN KEY (student_id) REFERENCES students (id),
    FOREIGN KEY (discipline_id) REFERENCES plans (id)
    );
    """
#executeQueryCommit(query)

# Заполняем таблицы данными:
query = """
    INSERT INTO students (full_name, admission_year, study_form, group_name)
    VALUES
    ('Ivanov Ivan Ivanovich', 2021, 'full-time', 'Group 1'),
    ('Orlov Ivan Ivanovich', 2021, 'full-time', 'Group 1'),
    ('Romanenko Roman Ivanovich', 2021, 'part-time', 'Group 2'),
    ('Petrov Petr Petrovich', 2021, 'part-time', 'Group 2'),
    ('Sokolov Petr Petrovich', 2021, 'part-time', 'Group 3'),
    ('Orlov Oleg Petrovich', 2021, 'part-time', 'Group 3'),
    ('Sidorov Sidr Sidorovich', 2022, 'evening', 'Group 3');
    """
#executeQueryCommit(query)

query = """
    INSERT INTO plans (specialty, discipline, semester, hours, assessment_form)
    VALUES
    ('Software Engineering', 'Java', 2, 90, 'exam'),
    ('Software Engineering', 'Data base', 2, 120, 'credit'),
    ('Software Engineering', 'English', 2, 120, 'credit'),
    ('Math', 'Algebra', 1, 60, 'exam'),
    ('Math', 'Math analis', 2, 80, 'exam'),
    ('Math', 'English', 1, 60, 'credit'),
    ('Software Engineering', 'Java', 1, 90, 'exam');
    """
#executeQueryCommit(query)

query = """
    INSERT INTO marks (year, semester, student_id, discipline_id, mark)
    VALUES
    (2022, 2, 1, 1, 5),
    (2022, 2, 1, 2, 5),
    (2022, 2, 1, 3, 5),
    (2022, 2, 2, 4, 4),
    (2022, 2, 2, 5, 4),
    (2022, 2, 2, 6, 4),
    (2022, 1, 3, 1, 3),
    (2022, 2, 3, 2, 2),
    (2022, 1, 3, 3, 2),
    (2022, 2, 4, 1, 5),
    (2022, 2, 4, 2, 5),
    (2022, 2, 4, 3, 5),
    (2022, 2, 5, 4, 4),
    (2022, 2, 5, 5, 4),
    (2022, 2, 5, 6, 4),
    (2022, 1, 6, 1, 3),
    (2022, 2, 6, 2, 2),
    (2022, 1, 6, 3, 2),
    (2022, 1, 7, 1, 5),
    (2022, 2, 7, 2, 3),
    (2022, 1, 7, 3, 4);
    """
#executeQueryCommit(query)

# Функции для просмотра таблиц
def showStudents():
    printTable(executeQuery("SELECT * FROM students"))
    
def showPlans():
    printTable(executeQuery("SELECT * FROM plans"))
    
def showMarks():
    printTable(executeQuery("SELECT * FROM marks ORDER BY MARK DESC"))

# Функции удаления
def deleteStudents():
    executeQueryCommit("DROP TABLE IF EXISTS students;")
def deleteMarks():
    executeQueryCommit("DROP TABLE IF EXISTS marks;")
def deletePlans():
    executeQueryCommit("DROP TABLE IF EXISTS plans;")

def averageMark():
    query = """
    SELECT students.full_name, AVG(marks.mark) AS average_mark
    FROM students
    JOIN marks ON students.id = marks.student_id
    GROUP BY students.full_name;
    """
    printTable(executeQuery(query))

def badMark():
    query = """
    SELECT students.full_name, plans.discipline, marks.mark
    FROM students
    JOIN marks ON students.id = marks.student_id
    JOIN plans ON marks.discipline_id = plans.id
    WHERE marks.mark < 3;
    """
    printTable(executeQuery(query))
    
def howStudentsInForm():
    query = """
    SELECT study_form, COUNT(*) AS student_count
    FROM students
    GROUP BY study_form;
    """
    printTable(executeQuery(query))

def howHours():
    printTable(executeQuery("""
    SELECT discipline, SUM(hours) AS total_hours
    FROM plans GROUP BY discipline;"""))
    
def assessmentForm():
    printTable(executeQuery("""
    SELECT assessment_form, COUNT(*) AS count
    FROM plans
    GROUP BY assessment_form;"""))

def admissionYear():
    printTable(executeQuery("""
    SELECT admission_year, COUNT(*) AS student_count
    FROM students
    GROUP BY admission_year;"""))
    
def excellentStudents():
    query = """
    SELECT students.full_name, AVG(marks.mark) AS average_mark
    FROM students
    JOIN marks ON students.id = marks.student_id
    GROUP BY students.full_name
    HAVING AVG(marks.mark) > 4;
    """
    printTable(executeQuery(query))

showMarks()
showPlans()
showStudents()

averageMark()
badMark()
howHours()
howStudentsInForm()
excellentStudents()
admissionYear()
assessmentForm()
