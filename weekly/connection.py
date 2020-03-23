import dns
from pymongo import MongoClient


class Connection:

    @staticmethod
    def connect(db_name):
        client = MongoClient('mongodb+srv://Derek:trek6000@cluster0-6udxg.mongodb.net/test')
        db = client[db_name]

        return db
