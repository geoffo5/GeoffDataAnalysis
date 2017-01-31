import pymongo

def addToDatabase(file, id):
    client = pymongo.MongoClient()
    db = client['DataAnalysis']
    coll = db['files']
    coll.insert({ '_id' : id, 'file' : file })
    
def checkFileExists(id):
    client = pymongo.MongoClient()
    db = client['DataAnalysis']
    coll = db['files']
    file = coll.find_one({'_id': ObjectId(id)})