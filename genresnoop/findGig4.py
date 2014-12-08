import math
import re
import csv
import operator

genres = ['alternative','dance','electronic','hip-hop','indie','pop','rap','rock','singer-songwriter','soul']
continents = ['Africa','Asia','Europe','North America','NULL','Oceania','South America','Antarctica']
for genre in genres:
	highScores = {}
	locations = {}
	for continent in continents:
		highScores[continent] = 0
		locations[continent] = [0.0,0.0]
	file = open("../mapBaskets2/" + genre + "Basket.txt")
	file.readline()
	reader = csv.reader(file,dialect='excel-tab')
	for line_num,line in enumerate(reader):
		latitude = float(line[0])
		longitude = float(line[1])
		weight = int(line[2])
		continent = line[3]
		if(weight > highScores[continent]):
			highScores[continent] = weight
			locations[continent][0] = latitude
			locations[continent][1] = longitude
	for continent in continents:
		output = open("../Gigs3/" + genre + continent + ".txt",'w')
		output.write("Genre \t Continent \t Latitude \t Longitude\n")
		output.write(genre + "\t" + continent + "\t" + str(locations[continent][0]) + "\t" + str(locations[continent][1]) + "\n")
		output.close()
