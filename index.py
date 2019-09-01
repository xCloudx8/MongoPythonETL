from lib import function1
from utils import connectToDb
import os
from dotenv import load_dotenv
import pymongo as py

connection = connectToDb.connect()

db = connection.testDatabase
collection = db.testCollection

dataExample = {
    "Name": "Nome",
    "Surname": "Cognome"
}

collection.insert_one(dataExample)

cursor = collection.find()
for record in cursor:
    print(record)
