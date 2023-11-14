"""
In this python script we convert ONE game dictionary into a dataframe and then into a csv.

The json file is a dictionary of dictionary of dictionaries... 

We convert the first dictionaries keys into columns then go into
the second inner dicitionary to make those keys columns as well. 

The output of the csv is every review with any information attached review 
which is scraped in the *get_steam_data.py* 
"""
import json
import pandas as pd
import os

# check your working directory
print("Current Working Directory:", os.getcwd())

# change file path here &&&& JSON file here
# definitly need to DEVOPS this
with open("data/zip_jsons/review_739630.json", "r") as file:
    data = json.load(file)


reviews_data = data.get("reviews", {})
df = pd.DataFrame.from_dict(reviews_data, orient="index")

# get the second inner dictionary as column headers as well
for index, row in df.iterrows():
    # Extract the "author" dictionary
    author_dict = row.get("author", {})

    # iterate over each key in the "author" dictionary
    for key, value in author_dict.items():
        df.at[index, key] = value

# drop the original "author" column
df = df.drop(columns=["author"])

# CHANGE CSV NAME AND OUTPUT
df.to_csv("data/zip_csvs/phas.csv", index=False)
