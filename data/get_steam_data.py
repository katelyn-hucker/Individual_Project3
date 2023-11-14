"""
In this python script we retrieve steam data with filters of interest. 

There are two routes here: API usage for everything but reviews and 
use the library steamreviews to load just reviews.

Note: we can access reviews using the api see usage at end of the file. 
It is just different format/filtering was confusing for me.
"""

from steam import Steam
import steamreviews as sr


from dotenv import load_dotenv

load_dotenv()
import os

# Here is the API KEY implementation.
# This access will be useful for extracting NON-review specifc data.
# In this specific implementation I am searching games with the name dead in it
# This returns a dictionary with name, review count, price, etc.
api_key = os.getenv("STEAM_API_KEY")
steam_key = Steam(api_key)
games = steam_key.apps.search_games("dead")

# print(games)

# Steam Review library implementation.
# one game (Phasmophobia) implementaton (this works)

# sr.download_reviews_for_app_id(739630)
# reviews = sr.load_review_dict(739630)

# 2 game implmentation
game_ids = [739630, 381210]

# let's create a dictionary to filter just steam purchases and english reviews
parameters = {}
parameters["purchase_type"] = "steam"
parameters["language"] = "english"

# call
sr.download_reviews_for_app_id(739630, chosen_request_params=parameters)
sr.download_reviews_for_app_id_batch(game_ids, chosen_request_params=parameters)

r"""
Here is output from the above lines of code for 2 game data processing. 
Not sure what happens when its expected reviews vs num_reviews. 
Need to look at documenation.

Loading idprocessed_on_20231112.txt
Creating idprocessed_on_20231112.txt

##GAME 1 (Phasmophobia)
Downloading reviews for appID = 739630
[appID = 739630] expected #reviews = 272613
[appID = 739630] num_reviews = 9830 (expected: 272613) ### WHY IS THIS HAPPENING
##### There are also A LOT more reviews according to steam website. 
##### It does not appear the param dicitonary is working. 

##GAME 2 (Dead by Daylight)
Downloading reviews for appID = 381210
[appID = 381210] expected #reviews = 186714
Number of queries 150 reached. Cooldown: 310 seconds
Number of queries 150 reached. Cooldown: 310 seconds
Number of queries 150 reached. Cooldown: 310 seconds
Number of queries 150 reached. Cooldown: 310 seconds
Number of queries 150 reached. Cooldown: 310 seconds
Number of queries 150 reached. Cooldown: 310 seconds
Number of queries 150 reached. Cooldown: 310 seconds
Number of queries 150 reached. Cooldown: 310 seconds
Number of queries 150 reached. Cooldown: 310 seconds
Number of queries 150 reached. Cooldown: 310 seconds
Number of queries 150 reached. Cooldown: 310 seconds
[appID = 381210] num_reviews = 165898 (expected: 186714)
Game records written: 2
Traceback (most recent call last):
  File "c:\Users\khsqu\OneDrive\Documents\NLP\NLP_ReviewAnalyzer\get_steam_data.py", line 42, in <module>
    parameters["language"] = "english"
    ^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: cannot unpack non-iterable bool object
r"""
