GigFinder
=========
A super awesome geographic music trend tool!


Summary
========
Our core algorithm consists of three modules:

    GenreSnoop
        which uses the Last.fm API to match music artists with genre tags,

    CountGenre
        which ranks the returned genre tags by artist frequency, and

    MapTweetsToGenre
        which matches tweet location data to genre by the artist-genre mapping from GenreSnoop.


Our directories are as follows:

    mmtd/
        contains our dataset, as well as processed data we use (genres, mappings, etc.)

    genresnoop/
        contains all three of our core algorithm modules: genresnoop2.py, countGenre.py, and mapTweetsToGenre.py

    mapData/
        contains formatted tweet location data, sorted into different genre files

    dist/
        contains Bootstrap js and css files for our webpage


Dependencies
=========
Python libraries : pylast
    Can be installed with 'pip install pylast'.

Dataset: the Million Musical Tweets Dataset (MMTD), found here: http://www.cp.jku.at/datasets/MMTD/
    'mmtd.txt'      contains tweets with location and artist data
    'artist.txt'    contains all musical artists from the MMTD in a separate file


Instructions
=========
1.  Run the Python script 'python genresnoop/genresnoop2.py', which will read in artistID's from 'mmtd/artists.txt' and output artistID's with their top 5 genre tags in 'mmtd/artistGenre.txt'. Genre tags are user-generated on Last.fm, so we take the top 5 to reduce strange inputs. This may take a little time to run on all of the artists.

2.  Run 'python genresnoop/countGenre.py' which reads in genre tags from 'mmtd/artistGenre.txt',  counts up the frequency of each genre in the dataset, and outputs a sorted list of genres in decreasing frequency order to 'mmtd/topGenre.txt.' This script will take a good amount of time to run; it took us a couple of days running on TAMU's compute server.

3.  Run 'python genresnoop/mapTweetsToGenre.py'. This script runs on the entire dataset in 'mmtd/mmtd.txt'. First it finds the top 50 genres from 'mmtd/topGenre.txt', which will serve as "buckets" for sorting tweets. It then extracts individual tweets from 'mmtd/mmtd.txt', using only the tweetID, artistID, and location data. Using the mapping in 'mmtd/artistGenre.txt,' the script maps the tweet to the 5 genres corresponding to its artistID. If at least one of those genres are in the top 50, the tweet location is sorted into the corresponding genre bucket(s). Otherwise the location is placed in the "other" genre bucket. Lastly, the genre buckets (including "other") are output as text files with the naming convention 'mapData/<genre>MapData.txt'.


=========
THANK YOU! Let us know if you have any questions!!