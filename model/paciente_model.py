from .base_model import BaseModel
from peewee import *


class Paciente(BaseModel):
    documento = CharField(unique=True)
    nombre_paciente = CharField()
    apellido_paciente = CharField()
    direccion_paciente = CharField()
    telefono_paciente = CharField()
    correo_paciente = CharField()
