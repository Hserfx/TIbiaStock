import pymongo
from dotenv import dotenv_values

config = dotenv_values('.env')

class MongoTibiaDB(object):
    URI = config['CONNECTION_STRING'] + 'market'
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(MongoTibiaDB.URI, tls=True,  tlsAllowInvalidCertificates=True)
        MongoTibiaDB.DATABASE = client['market']
        return client
    
    @staticmethod
    def insert(collection, data):
        MongoTibiaDB.DATABASE[collection].insert_one(data)

    @staticmethod
    def find(collection, query, **kwargs):
        return MongoTibiaDB.DATABASE[collection].find(query, **kwargs)
    
    @staticmethod
    def find_one(collection, query, **kwargs):
        return MongoTibiaDB.DATABASE[collection].find_one(query, **kwargs)

    @staticmethod
    def get_indexes(collection):
        return MongoTibiaDB.DATABASE[collection].getIndexes()