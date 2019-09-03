import pymongo
import os
from utils import connectToDb
from dotenv import load_dotenv
from app.dataStructure import mainStructure
load_dotenv()

def exists():
    conn = connectToDb.connectToDb()
    coll = conn[os.environ.get["MONGO_COLLECTION"]]
    structure = mainStructure.dataStructure()
    if coll.find(structure[0][0]):
        print("Already exists")
        return True