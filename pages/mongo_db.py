from datetime import datetime
import bson
from pymongo import MongoClient

DATABASE_CONNECTION_STRINGS = {
    'phi_db': 'mongodb+srv://stars-gl-core-dev:L0nd7l2NBtLHB4TE@stars-goodlife-phi-core.cyc7g.mongodb.net/stars-gl'
              '-core-dev?retryWrites=true&w=majority',
    'lifemap_db': 'mongodb+srv://stars-lm-dev:YCnKBZhqTcoqLT9C@stars-lifemap-dev.4crou.mongodb.net/stars-lm-dev'
                  '?retryWrites=true&w=majority'
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
}

DATABASE_DATA_TYPES = {
    'ObjectId': bson.objectid.ObjectId,
    'string': str,
    'boolean': bool,
    'date': datetime,
    'int': int,
    'array': list,
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
            print('List of database names: {}'.format(client.list_database_names()))
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
            print('List of collection names: {}'.format(my_db.list_collection_names()))
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
            print('List of collection documents: {}'.format(my_documents))
            return my_documents
        except:
            print('List of collection documents could not be returned')
            raise

    # this method returns a single documents in a provided collection

    @staticmethod
    def return_document(connection_string, db_name, collection_name, record):

        client = Connect.get_connection(connection_string)
        my_db = client[db_name]

        try:
            print('Document found: {}'.format(my_db[collection_name].find_one(record)))
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
                    print('Object found: {}'.format(my_item))
                    return my_item
        except AttributeError:
            print('Object could not be returned')
