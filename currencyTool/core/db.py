from pymongo import MongoClient

# DbClient Class - serve as a wrapper around pymongo pkg functions and provide a simpler set of functions
class DbClient:
    def __init__(self, db_name, default_collection):
        self._db_name = db_name
        self._default_collection = default_collection
        self._db = None

    def connect(self):
        self._client = MongoClient('mongodb://127.0.0.1:27017/')
        self._db = self._client.get_database(self._db_name)

    def disconnect(self):
        self._client.close()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exec_type, exec_value, traceback):
        self.disconnect()

        if exec_type:
            raise exec_type(exec_value)

        return self

    def _get_collection(self):
        if self._default_collection is None:
            raise AttributeError('collection argument is required')

        return self._db[self._default_collection]

    # filter refers to a criterion that will be used to search the collection's item that we want to update
    def find_one(self, filter=None):
        collection = self._get_collection()
        return collection.find_one(filter)

    # document is a dictionary with the fields that we want to update in the collection's item or insert
    # upsert means that if the item that we are trying to update doesn't exit in db's collection, we are going to
    # perform an insert operation and add item to the collection
    def update(self, filter, document, upsert=True):
        collection = self._get_collection()

        collection.find_one_and_update(filter, {'$set': document}, upsert=upsert)
