import pymongo
import os
from utils import connectToDb
from dotenv import load_dotenv
from app.dataStructure import mainStructure
load_dotenv()

def exists():
    conn = connectToDb.connectToDbColl()
    structure = mainStructure.dataStructure()
    res = conn.find({'_id' : structure['_id']})

    if list(res) != []:
        return True