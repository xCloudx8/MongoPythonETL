import os
import pymongo as py
from lib import function1
from utils import connectToDb
from utils import alreadyExists
from app import writeToDb, readFromDb
from app.dataStructure import mainStructure
from dotenv import load_dotenv

data = mainStructure.dataStructure()

if (alreadyExists.exists()):
    print("Already exists")
else: 
    writeToDb.writeData(data)
    
res = readFromDb.read()

print(list(res))