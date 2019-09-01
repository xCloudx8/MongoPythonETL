import os
import pymongo
from dotenv import load_dotenv

# Import environment variables
load_dotenv()

# Connect
def connect():
    conn = pymongo.MongoClient(os.environ.get("MONGO_HOST"), int(os.environ.get('MONGO_PORT')))
    if conn:
        print('Connection successfull at: ' + os.environ.get("MONGO_HOST") + ' ' +os.environ.get('MONGO_PORT'))
        print('Available databases: ' + str(conn.database_names()))
    else:
        print('Connection refused')
    
    return conn