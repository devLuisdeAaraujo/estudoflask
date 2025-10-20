from API import ma
from ..models.operacao_model import Operacao
from marshmallow import fields

class OperacaoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Operacao
        load_instance = True  # permite desserializar direto em instâncias
        include_fk = True

    nome = fields.String(required=True)
    resumo = fields.String(required=True)
    custo = fields.Float(required=True)
    tipo = fields.String(required=True)
    conta_id  = fields.Integer(required =True)
