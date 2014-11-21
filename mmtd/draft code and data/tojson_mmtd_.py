import json
#from here: http://stackoverflow.com/questions/11059390/parsing-a-tab-separated-file-in-python
import csv

mmtd = []
headers = []
liner = 0
with open("mmtd.txt", 'r') as csv_mmtd:
	mmtd_reader = csv.reader(csv_mmtd, dialect='excel-tab')
	#another hint: http://stackoverflow.com/questions/26384531/csv-reader-repeatedly-reading-1-line
	for line_num, line in enumerate(mmtd_reader):
		liner = line_num
		if line_num == 0:
			headers = line
		else:
		#from index 0 to 36, removes language fields
			entry = dict()
			for index in range(37):
				entry[headers[index]] = line[index]
			mmtd.append(entry)
		if line_num % 10000 == 0:
			print "finished " + str(line_num) + " tweets"

print "parsed all tweets: " + str(liner) + " of them!"
print "length of mmtd: " + str(len(mmtd))

texas = []
for tweet_num, tweet in enumerate(mmtd):
	if tweet_num % 100000 == 0:
		print "parsed through " + str(tweet_num) + " tweets"
	if tweet[headers[17]] == 'TX':
		texas.append(tweet)

print "parsed texas tweets"
print "length of texas: " + str(len(texas))

with open('texas.json','w') as tex_tweets:
	json.dump(texas, tex_tweets)
	
print "texas json dumped"

with open('mmtd.json','w') as alltweets:
	json.dump(mmtd, alltweets)

print "mmtd json dumped"