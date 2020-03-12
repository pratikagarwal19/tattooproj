import dns
from pymongo import MongoClient
import datetime

class Connection:

    @staticmethod
    def connect(self):
        client = MongoClient('mongodb+srv://Derek:trek6000@cluster0-6udxg.mongodb.net/test')

        db = client.gettingStarted
        people = db.people
        return people

# personDocument = {
#   "name": { "first": "Khurram", "last": "Khan" },
#   "birth": datetime.datetime(1912, 6, 23),
#   "death": datetime.datetime(1954, 6, 7),
#   "contribs": [ "Turing machine", "Turing test", "Turingery" ],
#   "views": 1250000
# }
#
# people.insert_one(personDocument)