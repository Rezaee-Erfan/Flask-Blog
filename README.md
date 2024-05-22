# Flask Blog API

This is a simple RESTful API for a blog application built with Flask and Python. The API allows users to create,
retrieve, and interact with blog posts and comments.

## Endpoints

### User Endpoints

- `POST /users`: Create a new user. The request body should include `username`, `first_name`, and `last_name`.

### Post Endpoints

- `POST /posts`: Create a new post. The request body should include `text` and `username`.
- `GET /posts`: Retrieve all posts.
- `GET /users/<username>/posts`: Retrieve all posts by a specific user.

### Comment Endpoints

- `POST /comments`: Create a new comment. The request body should include `text`, `username`, `post_id`, and
  optionally `parent_comment_id`.
- `GET /posts/<post_id>/comments`: Retrieve all comments on a specific post.

## Diagram

![Flask Blog API Diagram](https://github.com/Rezaee-Erfan/Flask-Blog/blob/master/Diagram.png?raw=true)

## Setup and Running

To run this project, you will need Python and Flask installed. Once you have these, you can clone the repository and run
the application:

```bash
git clone https://github.com/Rezaee-Erfan/Flask-Blog.git
cd Flask-Blog
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

The application will be running at `http://localhost:5000`.

## ENV

Put a .env file in the root directory of this project with the following environment variables:

```
MONGO_USERNAME = ""
MONGO_PASSWORD = ""
MONGO_HOST = "localhost"
MONGO_PORT = 27017
```

## License

This project is open source and available under the [MIT License](LICENSE).


