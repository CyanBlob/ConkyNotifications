ConkyNotifications
==================

A collection of Conky and some scripts to enable the display of notifications from common websites


#### HOW TO USE ####

Reddit notifications: Install PRAW (https://praw.readthedocs.org/en/v2.1.16/) and Python, the script will make a log file (default redditnotifications.log in the same directory as the script). From Conky, use ${exec tail /path/to/redditnotifications.log} to return the current number of notifications (updates every 15seconds by default, changeable easily within the script)

==================

Facebook notifications: Install the Facebook Python API (sudo pip install facebook-sdk). Receive a Facebook token from https://developers.facebook.com/tools/explorer/ by clicking 'Get Access Token' #### NOTE: I am unsure which funcionalities are required for the script to run. I checked all the boxes, just to be sure it works, but this is probably very insecure #### The script will make a log file (default facebooknotifications.log in the same directory as the script). From Conky, use ${exec tail -n 1 /home/andrew-mint/Scripts/facebooknotifications.log} to return the current number of notifications (updates every 15seconds by default, changeable easily within the script)
