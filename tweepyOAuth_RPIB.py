import tweepy

auth = tweepy.OAuthHandler("pwIYlJhhW89yuNDKHFfefIPDG",
    "AwkpCFOaWpW6cSRG7MLywAupsHNi0s7H8mUT6PMUIIez8nDmP2")
auth.set_access_token("1462802761783947271-u1Z0JFo8e1db7DAsk0vEXNAwmc51YA",
    "Q1OU6aDOgB9NgaW4A02jJy0Ns5qEbCKA1KkHKTvzylDME")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Auth OK")
except:
    print("Auth Err")
