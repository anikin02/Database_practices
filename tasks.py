from methods import executeQuery, executeQueryCommit, printTable, printTableStudent, printTableSubject, printTableUniversity, printTableExam

#printTableStudent()

# 2.1
# 1
query1 = """
    SELECT *
    FROM SUBJECT;
    """
#printTable(executeQuery(query1))

# 2
query2 = """
    SELECT *
    FROM EXAM_MARKS
    WHERE subj_id = 18;
    """
#printTable(executeQuery(query2))

# 2.2
# 1
query3 = """
    SELECT *
    FROM EXAM_MARKS
    WHERE exam_date
    BETWEEN DATE('2005-01-10') AND DATE('2005-01-20');
    """
#printTable(executeQuery(query3))

# 3
query4 = """
    SELECT *
    FROM SUBJECT
    WHERE subject_name LIKE 'P%';
    """
#printTable(executeQuery(query4))

# 2.3
# 7
query5 = """
    SELECT 'Cod - ' || univ_id || '; ' || univ_name || ' - c.' || city || '; Rating = ' || rating
    FROM UNIVERSITY;
    """
#printTable(executeQuery(query5))

# 8
query6 = """
    SELECT 'Cod - ' || univ_id || '; ' || univ_name || ' - c.' || city || '; Rating = ' || CAST(ROUND(rating / 100.0) * 100 AS INTEGER)
    FROM UNIVERSITY;
    """
#printTable(executeQuery(query6))

# 2.4
# 2
query7 = """
    SELECT COUNT(DISTINCT subj_id) AS CountSubjects
    FROM EXAM_MARKS;
    """
#printTable(executeQuery(query7))

# 9
query8 = """
    SELECT exam_id, AVG(mark) AS AverageMark
    FROM EXAM_MARKS
    GROUP BY exam_id;
    """
#printTable(executeQuery(query8))

# 2.7
# 2
query9 = """
    SELECT student_id, MAX(mark) AS MaxMark, MIN(mark) AS MinMark
    FROM EXAM_MARKS
    GROUP BY student_id;
    """
#printTable(executeQuery(query9))

# 4
query10 = """
    SELECT exam_date, SUM(mark) AS TotalMarks
    FROM EXAM_MARKS
    GROUP BY exam_date
    ORDER BY TotalMarks DESC;
    """
#printTable(executeQuery(query10))

# 2.8
# 4
query11 = """
    SELECT subject_name, hours
    FROM SUBJECT
    WHERE hours = (SELECT MAX(hours) FROM SUBJECT);
    """
#printTable(executeQuery(query11))

# 6
query12 = """
    SELECT u.univ_name, u.rating
    FROM UNIVERSITY u
    WHERE u.city = 'Vladivostok' AND u.rating < (SELECT rating FROM UNIVERSITY WHERE univ_name = 'TGU');
    """
#printTable(executeQuery(query12))

# 2.9
# 11
query13 = """SELECT * FROM STUDENT S
    WHERE 4<(SELECT AVG(MARK) FROM EXAM_MARKS
    WHERE STUDENT_ID=S.STUDENT_ID);
    """
#printTable(executeQuery(query13))

# 1
query14 = """SELECT S.STUDENT_ID, S.SURNAME, S.NAME, S.CITY, U.UNIV_NAME
    FROM STUDENT S
    JOIN UNIVERSITY U ON S.UNIV_ID = U.UNIV_ID
    WHERE S.CITY = U.CITY;
    """
#printTable(executeQuery(query14))

# 2.10
# 2
query15 = """ SELECT S.NAME, S.SURNAME
    FROM STUDENT S
    JOIN EXAM_MARKS EM ON S.STUDENT_ID = EM.STUDENT_ID
    WHERE EM.SUBJ_ID = 1
    GROUP BY S.NAME
    HAVING AVG(EM.MARK) > (
        SELECT AVG(MARK)
        FROM EXAM_MARKS
        WHERE SUBJ_ID = 1
    );
    """
#printTable(executeQuery(query15))

# 6
query16 = """ SELECT NAME, STUDENT_ID
    FROM STUDENT A
    WHERE A.CITY IS NOT NULL AND A.CITY NOT IN
    (SELECT B.CITY FROM UNIVERSITY B);
    """
#printTable(executeQuery(query16))

# 2.11
# 1
query17 = """SELECT *
    FROM STUDENT S
    WHERE EXISTS (
        SELECT 1
        FROM UNIVERSITY U
        WHERE U.UNIV_ID = S.UNIV_ID AND U.RATING > 300
    );
    """
#printTable(executeQuery(query17))

# 14
query18 = """SELECT *
    FROM STUDENT S
    WHERE NOT EXISTS (
        SELECT 1
        FROM EXAM_MARKS EM
        WHERE EM.STUDENT_ID = S.STUDENT_ID AND EM.MARK < 3
    );
    """
#printTable(executeQuery(query18))

# 2.12
# 8
query19 = """SELECT S.SURNAME
    FROM STUDENT S
    WHERE S.UNIV_ID IN (
        SELECT U.univ_id
        FROM UNIVERSITY U
        WHERE U.city = (
            SELECT MIN(city)
            FROM UNIVERSITY
        )
    );
    """
#printTable(executeQuery(query19))

# 2
query20 = """SELECT STUDENT.NAME, STUDENT.SURNAME
    FROM STUDENT
    JOIN EXAM_MARKS ON STUDENT.STUDENT_ID = EXAM_MARKS.STUDENT_ID
    WHERE EXAM_MARKS.MARK IN (3, 4, 5)
    GROUP BY STUDENT.STUDENT_ID, STUDENT.NAME, STUDENT.SURNAME
    HAVING COUNT(DISTINCT EXAM_MARKS.MARK) = 3;
    """
#printTable(executeQuery(query20))

# 2.14
# 1
query21 = """ SELECT univ_name
    FROM UNIVERSITY
    WHERE rating >= (SELECT rating FROM UNIVERSITY WHERE univ_name = 'TGU');
"""
#printTable(executeQuery(query21))

# 3
query22 = """ SELECT subject_name
    FROM SUBJECT
    WHERE subject_id NOT IN (
    SELECT subj_id
    FROM EXAM_MARKS
    WHERE mark <= (
        SELECT MAX(mark)
        FROM EXAM_MARKS
        WHERE subj_id = 1
    )
    );
    """
#printTable(executeQuery(query22))

# 2.15
# 1
query23 = """SELECT s.surname, sj.subject_name, s.kurs
    FROM STUDENT s
    JOIN EXAM_MARKS em ON s.student_id = em.student_id
    JOIN SUBJECT sj ON em.subj_id = sj.subject_id
    """
#printTable(executeQuery(query23))

# 2
query24 = """SELECT name, surname
    FROM STUDENT
    WHERE student_id IN (
        SELECT student_id
        FROM EXAM_MARKS
        GROUP BY student_id
        HAVING COUNT(DISTINCT mark) = 3
        AND MIN(mark) >= 3
        AND MAX(mark) <= 5
    )
"""
#printTable(executeQuery(query24))

# 2.15.1
# 10
query25 = """SELECT UNIV_NAME, SURNAME, NAME, STIPEND
    FROM STUDENT S, UNIVERSITY U WHERE S.UNIV_ID=U.UNIV_ID
    AND STIPEND=(SELECT MAX(STIPEND) FROM STUDENT WHERE UNIV_ID=U.UNIV_ID);
    """
#printTable(executeQuery(query25))

# 11
query26 = """SELECT ST.SURNAME, ST.NAME, E.SUBJ_ID, E.MARK
    FROM STUDENT ST, EXAM_MARKS E, SUBJECT SB WHERE ST.STUDENT_ID=E.STUDENT_ID
    AND E.SUBJ_ID=SB.SUBJECT_ID;
    """
#printTable(executeQuery(query26))

# 2.15.2
# 2
query27 = """SELECT SURNAME, SUBJ_ID
    FROM STUDENT LEFT OUTER JOIN EXAM_MARKS
    ON STUDENT.STUDENT_ID = EXAM_MARKS.STUDENT_ID;
    """
#printTable(executeQuery(query27))

# 3
query28 = """SELECT SURNAME, SUBJECT_NAME
FROM STUDENT, EXAM_MARKS, SUBJECT WHERE STUDENT.STUDENT_ID =
EXAM_MARKS.STUDENT_ID
AND SUBJECT.SUBJECT_ID=EXAM_MARKS.SUBJ_ID;"""
#printTable(executeQuery(query28))

# 2.15.3
# 3
query29 = """SELECT A.UNIV_NAME, A.CITY
FROM UNIVERSITY A, UNIVERSITY B WHERE A.RATING >= B.RATING
AND B.UNIV_NAME = 'TGU';"""
#printTable(executeQuery(query29))

# 2
query30 = """ SELECT A.UNIV_NAME, B.UNIV_NAME
FROM UNIVERSITY A, UNIVERSITY B
 WHERE A.CITY = B.CITY
AND A.UNIV_NAME < B.UNIV_NAME;"""
#printTable(executeQuery(query30))

# 2.16.2
# 5
query31 = """SELECT CITY, UNIV_NAME, RATING, 'max'
FROM UNIVERSITY U
WHERE RATING=(SELECT MAX(RATING)
FROM UNIVERSITY WHERE CITY=U.CITY)
UNION
SELECT CITY, UNIV_NAME, RATING, 'min' FROM UNIVERSITY U
WHERE RATING=(SELECT MIN(RATING)
FROM UNIVERSITY
WHERE CITY=U.CITY);"""
#printTable(executeQuery(query31))

#8
query32 = """SELECT UNIV_NAME, SURNAME, NAME
FROM UNIVERSITY U JOIN STUDENT S
ON S.UNIV_ID=U.UNIV_ID
UNION ALL
SELECT UNIV_NAME, 'Студентов', 'нет'
FROM UNIVERSITY U WHERE NOT EXISTS (SELECT * FROM STUDENT
WHERE UNIV_ID=U.UNIV_ID);"""
#printTable(executeQuery(query32))

# 3.1
# 1
query33 = """INSERT INTO
SUBJECT (SEMESTER, SUBJECT_NAME, HOURS, SUBJECT_ID) VALUES (3, 'Algebra', 72, 205);"""
#executeQueryCommit(query33)

# 2
query34 = """INSERT INTO STUDENT (STUDENT_ID, SURNAME, NAME, KURS, CITY, UNIV_ID)
VALUES (200, 'Orlov', 'Nikolay', 1, 'Voronezh', 5);"""
#executeQueryCommit(query34)

# 3.1
# 2
query35_1 = """CREATE TABLE SUBJECT1 (
                subject_id INT,
                subject_name VARCHAR(50),
                semester INT,
                hours INT,
                PRIMARY KEY (subject_id));"""
#executeQueryCommit(query35_1)

query35_2 = """INSERT INTO SUBJECT1
    SELECT *
    FROM SUBJECT"""
#executeQueryCommit(query35_2)

query35_3 = """DELETE FROM SUBJECT1 WHERE 0 =
(SELECT COUNT(MARK)
FROM EXAM_MARKS
WHERE EXAM_MARKS.SUBJ_ID = SUBJECT1.SUBJECT_ID);"""
#executeQueryCommit(query35_3)

query299 = "Select * from STUDENT"
#printTable(executeQuery(query299))

# 3
query36 = """UPDATE STUDENT
SET STIPEND = STIPEND * 1.2
WHERE STUDENT_ID IN (
  SELECT STUDENT_ID
  FROM EXAM_MARKS
  WHERE MARK IS NOT NULL
  GROUP BY STUDENT_ID
  HAVING SUM(MARK) > 5
);"""
#executeQueryCommit(query36)

query299 = "Select * from STUDENT"
#printTable(executeQuery(query299))
