import math
import re
import csv
import operator

artistCountFile = open("../mmtd/topGenre.txt","r")

topGenreDict = {}
lineCount = 0
for lineCount,line in enumerate(artistCountFile):
    if lineCount == 50:
        break
    tokens = re.split(r'\t', line.rstrip("\t"))
    if tokens[0] not in topGenreDict:
        topGenreDict[tokens[0]] = []


artistFile = open("../mmtd/artistGenre.txt", "r")
artistDict = {}
for line in artistFile:
    tokens = re.split(r'\t', line.rstrip("\t"))
    artistDict[tokens[0]] = []
    for num in range(1, len(tokens)-1):
            artistDict[tokens[0]].append(tokens[num].lower())


otherGenre = []

#0 is tweet id
#3 is artistid
#8 longitude
#9 latitude
#27 continent
tweetFile = open("../mmtd/mmtd.txt")
tweetFile.readline()

mmtd_reader = csv.reader(tweetFile, dialect='excel-tab')
for line_num,line in enumerate(mmtd_reader):
    #if line_num == 100:
    #   break
    tweetId = line[0]
    artistId = line[3]
    longitude = line[8]
    latitude = line[9]
    continent = line[27]

    if artistId in artistDict:
        found = False
        for genre in artistDict[artistId]:
            if genre in topGenreDict:
                topGenreDict[genre].append([tweetId,latitude,longitude,continent])
                found = True
        if not found:
            otherGenre.append([tweetId,latitude,longitude,continent])

topGenreDict["others"] = otherGenre
genreContDict = {}
for genre in topGenreDict:
    genreContDict[genre] = {}
    for item in topGenreDict[genre]:
        #print genre
        #print item
        genreContDict[genre][item[3]] = []
for genre in topGenreDict:
    for item in topGenreDict[genre]:
        genreContDict[genre][item[3]].append([item[0],item[1],item[2]])

locationScoreDict = {}
locationDict = {}
for genre in genreContDict:
    locationScoreDict[genre] = {}
    locationDict[genre] = {}
    for continent in genreContDict[genre]:
        print genre
        print continent
        #print len(genreContDict[genre][continent])
        locationScoreDict[genre][continent] = 0
        locationDict[genre][continent] = [0,0]
        for item1 in genreContDict[genre][continent]:
            score = 0.
            for item2 in genreContDict[genre][continent]:
                #print item1
                #print item2
                if(item1 is item2):
                    continue
                distance = math.sqrt((float(item2[1]) - float(item1[1]))**2 + (float(item2[2]) - float(item1[2]))**2)
                if(distance == 0):
                    distance = .000001
                #distance *= 1000
                #print distance
                score += 1/(distance**2)
            #print score
            if(score > locationScoreDict[genre][continent]):
                locationScoreDict[genre][continent] = score
                locationDict[genre][continent] = [item1[1],item1[2]]
                #print locationDict[genre][continent]
        fileName = "../Gigs/" + genre + continent + ".txt"
        outFile = open(fileName,'w')
        outFile.write("Genre \t Continent \t Latitude \t Longitude\n")
        outFile.write(genre + "\t" + continent + "\t" + str(locationDict[genre][continent][0]) + "\t" + str(locationDict[genre][continent][1]) + "\n")
        outFile.close()

fileName = "../GigLocations2.txt"
outFile = open(fileName,'w')
outFile.write("Genre \t Continent \t Latitude \t Longitude\n")
for genre_name, genre in locationDict.iteritems():
    #print genre_name
    #print genre
    for location_name, location in genre.iteritems():
        outFile.write(genre_name + "\t" + location_name + "\t" + str(location[0]) + "\t" + str(location[1]) + "\n")
outFile.close()


"""for genre,tweets in topGenreDict.iteritems():
    fileName = "../mapData/"+ genre + "MapData.txt"
    outFile = open(fileName,'w')
    outFile.write("Tweet Id \t Latitude \t Longitude \t Continent\n")
    for data in tweets:
        for item in data:
            outFile.write(item)
            outFile.write('\t')
        outFile.write('\n')

    outFile.close()

    genreTweets[genre] = len(tweets)



genresSorted = sorted(genreTweets.iteritems(), key = operator.itemgetter(1), reverse = True)

print genresSorted

genreFile = open("../mmtd/topGenreByTweet.txt", "w")

for item in genresSorted:
    genreFile.write(item[0] + "\t")
    genreFile.write(str(item[1]))
    genreFile.write("\n")

genreFile.close()
"""


