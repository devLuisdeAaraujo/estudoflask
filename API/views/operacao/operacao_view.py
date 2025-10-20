from flask_restful import Resource
from ...schemas.operacao_schema import  OperacaoSchema
from flask import request,jsonify,make_response
from ...entidades.operacao import Operacao
from API import api
from ...services.contas_service import mostrar_contas_por_id
from ...services.operacao_service import cadastrar_operacao,listar_operacao

class OperacaoList(Resource):
    def post(self):
        os = OperacaoSchema()
        validate = os.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            resumo = request.json['resumo']
            custo = request.json['custo']
            tipo = request.json['tipo']
            conta= request.json['conta_id']

            operacao_nova = Operacao(nome=nome,
                                     resumo=resumo,
                                     custo=custo,
                                     tipo=tipo,
                                     conta = conta)
            if mostrar_contas_por_id(conta) is None:
                return make_response({'erro':'conta nao existe'},404)
            else:
                resultado = cadastrar_operacao(operacao_nova)
                return make_response(os.jsonify(resultado), 201)

    def get(self):
        os = OperacaoSchema(many=True)
        operacao_ = listar_operacao()
        return make_response(os.jsonify(operacao_), 200)


api.add_resource(OperacaoList, '/operacao')