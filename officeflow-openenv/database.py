import sqlite3

def init_db():
    conn = sqlite3.connect("officeflow.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_name TEXT,
        deadline INTEGER,
        completed INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        action TEXT,
        reward REAL
    )
    """)

    conn.commit()
    conn.close()