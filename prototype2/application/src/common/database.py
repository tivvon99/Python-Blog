__author__ = 'Tivvon'

import pymongo


class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    # insert one document into db
    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert_one(data)
    
    # added delete function for mongo db
    @staticmethod
    def delete(collection, data):
        Database.DATABASE[collection].delete_one(data)

    # finds all
    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    # finds one
    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
    
    
    @staticmethod
    def count_users():
        pass
