
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
    
    if artistId in artistDict:
        found = False
        for genre in artistDict[artistId]:
            if genre in topGenreDict:
                topGenreDict[genre].append([tweetId,latitude,longitude])
                found = True
        if not found:
            otherGenre.append([tweetId,latitude,longitude])
        
topGenreDict["others"] = otherGenre
genreTweets = {}
for genre,tweets in topGenreDict.iteritems():
    fileName = "../mapData/"+ genre + "MapData.txt"
    outFile = open(fileName,'w')
    outFile.write("Tweet Id \t Latitude \t Longitude\n")
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
        
    
    
