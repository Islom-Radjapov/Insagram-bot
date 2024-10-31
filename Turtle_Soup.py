import sqlite3
import time
from instagrapi import Client

post_id = "3488854135114788553"  # Replace with your target post's ID
username = "b1llion.uz"
password = "3333billion"

def add_comment(text):
    conn = sqlite3.connect("base")
    # Create a cursor object
    cursor = conn.cursor()
    # Create table
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS table_1 (text TEXT)''')
    # Insert data
    cursor.execute(f"INSERT INTO table_1 (text) VALUES (?)", (text, ))
    # Commit the changes
    conn.commit()
    # Close the connection
    conn.close()


def check_existence(value):
    # Connect to the SQLite database
    conn = sqlite3.connect("base")
    cursor = conn.cursor()

    # Prepare the SQL query
    query = f"SELECT EXISTS(SELECT 1 FROM table_1 WHERE text = ?)"

    # Execute the query
    cursor.execute(query, (value,))

    # Fetch the result
    exists = cursor.fetchone()[0]  # returns 1 if exists, 0 otherwise
    # Close the connection
    conn.close()
    return bool(exists)



cl = Client()
cl.login(username, password)
comments = cl.media_comments(post_id)

for comment in comments:
    if comment.text == "+" or " " * len(comment.text):
        if comment.user.username != "b1llion.uz":
            add_comment(comment.pk)

print("Start")
while True:
    try:
        comments = cl.media_comments(post_id)
        for comment in comments:
            if comment.user.username != "b1llion.uz":
                if comment.text == "+" or " " * len(comment.text):
                    if (check_existence(comment.pk) == False):
                        cl.comment_like(comment.pk)                 # komentga like bosish
                        cl.direct_send(f"""Assalomu alekum {comment.user.full_name} ICT konsepsiyasidagi Turtle Soup modelni o'rganib foydaga chiqishingiz aniq! 💯\nDarslik online formatda telegramda bo'lib o'tadi, darsligimiz mutlaqo bepul ammo bizni qoidalarimizga rioya qilishingiz kerak! guruhga qoshilish uchun adminga murojat qiling🤗""",
                                           [comment.user.pk])   # komentga yozgani directiga habar jonatadi
                        cl.direct_send("https://t.me/Billion_Trade_Club_admin", [comment.user.pk])
                        cl.media_comment(post_id, f"Salom {comment.user.username} sizga directdan habar yubordik😊", replied_to_comment_id=comment.pk)      # komentariyaga atvet yozish
                        add_comment(comment.pk)
                        time.sleep(3)
    except Exception as er:
        print("ERROR: ", er)
    time.sleep(3)



# Step 4: Log out when finished
cl.logout()

