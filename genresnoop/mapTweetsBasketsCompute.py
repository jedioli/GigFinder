import re


def euclid_within(loc1, loc2):
    dist = 0.0
    for coord in range(2):
        dist += (loc1[coord] - loc2[coord]) * (loc1[coord] - loc2[coord])
    
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


genreBox = []

#just did 80s
#just did all
#genreBox.append('alternative rock')    #don't need escaped space!
#genreBox.append('alternative')
#genreBox.append('ambient')
#genreBox.append('black metal')
#genreBox.append('blues')
#genreBox.append('chillout')
#genreBox.append('dance')
#genreBox.append('death metal')
#genreBox.append('drum and bass')
#genreBox.append('electro')
#skip electronic
#genreBox.append('electronica')
#genreBox.append('experimental')
#genreBox.append('female vocalists')
#genreBox.append('folk')
#genreBox.append('french')
#genreBox.append('funk')
#genreBox.append('german')
#genreBox.append('hard rock')
#genreBox.append('hardcore')
#genreBox.append('heavy metal')
#genreBox.append('hip hop')
#genreBox.append('hip-hop')
#genreBox.append('house')
#genreBox.append('indie rock')
#genreBox.append('indie')
#genreBox.append('industrial')
#genreBox.append('instrumental')
#genreBox.append('japanese')
#genreBox.append('jazz')
#genreBox.append('metal')
#genreBox.append('noise')
#genreBox.append('others')
#skip pop
#genreBox.append('progressive rock')
#genreBox.append('psychedelic')
#genreBox.append('punk rock')
#genreBox.append('punk')
#genreBox.append('rap')
#genreBox.append('reggae')
#skip rock
#genreBox.append('seen live')
#genreBox.append('singer-songwriter')
#genreBox.append('soul')
#skip spotify
#genreBox.append('swedish')
#genreBox.append('techno')
#genreBox.append('trance')
#genreBox.append('under 2000 listeners')

genreBox.append('rock')
genreBox.append('pop')
genreBox.append('hip-hop')
genreBox.append('alternative')
genreBox.append('rap')
genreBox.append('indie')
genreBox.append('electronic')
genreBox.append('soul')
genreBox.append('singer-songwriter')
genreBox.append('dance')

for genre in genreBox:

    print "starting " + genre
    
    map_data = "../mapData/" + genre + "MapData.txt"

    baskets = {}
    with open(map_data, "r") as data_file:
        for line_num, line in enumerate(data_file):
            if line_num == 0:
            #    print "throw out header"
                continue
            tokens = re.split(r'\t', line.rstrip("\t"))
                #   0   1   2   3
                #   ID  lat lng cntnt
            loc = (float(tokens[1]), float(tokens[2]), tokens[3])
        
            if len(baskets) < 1:
                baskets[loc] = 1
                continue
    
            for center_loc in baskets:
                if euclid_within(center_loc, loc):
                    baskets[center_loc] += 1
                    break
            else:
                baskets[loc] = 1

            if len(baskets) % 1000 == 0:
                print "num baskets = " + str(len(baskets))


    print "baskets ready for " + genre

    out_basket = "../mapBaskets2/" + genre + "Basket.txt"

    with open(out_basket, 'w') as out_file:
        out_file.write("Latitude \t Longitude \t Weight \t Continent\n")
        for loc in baskets:
            out_file.write(str(loc[0]) + '\t' + str(loc[1]) + '\t' + str(baskets[loc]) + '\t' + loc[2] + '\n')
    
    print "************ finished " + genre + " ************"
    print

print "all done!"
