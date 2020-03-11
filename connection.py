import dns
from pymongo import MongoClient
import datetime

client = MongoClient('mongodb+srv://pratik:QeJmJPmFYOliF9Du@cluster0-nxdcn.mongodb.net/test')

db = client.gettingStarted

people = db.people

personDocument = {
  "name": { "first": "Alan", "last": "Turing" },
  "birth": datetime.datetime(1912, 6, 23),
  "death": datetime.datetime(1954, 6, 7),
  "contribs": [ "Turing machine", "Turing test", "Turingery" ],
  "views": 1250000
}

people.insert_one(personDocument)