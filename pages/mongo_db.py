from datetime import datetime
import bson
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('/Users/radu/Documents/AutomationTemplate/Humana/humana-automation-project/.env')
load_dotenv(dotenv_path=dotenv_path)

DATABASE_CONNECTION_STRINGS = {
    'phi_db_dev': os.getenv('PHI_DB_DEV'),
    'lifemap_db_dev': os.getenv('LIFEMAP_DB_DEV'),
    'phi_db_staging': os.getenv('PHI_DB_STAGING'),
    'lifemap_db_staging': os.getenv('LIFEMAP_DB_STAGING')

}

DATABASE_KEYS = {
    '_id': '_id',
    'memberPersonalGeneratedKey': 'memberPersonalGeneratedKey',
    'token': 'token',
    'emailToken': 'emailToken',
    'synced': 'synced',
    'createdAt': 'createdAt',
    'updatedAt': 'updatedAt',
    '__v': '__v',
    'exportUpdatedAt': 'exportUpdatedAt',
    'userTracks': 'userTracks',
    'userId': 'userId',
    'lastName': 'lastName',
    'firstName': 'firstName',
    'cardId': 'cardId',
    'addressLine1': 'addressLine1',
    'addressLine2': 'addressLine2',
    'cityName': 'cityName',
    'stateCode': 'stateCode',
    'zipCode': 'zipCode',
    'birthDate': 'birthDate',
    'phoneNumber': 'phoneNumber',
    'customerId': 'customerId',
    'languageSpokenCode': 'languageSpokenCode',
    'sexCode': 'sexCode',
    'email': 'email',
    'group': 'group',
    'smoker': 'smoker',
    'trackId': 'trackId',
    'trackName': 'trackName'
}

DATABASE_DATA_TYPES = {
    'ObjectId': bson.objectid.ObjectId,
    'string': str,
    'boolean': bool,
    'date': datetime,
    'int': int,
    'array': list,
}

DATABASE_TRACK_IDS = {
    'track 1': '0001'
}


class Connect:

    # this method connects to a MongoDB instance

    @staticmethod
    def get_connection(connection_string):
        return MongoClient(connection_string)

    # this method returns a list of database names in a provided connection

    @staticmethod
    def get_database_names(connection_string):

        client = Connect.get_connection(connection_string)
        try:
            return client.list_database_names()
        except:
            print('List of database names could not be returned')
            raise

    # this method returns a list of collections name in a provided db

    @staticmethod
    def get_collection_names(connection_string, db_name):

        client = Connect.get_connection(connection_string)
        my_db = client[db_name]

        try:
            return my_db.list_collection_names()
        except:
            print('List of collection names could not be returned')
            raise

    # this method returns a list of all documents in a provided collection

    @staticmethod
    def return_documents(connection_string, db_name, collection_name):

        client = Connect.get_connection(connection_string)
        my_db = client[db_name]
        my_collection = my_db[collection_name].find({})

        my_documents = []

        try:
            for doc in my_collection:
                my_documents.append(doc)
            return my_documents
        except:
            print('List of collection documents could not be returned')
            raise

    # this method returns a single document in a provided collection

    @staticmethod
    def return_document(connection_string, db_name, collection_name, record):

        client = Connect.get_connection(connection_string)
        my_db = client[db_name]

        try:
            return my_db[collection_name].find_one(record)
        except:
            print('Document could not be returned')
            raise

    # this method returns an object from the db based on a given unique key/value pair

    @staticmethod
    def return_object(connection_string, db_name, collection_name, key, unique_value):
        list_of_objects = Connect.return_documents(connection_string, db_name, collection_name)
        try:
            for item in list_of_objects:
                if item[key] == unique_value:
                    my_item = item
                    return my_item
        except AttributeError:
            print('Object could not be returned')

    # this method returns all objects from the db based on a given unique key/value pair

    @staticmethod
    def return_objects(connection_string, db_name, collection_name, key, unique_value):
        list_of_objects = Connect.return_documents(connection_string, db_name, collection_name)
        objects = []
        try:
            for item in list_of_objects:
                if item[key] == unique_value:
                    objects.append(item)
            return objects
        except AttributeError:
            print('Objects could not be returned')
