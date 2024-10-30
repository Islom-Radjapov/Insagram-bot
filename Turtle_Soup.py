import sqlite3
import time
from instagrapi import Client

post_id = ""
username = ""
password = ""

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
    if comment.text == "+" or " " * len(comment.text):
        add_comment(post_id, f"{comment.pk}~{comment.user.username}~{comment.text}")
print("Start")
while True:
    try:
        comments = cl.media_comments(post_id)
        base_comment = get_comment(post_id)
        for comment in comments:
            if comment.text == "+" or " " * len(comment.text):
                new_comment = True
                for x in base_comment:
                    if f"{comment.pk}~{comment.user.username}~{comment.text}" == x[0]:
                        new_comment = False
                        break
                if (new_comment):
                    add_comment(post_id, f"{comment.pk}~{comment.user.username}~{comment.text}")
                    cl.comment_like(comment.pk)                 # komentga like bosish
                    time.sleep(2)
                    cl.direct_send(f"""Assalomu alekum {comment.user.full_name} ICT konsepsiyasidagi Turtle Soup modelni o'rganib foydaga chiqishingiz aniq! 💯\nDarslik online formatda telegramda bo'lib o'tadi, darsligimiz mutlaqo bepul ammo bizni qoidalarimizga rioya qilishingiz kerak! guruhga qoshilish uchun adminga murojat qiling🤗""",
                                       [comment.user.pk])   # komentga yozgani directiga habar jonatadi
                    time.sleep(2)
                    cl.direct_send("https://t.me/Billion_Trade_Club_admin", [comment.user.pk])
                    time.sleep(2)
                    cl.media_comment(post_id, f"Salom {comment.user.username} sizga directdan habar yubordik😊", replied_to_comment_id=comment.pk)      # komentariyaga atvet yozish
                    #cl.media_comment_reply(post_id, comment.pk, "Thank you for your comment!")
                    time.sleep(5)
    except Exception as e:
        print(f"ERROR: {e}")
    time.sleep(1)



# Step 4: Log out when finished
cl.logout()
