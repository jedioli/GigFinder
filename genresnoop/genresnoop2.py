import json
import time
import re
import sys
sys.path.append("../../.local/lib/python2.7/site-packages/")
import pylast

api_key = "5b859fc1368c4238acb1ba14ffc0c330"
api_secret = "734ea732f54cd69aba43e81434046d59"

usr_name = "jedi_oli"	#use this for now; usually you would replace with your username
pw_hash = pylast.md5("blueberry7")	#as above

network = pylast.LastFMNetwork(api_key = api_key, api_secret = 
    api_secret, username = usr_name, password_hash = pw_hash)

artistFile = open("../mmtd/artists.txt", "r")
tagLimit = 5

# read title line
artistFile.readline()
jumpToLine = 0
if len(sys.argv) == 2:
    jumpToLine = int(sys.argv[1])
else:
    jumpToLine = 0
#skips to a line
for i in range(0, jumpToLine):
    artistFile.readline()
    

artistOut = open("../mmtd/artistGenre.txt", "a")

for num in range(jumpToLine, 1000000):
    line = artistFile.readline()
    tokens = re.split(r'\t+', line.rstrip('\t'))
    if len(tokens) == 3:
        if tokens[2] != " " and len(tokens[2]) != 0 and tokens[2] != "" and tokens[2] != "\t" and tokens[2] != "\n" and tokens[2] != "\n\r" and tokens[2] != "\r":
            
            try:
                artistName = tokens[2].decode('utf-8')
                artistName = artistName.encode("ascii", "ignore")
            except:
                print "Most likely unicode error on artist:" + str(num)
                sys.exc_clear()
                continue
                pass
            nameList = re.split("\"", artistName)
            newName = ""
            tags = []
            for part in nameList:
                newName += part
            try:
                artistInfo = network.get_artist(newName)
                tags = artistInfo.get_top_tags(limit=tagLimit)
            except:
                print "Error with artist" + newName
                sys.exc_clear()
                continue
                pass
            
            genre = []
            genreString = ""
            if len(tags) != 0:
                for count in range(0, len(tags)):
                    try:
                        tagName = tags[count].item.get_name().decode('utf-8')
                        tagName = tagName.encode("ascii", "ignore")
                    except:
                        print "Most likely unicode error on artist:" + str(num)
                        sys.exc_clear()
                        continue
                        pass
                    genre.append(tagName)
                    genreString += tagName + "\t"
                artistOut.write(tokens[0] + "\t" + genreString + "\n")
                print tokens[0] + " " + genreString
            time.sleep(0.2)
    else :
        print "No artist for id " + tokens[0]
    if num % 100 == 0:
	print "Flushing I/O buffer"
	artistOut.flush()

artistOut.close()

