from pymongo import MongoClient

from env import Env


class MongoConnection:
    def __init__(self):
        self.__client = MongoClient(
            Env.MONGO_HOST,
            Env.MONGO_PORT,
            username=Env.MONGO_USERNAME,
            password=Env.MONGO_PASSWORD
        )
        self.__db = self.__client['social_media']
        self.users = self.__db['users']
        self.posts = self.__db['posts']
        self.comments = self.__db['comments']

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__client.close()
