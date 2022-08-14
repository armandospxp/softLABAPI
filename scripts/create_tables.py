from model.analisis_model import Analisis, PedidoAnalisis, Medico, TipoMuestra
from model.determinacion_model import UnidadMedida, Determinacion, Metodo
from model.paciente_model import Paciente
from model.resultado_model import Resultado, ResultadoDeterminacion
from model.user_model import User
from utils.db import db


def create_tables():
    with db:
        db.create_tables([Analisis, PedidoAnalisis, Medico, TipoMuestra, UnidadMedida, Determinacion, Metodo,\
                          Paciente, Resultado, ResultadoDeterminacion, User])
