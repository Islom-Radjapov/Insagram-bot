from password import *

from instagrapi import Client
cl = Client()
cl.login(username, password)

comments = cl.media_comments(post_id)
for comment in comments:
    if comment.text == "+++":
        print(f"@{comment.user.username}: {comment.text}")
        cl.media_comment(post_id, "wasdfghsdfghvb", replied_to_comment_id=comment.pk) # komentariyaga atvet yozish
        comment_author_user_id = cl.user_id_from_username(comment.user.username)
        a = cl.direct_send("message_text skdfdbgljlbdkfjlbkdjflbkjdlfkj", [comment_author_user_id]) # komentga yozgani directiga habar jonatadi
        print(a)





# Log out when finished
cl.logout()