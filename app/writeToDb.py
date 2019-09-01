import pymongo
import json
from utils import connectToDb
from app.dataStructure import mainStructure

structure = mainStructure.dataStructure()

exit(0)
for i in structure.values():
    print(i['__id'])

exit(0)

def writeData():
    db = connectToDb.connectToDb()
    collection = db.testCollection
    collection.insert(structure)