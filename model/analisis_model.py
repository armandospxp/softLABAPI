from .base_model import BaseModel
from datetime import date
from peewee import *

from model.determinacion_model import Determinacion
from model.paciente_model import Paciente


class Analisis(BaseModel):
    nombre_analisis = CharField()
    descripcion_analisis = CharField()
    observacones = CharField()
    determinacion = ManyToManyField(Determinacion, backref='analisis')


class PedidoAnalisis(BaseModel):
    analisis = ManyToManyField(Analisis, backref='pedidoanalisis')
    fecha = DateField(default=date.today)
    estado = CharField(max_length=2, default='PE')
    paciente = ForeignKeyField(Paciente, backref='pedidoanalisis')
    numero = IntegerField()
    precio_cobrado = IntegerField()


class Medico(BaseModel):
    nombre_medico = CharField()
    apellido_medico = CharField()
    numero_registro = CharField()


class TipoMuestra(BaseModel):
    nombre_tipo_muestra = CharField()
    descripcion_tipo_muestra = CharField()
