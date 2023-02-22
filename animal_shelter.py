from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,username,password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:29948/?authMechanism=DEFAULT&authSource=AAC' % (username, password))
        
        # where xxxx is your unique port number
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data): # TODO add check for existing entry
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary   
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read_all(self, data):
        cursor = self.database.animals.find(data, {'_id':False}) ## return a cursor which a pointer to a list of results
        return cursor
    
    def read(self, data):
        return self.database.animals.find_one(data) ## returns only one document as a python dictionary
 
 
# Create method to implement the U in CRUD.
    def update_many(self, query, update):
        if query is not None:
            self.database.animals.update_many(query, update)
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
    def update_one(self, query, update):
        if query is not None:
            self.database.animals.update_one(query, update)
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")     
            
# Create method to implement the D in CRUD
    def delete(self, data):
        if data is not None:
            self.database.animals.remove(data)
            return True
        else:
            raise Exception("Nothing to delete, because data parameter is empty")

            
            
       