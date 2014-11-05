'''
sample pylast code

import pylast

# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from http://www.last.fm/api/account for Last.fm
API_KEY = "b25b959554ed76058ac220b7b2e0a026" # this is a sample key
API_SECRET = "425b55975eed76058ac220b7b4e8a054"

# In order to perform a write operation you need to authenticate yourself
username = "your_user_name"
password_hash = pylast.md5("your_password")

network = pylast.LastFMNetwork(api_key = API_KEY, api_secret =
    API_SECRET, username = username, password_hash = password_hash)

# now you can use that object everywhere
artist = network.get_artist("System of a Down")
artist.shout("<3")


track = network.get_track("Iron Maiden", "The Nomad")
track.love()
track.add_tags(("awesome", "favorite"))

# type help(pylast.LastFMNetwork) or help(pylast) in a Python interpreter to get more help
# about anything and see examples of how it works
'''

import json
import pylast

api_key = "5b859fc1368c4238acb1ba14ffc0c330"
api_secret = "734ea732f54cd69aba43e81434046d59"

usr_name = "jedi_oli"	#replace with your username
pw_hash = pylast.md5("blueberry7")	#replace with your password

network = pylast.LastFMNetwork(api_key = api_key, api_secret = 
    api_secret, username = usr_name, password_hash = pw_hash)

# now you can use that object everywhere
tagLimit = 5
artist = network.get_artist("Kanye West")
tags = artist.get_top_tags(limit=tagLimit)
genre = []
for count in range(0, tagLimit):
    genre.append(tags[count].item.get_name())

for item in genre:
    print item
