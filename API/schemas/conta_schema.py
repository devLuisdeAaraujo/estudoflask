from API import ma
from ..models.contas_model import  Contas
from marshmallow import fields

class ContaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Contas
        load_instance = True

        nome = fields.String(required=True)
        resumo = fields.String(required=True)
        valor = fields.Float(required=True)