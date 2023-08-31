import pymongo
import os
from urllib import parse

class MongodbClient:
    client = None

    def __init__(self, database_name=os.environ["DATABASE_NAME"]) -> None:
        if MongodbClient.client is None:
            #MongodbClient.client = pymongo.MongoClient(
            #    f"mongodb+srv://{os.environ['ATLAS_CLUSTER_USERNAME']}:{os.environ['ATLAS_CLUSTER_PASSWORD']}@projects.ch4mixt.mongodb.net/?retryWrites=true&w=majority"
            #)
            user = parse.quote_plus("venkataniladibhatla@gmail.com")
            passwd = parse.quote_plus("Priyanka@45")
            MongodbClient.client = pymongo.MongoClient("mongodb://{0}:{1}@projects.ch4mixt.mongodb.net/?retryWrites=true&w=majority".format(user,passwd))
        self.client = MongodbClient.client
        self.database = self.client[database_name]
        self.database_name = database_name
