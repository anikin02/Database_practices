import sqlite3

def executeQuery(query):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    return result

def executeQueryCommit(query):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

def printTable(result):
    if len(result) == 0:
        print("No data available.\n")
        return
    for row in result:
        print(*row)
    print("\n")

def printTableStudent():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("Select * from Student")
    result = cursor.fetchall()
    printTable(result)
    connection.close()

def printTableSubject():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("Select * from Subject")
    result = cursor.fetchall()
    printTable(result)
    connection.close()
    
def printTableUniversity():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("Select * from University")
    result = cursor.fetchall()
    printTable(result)
    connection.close()
    
def printTableExam():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("Select * from Exam_marks")
    result = cursor.fetchall()
    printTable(result)
    connection.close()
