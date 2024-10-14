from password import *
import sqlite3
import time
from instagrapi import Client

def add_comment(table_name, text):
    conn = sqlite3.connect("base")
    # Create a cursor object
    cursor = conn.cursor()
    # Create table
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS table_{table_name}
                 (text TEXT)''')
    # Insert data
    cursor.execute(f"INSERT INTO table_{table_name} (text) VALUES (?)", (text,))
    # Commit the changes
    conn.commit()
    # Close the connection
    conn.close()


def get_comment(table):
    conn = sqlite3.connect("base")
    # Create a cursor object
    cursor = conn.cursor()
    # Query the data
    rows = cursor.execute(f"SELECT text FROM table_{table}").fetchall()
    # Close the connection
    conn.close()
    return rows


cl = Client()
cl.login(username, password)
comments = cl.media_comments(post_id)

for comment in comments:
    if comment.text == "+" or comment.text == "++" or comment.text == "+++" or comment.text == "++++" or comment.text == "+++++" or comment.text == "++++++":
        add_comment(post_id, f"{comment.pk}~{comment.user.username}~{comment.text}")

while True:
    comments = cl.media_comments(post_id)
    base_comment = get_comment(post_id)
    for comment in comments:
        if comment.text == "+" or comment.text == "++" or comment.text == "+++" or comment.text == "++++" or comment.text == "+++++" or comment.text == "++++++":
            new_comment = True
            for x in base_comment:
                if f"{comment.pk}~{comment.user.username}~{comment.text}" == x[0]:
                    new_comment = False
                    break
            if (new_comment):
                add_comment(post_id, f"{comment.pk}~{comment.user.username}~{comment.text}")
                comment_author_user_id = cl.user_id_from_username(comment.user.username)
                cl.comment_like(comment.pk)                 # komentga like bosish
                cl.direct_send("Directdan salom",
                                   [comment.user.pk])   # komentga yozgani directiga habar jonatadi
                time.sleep(3)
                cl.media_comment(post_id, "Directdan javob berdik!",
                                 replied_to_comment_id=comment.pk)      # komentariyaga atvet yozish
                time.sleep(3)
    time.sleep(60)



# Step 4: Log out when finished
cl.logout()