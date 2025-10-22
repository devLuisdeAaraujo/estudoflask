from API import ma
from ..models.contas_model import  Contas
from marshmallow import fields
from ..schemas import operacao_schema

class ContaSchema(ma.SQLAlchemyAutoSchema):
    operacoes = ma.Nested(operacao_schema.OperacaoSchema,many=True)
    class Meta:
        model = Contas
        load_instance = True

        nome = fields.String(required=True)
        resumo = fields.String(required=True)
        valor = fields.Float(required=True)