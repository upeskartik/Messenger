from pymongo import MongoClient
import urllib 

def get_db_handle(db_name, col_info):
    password = 'KRQ1nnG@'
    client = MongoClient("mongodb+srv://kartik:"+urllib.parse.quote(password)+"@cluster0.vqxmk.mongodb.net/"+urllib.parse.quote(db_name)+"?retryWrites=true&w=majority")
    db = client.test
    db_col = db['User']
    return db, db_col


def get_collection_handle(db_handle, collection_name):
    return db_handle[collection_name]