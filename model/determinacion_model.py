from .base_model import BaseModel
from peewee import *


class UnidadMedida(BaseModel):
    nombre_unidad = CharField()
    abreviacion_unidad = CharField()


class Determinacion(BaseModel):
    nombre_determinacion = CharField()
    descripcion_determinacion = CharField()
    limite_inferior = IntegerField()
    limite_superior = IntegerField()
    valor_referencia = CharField()
    unidad_medida = ForeignKeyField(UnidadMedida, backref='determinacion')


class Metodo(BaseModel):
    nombre_metodo = CharField()
