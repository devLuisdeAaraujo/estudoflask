from flask_restful import Resource
from ...schemas.operacao_schema import  OperacaoSchema
from flask import request,jsonify,make_response
from ...entidades.operacao import Operacao
from API import api
from ...services.operacao_service import listar_operacao_por_id

class OperaracaoPorId(Resource):
    def get(self,id):
        operacao = listar_operacao_por_id(id)
        cs = OperacaoSchema()
        if operacao is None:
            return make_response(jsonify({'erro':'nao foi possivel achar esse id'}),404)
        else:
            return make_response(jsonify(cs.dump(operacao)),200)

api.add_resource(OperaracaoPorId,'/operacao_por_id/<int:id>')