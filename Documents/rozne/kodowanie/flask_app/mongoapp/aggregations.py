import os
import datetime
from pprint import pprint
import sys
import bson
from dotenv import load_dotenv
import pymongo

# Load config from a .env file:
load_dotenv(verbose=True)
MONGODB_URI = 'conncetionstring'

# Connect to your MongoDB cluster:
client = pymongo.MongoClient(MONGODB_URI)

# List all the databases in the cluster:
for db_info in client.list_database_names():
    print(db_info)

# Get a reference to the "sample_mflix" database:
db = client["sample_mflix"]

# Get a reference to the "movies" collection:
confs_collection = db["movies"]

#################################
pipeline_requests = [
    {
        "$match": {
            "title": "A Star Is Born"
        }
    },
    {
        "$sort": {
            "year": pymongo.ASCENDING
        }
    },
]
requests = confs_collection.aggregate(pipeline_requests)
for movie in requests:
    print(" * {title}, {first_castmember}, {year}".format(
          title=movie["title"],
          first_castmember=movie["cast"][0],
          year=movie["year"],
          ))


pipeline_users = [
    {
        "$match": {
            "title": "A Star Is Born"
        }
    },
    {
        "$sort": {
            "year": pymongo.ASCENDING
        }
    },
]
users = confs_collection.aggregate(pipeline_users)
for movie in users:
    print(" * {title}, {first_castmember}, {year}".format(
          title=movie["title"],
          first_castmember=movie["cast"][0],
          year=movie["year"],
          ))

pipeline_systems = [
    {
        "$match": {
            "title": "A Star Is Born"
        }
    },
    {
        "$sort": {
            "year": pymongo.ASCENDING
        }
    },
]
systems = confs_collection.aggregate(pipeline_systems)
for movie in systems:
    print(" * {title}, {first_castmember}, {year}".format(
          title=movie["title"],
          first_castmember=movie["cast"][0],
          year=movie["year"],
          ))
