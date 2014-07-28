import praw
import time

r = praw.Reddit('Notification script by /u/CyanBlob. Creates a text file with the number of unread messages a user has, to be used with Conky. v0.1')

r.login('USERNAME','PASSWORD')

while (True):
    x = 0
    unread = r.get_unread(limit=None)

    for msg in unread:
        x = x + 1
    with open('redditnotifications.log', 'w') as f:
            f.write(str(x))
    time.sleep(15)
