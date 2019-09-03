import pymongo
import json
from utils import connectToDb
from app.dataStructure import mainStructure

def writeData(structure):
    db = connectToDb.connectToDb()
    collection = db.testCollection
    collection.insert(structure)
    print("Wrote data")