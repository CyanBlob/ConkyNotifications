import facebook
import time
import logging

token = 'ENTER_FACEBOOK_TOKEN_HERE'

graph = facebook.GraphAPI(token)

while (True):
    notifications = graph.get_object("me/notifications")

    summary = notifications['summary']

    if summary:
        num = summary['unseen_count']
        with open('facebooknotifications.log', 'w') as f:
            f.write(str(num))

    else:
        with open('facebooknotifications.log', 'w') as f:
            f.write(str(0))

    time.sleep(15)
