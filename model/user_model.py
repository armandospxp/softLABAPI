from .base_model import BaseModel
from peewee import *


class User(BaseModel):
    email = CharField(unique=True)
    username = CharField(unique=True)
    password = CharField()
