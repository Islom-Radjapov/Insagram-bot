import sqlite3


def add_comment(table_name, text):
    conn = sqlite3.connect("base")
    # Create a cursor object
    cursor = conn.cursor()
    # Create table
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}
                 (text TEXT)''')
    # Insert data
    cursor.execute(f"INSERT INTO {table_name} (text) VALUES (?)", (text,))
    # Commit the changes
    conn.commit()
    # Close the connection
    conn.close()


def get_comment(table):
    conn = sqlite3.connect("base")
    # Create a cursor object
    cursor = conn.cursor()
    # Query the data
    rows = cursor.execute(f"SELECT text FROM {table}").fetchall()
    # Close the connection
    conn.close()
    return rows
