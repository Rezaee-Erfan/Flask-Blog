from database.mongodb import MongoConnection


class User:
    def __init__(self, username, first_name, last_name):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name

    def save(self):
        user = {
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name
        }
        with MongoConnection() as db:
            db.users.insert_one(user)

    @staticmethod
    def find_by_username(username):
        with MongoConnection() as db:
            return db.users.find_one({"username": username},
                                     {"_id": {"$toString": "$_id"}, "username": 1, "first_name": 1, "last_name": 1})
