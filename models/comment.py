from bson import ObjectId

from database.mongodb import MongoConnection


class Comment:
    def __init__(self, text, username, post_id, parent_comment_id=None):
        self.text = text
        self.username = username
        self.post_id = ObjectId(post_id)
        self.parent_comment_id = ObjectId(parent_comment_id) if parent_comment_id else None

    def save(self):
        comment = {
            "text": self.text,
            "username": self.username,
            "post_id": self.post_id,
            "parent_comment_id": self.parent_comment_id
        }
        with MongoConnection() as db:
            db.comments.insert_one(comment)

    @staticmethod
    def find_by_post(post_id):
        with MongoConnection() as db:
            return list(db.comments.find({"post_id": ObjectId(post_id)}, {
                "_id": {"$toString": "$_id"},
                "text": 1,
                "username": 1,
                "post_id": {"$toString": "$post_id"},
                "parent_comment_id": {"$toString": "$parent_comment_id"}

            }))

    @staticmethod
    def find_by_parent_comment(parent_comment_id):
        with MongoConnection() as db:
            return list(db.comments.find(
                {"parent_comment_id": ObjectId(parent_comment_id)}, {
                    "_id": {"$toString": "$_id"},
                    "text": 1,
                    "username": 1,
                    "post_id": {"$toString": "$post_id"},
                    "parent_comment_id": {"$toString": "$parent_comment_id"}
                }))
