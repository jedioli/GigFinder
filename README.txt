GigFinder
=========
A super awesome geographic music trend tool!


NOTE: All API keys (and referenced usernames and passwords) previously used in this project are now null, void, and deleted. Should you wish to view index.html or run genresnoop2.py, you must obtain your own API keys for Google Maps and Last.fm, respectively.


Summary
========
Our core algorithm consists of five modules:

    GenreSnoop
        which uses the Last.fm API to match music artists with genre tags,

    CountGenre
        which ranks the returned genre tags by artist frequency, 

    MapTweetsToGenre
        which matches tweet location data to genre by the artist-genre mapping from GenreSnoop,
    
    MapTweetsBasketsCompute
        which finds the number of tweets in a small area and combines them into a single weighted point, and
    
    FindGig
        which searches through the weighted points for each genre and continent and finds the largest weighted point.

In addition, our GigFinder application:
    
    index.html
        which is deployed as a local Javascript application integrated with Google Maps and uses data in mapBaskets/ and Gig3/.

Our directories are as follows:

    mmtd/
        contains our dataset, as well as processed data we use (genres, mappings, etc.)

    genresnoop/
        contains all five of our core algorithm modules: genresnoop2.py, countGenre.py, mapTweetsToGenre.py, mapTweetsBasketsCompute.py, and findGig4.py

    mapData/
        contains formatted tweet location data, sorted into different genre files

    dist/
        contains Bootstrap .js and .css files for our webpage
    
    mapBaskets/
        contains the weighted points without continent information
        NOTE: only the top 10 unique genres (by frequency) display in index.html, but all of our data is included here.
    
    mapBasketsCnt/
        contains the weighted points with continent information
    
    Gigs3/
        contains the location of the highest concentration of points for each genre and continent


Dependencies
=========
Python libraries : pylast
    Can be installed with 'pip install pylast'.

Dataset: the Million Musical Tweets Dataset (MMTD), found here: http://www.cp.jku.at/datasets/MMTD/. Due to the large size of 'mmtd.txt', we request that you DOWNLOAD it yourself at the aforementioned link and PLACE it within 'mmtd/'.

    'mmtd.txt'      contains tweets with location and artist data
    'artists.txt'    contains all musical artists from the MMTD in a separate file


Instructions
=========
0.  Navigate to 'genresnoop/'. All of our filepaths depend on running the scripts from this directory.

1.  Run the Python script 'python genresnoop2.py', which will read in artistID's from 'mmtd/artists.txt' and output artistID's with their top 5 genre tags in 'mmtd/artistGenre.txt'. Genre tags are user-generated on Last.fm, so we take the top 5 to reduce strange inputs. This may take some time to run on all of the artists.

2.  Run 'python countGenre.py' which reads in genre tags from 'mmtd/artistGenre.txt',  counts up the frequency of each genre in the dataset, and outputs a sorted list of genres in decreasing frequency order to 'mmtd/topGenre.txt.'

3.  Run 'python mapTweetsToGenre.py'. This script runs on the entire dataset in 'mmtd/mmtd.txt'. First it finds the top 50 genres from 'mmtd/topGenre.txt', which will serve as "buckets" for sorting tweets. It then extracts individual tweets from 'mmtd/mmtd.txt', using only the tweetID, artistID, and location data. Using the mapping in 'mmtd/artistGenre.txt,' the script maps the tweet to the 5 genres corresponding to its artistID. If at least one of those genres are in the top 50, the tweet location is sorted into the corresponding genre bucket(s). Otherwise the location is placed in the "other" genre bucket. Lastly, the genre buckets (including "other") are output as text files with the naming convention 'mapData/<genre>MapData.txt'.

4.  Run 'python mapTweetsBasketsCompute.py'. This script preprocesses the location data points by clustering nearby points into a single weighted point.

5.  Run 'python findGig4.py'. This script finds the largest weighted point from those created by mapTweetsBasketsCompute.py.


->  Once the data has been loaded into mapBaskets/ and Gig3/, you can view and use the GigFinder tool in index.html!

=========
THANK YOU! Let us know if you have any questions!!
