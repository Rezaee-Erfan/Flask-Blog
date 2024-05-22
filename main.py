from flask import Flask, request, jsonify

from models import User, Post, Comment

app = Flask(__name__)


@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user = User(data['username'], data['first_name'], data['last_name'])
    user.save()
    return jsonify({"message": "User added successfully"}), 201


@app.route('/posts', methods=['POST'])
def add_post():
    data = request.get_json()
    post = Post(data['text'], data['username'])
    post.save()
    return jsonify({"message": "Post added successfully"}), 201


@app.route('/comments', methods=['POST'])
def add_comment():
    data = request.get_json()
    comment = Comment(data['text'], data['username'], data['post_id'], data.get('parent_comment_id'))
    comment.save()
    return jsonify({"message": "Comment added successfully"}), 201


@app.route('/users/<username>/posts', methods=['GET'])
def get_user_posts(username):
    posts = Post.find_by_user(username)
    return jsonify(posts), 200


@app.route('/posts', methods=['GET'])
def get_all_posts():
    posts = Post.find_all()
    return jsonify(posts), 200


@app.route('/posts/<post_id>/comments', methods=['GET'])
def get_post_comments(post_id):
    comments = Comment.find_by_post(post_id)
    return jsonify(comments), 200


if __name__ == '__main__':
    app.run(debug=True)
