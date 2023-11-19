from RyuzakiLib.db.pymongo import MongoConnect


def update_user(mongo_url, client_db, database, dict_list, set_name_db):
    conn = MongoConnect(mongo_url, client=client_db, database=database)
    collection = conn.get_collection()
    filter_query = {"key": dict_list["key"]}
    update_query = {"$set": {set_name_db: dict_list}}
    return collection.update_one(filter_query, update_query, upsert=True)
