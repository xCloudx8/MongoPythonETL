import json
import pymongo
from utils import connectToDb

def read():
    coll = connectToDb.connectToDbColl()
    res = coll.find()
    return res
