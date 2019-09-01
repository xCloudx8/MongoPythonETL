from lib import function1
import os
from dotenv import load_dotenv
import pymongo as py

#Load environment varibles
load_dotenv()

a = os.environ.get("TEST_ENV")
print(a)
