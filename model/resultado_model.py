from .base_model import BaseModel
from model.analisis_model import PedidoAnalisis
from model.determinacion_model import Determinacion
from peewee import *

ESTADO_RESULTADO_CHOICES = [('PE', 'PE'), ('IN', 'INCOMPLETO'),
                            ('CO', 'COMPLETO'), ('VA', 'VALIDADO'),
                            ('IM', 'IMPRESO')]


class Resultado(BaseModel):
    pedido = ForeignKeyField(PedidoAnalisis, backref='resultado_determinacion')
    estado_resultado = CharField(choices=ESTADO_RESULTADO_CHOICES)


class ResultadoDeterminacion(BaseModel):
    valor = CharField()
    determinacion = ForeignKeyField(Determinacion, backref='resultado_determinacion')
    resultado = ForeignKeyField(Resultado, backref='resultado_determinacion')
