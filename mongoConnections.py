from pymongo import MongoClient

client = MongoClient()

db = client.lotr_quotes.dialogue

def insert(data):

    res = db.insert_one(data)
    return res.inserted_id


def read(query, project=None):
    data = db.find(query, project)
    return list(data)