from pymongo import MongoClient

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

MONGODB_DATABSE = 'feeds'

_client = None


def get_client():
    global _client
    if _client is None:
        _client = MongoClient('mongodb://%s:%d/' % (MONGODB_HOST, MONGODB_PORT))
    return _client
