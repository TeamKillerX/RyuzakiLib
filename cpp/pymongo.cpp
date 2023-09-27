#include <iostream>
#include <mongocxx/client.hpp>
#include <mongocxx/instance.hpp>
#include <mongocxx/uri.hpp>

class MongoConnect {
public:
    MongoConnect(std::string mongo_url = "", std::string client = "", std::string database = "", bool mongodb_connect = false)
        : mongo_url(mongo_url), client(client), database(database), mongodb_connect(mongodb_connect) {}

    mongocxx::collection get_collection() {
        if (mongodb_connect) {
            mongocxx::uri uri(mongo_url);
            mongocxx::client client(uri);
            mongocxx::database db = client[client];
            mongocxx::collection collection = db[database];
            return collection;
        } else {
            mongocxx::uri uri(mongo_url);
            mongocxx::client client(uri);
            mongocxx::database db = client["tiktokbot"];
            mongocxx::collection collection = db["ryuzakilib"];
            return collection;
        }
    }

private:
    std::string mongo_url;
    std::string client;
    std::string database;
    bool mongodb_connect;
};
