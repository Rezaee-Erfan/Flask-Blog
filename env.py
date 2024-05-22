from dataclasses import dataclass
from os import environ

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Env:
    MONGO_HOST = environ.get("MONGO_HOST")
    MONGO_PORT = int(environ.get("MONGO_PORT"))
    MONGO_USERNAME = environ.get("MONGO_USERNAME")
    MONGO_PASSWORD = environ.get("MONGO_PASSWORD")
