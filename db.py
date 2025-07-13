import sqlite3 as sl

def init_db():
    conn= sl.connect('data.db')
    c=conn.cursor()
    c.execute('''
              CREATE TABLE IF NOT EXISTS tasks(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  category TEXT NOT NULL,
                  hours REAL NOT NULL,
                  date TEXT NOT NULL
              )''')
    conn.commit()
    conn.close()
    
def add_task(name, category, hours ,date):
    conn= sl.connect('data.db')
    c=conn.cursor()
    c.execute('''INSERT INTO tasks(name, category, hours, date) VALUES(?,?,?,?)''',(name, category, hours, date))
    conn.commit()
    conn.close()

def get_all_tasks():
    conn=sl.connect('data.db')
    c=conn.cursor()
    c.execute('''SELECT * FROM tasks ORDER BY date DESC''')
    data=c.fetchall()
    conn.close()
    return data