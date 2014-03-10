"""
A location spoofer using tweepy and Twitter's API.
Could be used to mess with people.
Or for more serious purposes, like hiding locations from oppressive governments.
Who knows...
"""
import tweepy

"""
Initializes the API.
Here's where it gets interesting. Because I don't know of any good ways of securing the keys from others, I'm just going to remove them.
If you want access keys, email me at kmschapm AT oakland DOT edu.
Don't spam me though. That's bad.
"""
consumer_key = ''
consumer_secret = ''
token_key = ''
token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(token_key, token_secret)
api = tweepy.API(auth)

# Making a status. The location part comes later!
tweet = raw_input("\nWhat's on your mind? ")
lat = input("\nAlright! Now, enter in the LATITUDE of your \"location\": ")
longitude = input("And now, your LONGITUDE: ")

# Now, we take these three bits of information and mix them all up...
api.update_status(status=tweet, lat=lat, long=longitude)
