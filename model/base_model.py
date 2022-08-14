from peewee import *
from utils.db import db
from datetime import date

STATUS_CHOICES = [('A', 'ACTIVO'),
                  ('H', 'HISTORICO')]


class BaseModel(Model):
    status = CharField(unique=True, choices=STATUS_CHOICES)
    creation_date = DateField(default=date.today)

    class Meta:
        database = db
