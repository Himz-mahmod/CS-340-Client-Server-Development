"""
CS 340 - Project One
AnimalShelter CRUD Python Module
Author: Tanvir Mahmod
"""

from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """CRUD operations for the Austin Animal Center (AAC) 'animals' collection
    in MongoDB."""

    def __init__(self, username, password):
        USER = username
        PASS = password
        HOST = '127.0.0.1'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'

        try:
            self.client = MongoClient(
                'mongodb://%s:%s@%s:%d/?authSource=aac&directConnection=true' % (USER, PASS, HOST, PORT),
                serverSelectionTimeoutMS=5000
            )
            self.client.admin.command('ping')
            self.database = self.client['%s' % DB]
            self.collection = self.database['%s' % COL]
        except Exception as e:
            raise Exception(f"Unable to connect to MongoDB: {e}")

    def create(self, data):
        if data is not None and isinstance(data, dict) and len(data) > 0:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print(f"Error inserting document: {e}")
                return False
        else:
            raise ValueError("Data parameter must be a non-empty dictionary")

    def read(self, query):
        if query is not None and isinstance(query, dict):
            try:
                cursor = self.collection.find(query)
                return list(cursor)
            except Exception as e:
                print(f"Error reading documents: {e}")
                return []
        else:
            raise ValueError("Query parameter must be a dictionary")

    def update(self, query, update_data, many=False):
        if query is not None and isinstance(query, dict):
            try:
                if many:
                    result = self.collection.update_many(query, update_data)
                else:
                    result = self.collection.update_one(query, update_data)
                return result.modified_count
            except Exception as e:
                print(f"Error updating document(s): {e}")
                return 0
        else:
            raise ValueError("Query parameter must be a dictionary")

    def delete(self, query, many=False):
        if query is not None and isinstance(query, dict):
            try:
                if many:
                    result = self.collection.delete_many(query)
                else:
                    result = self.collection.delete_one(query)
                return result.deleted_count
            except Exception as e:
                print(f"Error deleting document(s): {e}")
                return 0
        else:
            raise ValueError("Query parameter must be a dictionary")