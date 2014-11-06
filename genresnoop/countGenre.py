
import re
import operator

artistFile = open("../mmtd/artistGenre.txt", "r")
genres = {}
for line in artistFile:
    tokens = re.split(r'\t', line.rstrip("\t"))
    for num in range(1, len(tokens)-1):
        if genres.has_key(tokens[num].lower()) == True:
            genres[tokens[num].lower()] += 1
        else:
            genres[tokens[num].lower()] = 1


genresSorted = sorted(genres.iteritems(), key = operator.itemgetter(1), reverse = True)

print genresSorted

genreFile = open("../mmtd/topGenre.txt", "w")

for item in genresSorted:
    genreFile.write(item[0] + "\t")
    genreFile.write(str(item[1]))
    genreFile.write("\n")
    
genreFile.close()
