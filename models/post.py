from database.mongodb import MongoConnection


class Post:
    def __init__(self, text, username):
        self.text = text
        self.username = username

    def save(self):
        post = {
            "text": self.text,
            "username": self.username
        }
        with MongoConnection() as db:
            db.posts.insert_one(post)

    @staticmethod
    def find_by_user(username):
        with MongoConnection() as db:
            return list(db.posts.find({"username": username}, {"_id": {"$toString": "$_id"}, "username": 1, "text": 1}))

    @staticmethod
    def find_all():
        with MongoConnection() as db:
            return list(db.posts.find({}, {"_id": {"$toString": "$_id"}, "username": 1, "text": 1}))
