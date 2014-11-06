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
import time
import re
import sys

api_key = "5b859fc1368c4238acb1ba14ffc0c330"
api_secret = "734ea732f54cd69aba43e81434046d59"

usr_name = "jedi_oli"	#replace with your username
pw_hash = pylast.md5("blueberry7")	#replace with your password

network = pylast.LastFMNetwork(api_key = api_key, api_secret = 
    api_secret, username = usr_name, password_hash = pw_hash)

# now you can use that object everywhere

artistFile = open("../mmtd/artists.txt", "r")
tagLimit = 5

# read title line
artistFile.readline()

artistOut = open("../mmtd/artistGenre.txt", "w")

for num in range(0, 10000):
    line = artistFile.readline()
    tokens = re.split(r'\t+', line.rstrip('\t'))
    if len(tokens) == 3:
        if tokens[2] != " " and len(tokens[2]) != 0 and tokens[2] != "" and tokens[2] != "\t" and tokens[2] != "\n" and tokens[2] != "\n\r" and tokens[2] != "\r":
            artistName = tokens[2]
            nameList = re.split("\"", artistName)
            newName = ""
            for part in nameList:
                newName += part
            try:
                artistInfo = network.get_artist(newName)
                tags = artistInfo.get_top_tags(limit=tagLimit)
            except:
                print "Error with artist" + newName
                sys.exc_clear()
                pass
            
            genre = []
            genreString = ""
            if len(tags) != 0:
                for count in range(0, len(tags)):
                    genre.append(tags[count].item.get_name())
                    genreString += tags[count].item.get_name() + "\t"
                artistOut.write(tokens[0] + "\t" + genreString + "\n")
                print tokens[0] + " " + genreString
            time.sleep(0.3)
    else :
        print "No artist for id " + tokens[0]

artistOut.close()

'''
artist = network.get_artist("Kanye West")
tags = artist.get_top_tags(limit=tagLimit)
genre = []
for count in range(0, tagLimit):
    genre.append(tags[count].item.get_name())

for item in genre:
    print item
'''
