# this file is the local version of mapTweetsBasketsCompute.py,
#   and is not really used.


import re
import sys
from math import sqrt



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


genre = sys.argv[1]

map_data = "../mapData/" + genre + "MapData.txt"

baskets = {}
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

        if len(baskets) % 100 == 0:
            print "num baskets = " + str(len(baskets))


print "baskets ready"

out_basket = "../mapBaskets/" + genre + "Basket.txt"

with open(out_basket, 'w') as out_file:
    out_file.write("Latitude \t Longitude \t Weight\n")
    for loc in baskets:
        out_file.write(str(loc[0]) + '\t' + str(loc[1]) + '\t' + str(baskets[loc]) + '\n')