import os
import pymongo
from dotenv import load_dotenv

# Import environment variables
load_dotenv()

# Connect
def connect():
    conn = pymongo.MongoClient(os.environ.get("PYMONGO_CONN"))
    if conn:
        print('Connection successfull at: ' + os.environ.get("PYMONGO_CONN"))
        print('Databases: ' + str(conn.database_names()))
    else:
        print('Connection refused')