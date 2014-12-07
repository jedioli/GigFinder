
import re
#import csv
#import operator
import sys
from math import sqrt

'''
artistCountFile = open("../mmtd/topGenre.txt","r")

topGenreDict = {}
'''


def euclid_within(loc1, loc2):
    dist = 0.0
    for coord in range(2):
        dist += (loc1[coord] - loc2[coord]) * (loc1[coord] - loc2[coord])
    
    #dist = sqrt(dist)
    
    #if dist < 0.01414:
    #if dist < 0.1414:
    if dist < 0.02:
        return True
    else:
        return False

def round_within(loc1, loc2):
    round1 = (round(loc1[0], 1), round(loc1[1], 1))
    round2 = (round(loc2[0], 1), round(loc2[1], 1))

    if round1[0] == round2[0] and round1[1] == round2[1]:
        return True
    else:
        return False


#genre = "rock"
genre = sys.argv[1]

map_data = "../mapData/" + genre + "MapData.txt"

baskets = {}
#line_num = 0
with open(map_data, "r") as data_file:
    for line_num, line in enumerate(data_file):
        if line_num == 0:
            print "throw out header"
            continue
        tokens = re.split(r'\t', line.rstrip("\t"))
            #   0   1   2   3
            #   ID  lat lng cntnt
        loc = (float(tokens[1]), float(tokens[2]))
        
        if len(baskets) < 1:
            baskets[loc] = 1
            continue
    
        for center_loc in baskets:
            if euclid_within(center_loc, loc):
                baskets[center_loc] += 1
                break
        else:
            baskets[loc] = 1

        if len(baskets) % 100 is 0: #ONLY USE for memory location compare!
            print "num baskets = " + str(len(baskets))


print "baskets ready"

out_basket = "../mapBaskets/" + genre + "Basket.txt"

with open(out_basket, 'w') as out_file:
    out_file.write("Latitude \t Longitude \t Weight\n")
    for loc in baskets:
        out_file.write(str(loc[0]) + '\t' + str(loc[1]) + '\t' + str(baskets[loc]) + '\n')
    
    
    
    '''
    
out_file = open(out_basket, 'w')

out_file.write("Latitude \t Longitude \t Weight\n")
for loc in baskets:
    out_file.write(str(loc[0]) + '\t' + str(loc[1]) + '\t' + str(baskets[loc]) + '\n')
    
out_file.close() 
    
    '''
    
    
    

'''
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
#    tweetId = line[0]
    artistId = line[3]
    longitude = line[8]
    latitude = line[9]
    continent = line[27]
    weight = 1
    location = {}

    if artistId in artistDict:
        found = False
        for genre in artistDict[artistId]:
            if genre in topGenreDict:
                
                # addition for sorting into baskets
                if
                
                
                topGenreDict[genre].append([tweetId,latitude,longitude,continent])
                found = True
        if not found:
            otherGenre.append([tweetId,latitude,longitude,continent])

topGenreDict["others"] = otherGenre
genreTweets = {}
for genre,tweets in topGenreDict.iteritems():
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
'''


