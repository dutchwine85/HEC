import tweepy

API_key = "pwIYlJhhW89yuNDKHFfefIPDG"
API_secret = "AwkpCFOaWpW6cSRG7MLywAupsHNi0s7H8mUT6PMUIIez8nDmP2"
Access_token = "1462802761783947271-u1Z0JFo8e1db7DAsk0vEXNAwmc51YA"
Access_token_secret = "Q1OU6aDOgB9NgaW4A02jJy0Ns5qEbCKA1KkHKTvzylDME"

callback_uri = "oob"

auth = tweepy.OAuthHandler(API_key, API_secret, callback_uri)
auth.set_access_token(Access_token, Access_token_secret)

redirect_url = auth.get_authorization_url()
print(redirect_url)

# LAST BUILD STEP ->
################# MANUAL OVERRIDE - remove >>>
exec(open("OAutomator.py").read())
"""
# oaPIN = input("Add PIN -> ")
# print("\n")
# auth.get_access_token(oaPIN)
# driver. close()
"""

import time
API = tweepy.API(auth)

print("|")
time.sleep(0.1)
print("|")
time.sleep(0.1)
print("v")
time.sleep(0.5)
print(z_file)
print(docName)

upload = API.media_upload(filename=r"/Users/tomweston/PycharmProjects/HEC/z_img_chosen/"+z_file)
print()
print("File stats : " + (str(upload)))
print(upload.media_id_string)
mID = [upload.media_id_string]
API.update_status(media_ids=mID, status=docName[:-6])