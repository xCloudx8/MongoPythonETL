import os
import pymongo
from dotenv import load_dotenv

# Import environment variables
load_dotenv()

# Connect
def connectWithPrint():
    conn = pymongo.MongoClient(os.environ.get("MONGO_HOST"), int(os.environ.get('MONGO_PORT')))
    if conn:
        print('Connection successfull at: ' + os.environ.get("MONGO_HOST") + ' ' +os.environ.get('MONGO_PORT'))
    else:
        print('Connection refused')
    
    return conn

def connect():
    conn = pymongo.MongoClient(os.environ.get("MONGO_HOST"), int(os.environ.get('MONGO_PORT')))
    return conn

def connectToDb():
    conn = connect()
    db = conn.testDb
    return db

def connectToDbColl():
    db = connectToDb()
    coll = db.testCollection
    return coll