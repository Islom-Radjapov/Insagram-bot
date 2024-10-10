from password import *

from instagrapi import Client
cl = Client()
cl.login(username, password)

try:
    # Get the post's media ID (primary key) from URL
    media_id = cl.media_pk_from_url(url)
    print(f"Retrieved Media ID: {media_id}")

    # Fetch comments using the retrieved media ID
    comments = cl.media_comments(media_id)
    print(f"Comments for the post ID {media_id}:\n")
    for comment in comments:
        print(f"@{comment.user.username}: {comment.text}")
except Exception as e:
    print(f"An error occurred: {e}")



"""
comments = cl.media_comments(post_id)
for comment in comments:
    print(comment, "Coment text => ", comment.text)
"""


# Log out when finished
cl.logout()