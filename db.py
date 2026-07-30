import sqlite3
import csv

DB_PATH = 'students.db'

def get_conn():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            grade REAL
        )
        '''
    )
    conn.commit()
    conn.close()

def add_student(name, age, grade):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('INSERT INTO students (name, age, grade) VALUES (?, ?, ?)', (name, age, grade))
    conn.commit()
    conn.close()

def list_students():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('SELECT id, name, age, grade FROM students')
    rows = cur.fetchall()
    conn.close()
    return rows

def find_student(name_query):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('SELECT id, name, age, grade FROM students WHERE name LIKE ?', (f'%{name_query}%',))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_student(student_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()
    conn.close()

def export_csv(path='students.csv'):
    rows = list_students()
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'name', 'age', 'grade'])
        writer.writerows(rows)
