import pymongo
import json

def addToDatabase(file, id):
    client = pymongo.MongoClient()
    db = client['DataAnalysis']
    coll = db['files']
    coll.insert ({'_id': id, 'basic':file}, check_keys=False)
    
def checkFileExists(id):
    client = pymongo.MongoClient()
    db = client['DataAnalysis']
    coll = db['files']
    file = coll.find_one({'_id': id})
    if file:
        return True
    else: 
        return False

def retrieveFile(id):
    client = pymongo.MongoClient()
    db = client['DataAnalysis']
    coll = db['files']
    file = coll.find_one({'_id':id})
    return file

def updateDatabase(file, id):
    client = pymongo.MongoClient()
    db = client['DataAnalysis']
    coll = db['files']
    coll.update({'_id':id}, {'$set':{'advanced': file}})
    
    
    