from lib import function1
from app import writeToDb
from utils import connectToDb
from app.dataStructure import mainStructure
import os
from dotenv import load_dotenv
import pymongo as py

connection = connectToDb.connect()
data = mainStructure.dataStructure()

writeToDb.writeData(data)
#collection.insert_one(dataExample)
