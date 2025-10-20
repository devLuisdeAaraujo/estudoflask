from flask_restful import Resource
from ...schemas.operacao_schema import  OperacaoSchema
from flask import request,jsonify,make_response
from ...entidades.operacao import Operacao
from API import api
from ...services.operacao_service import excluir,listar_operacao_por_id

class ExcluirOperacao(Resource):
    def delete(self, id):
        operacao = excluir(id)
        if operacao is None:
            return make_response(jsonify({'erro': 'Operacao não encontrada'}), 404)

        cs = OperacaoSchema()
        return make_response(jsonify(cs.dump(operacao)), 200)


api.add_resource(ExcluirOperacao,'/excluir_operacao/<int:id>')