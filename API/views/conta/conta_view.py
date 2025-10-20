from flask_restful import Resource
from API.schemas.conta_schema import ContaSchema
from flask import request, make_response, jsonify
from API.entidades import conta
from API.services import contas_service
from API import api


class ContaList(Resource):
    def post(self):
        cs = ContaSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            resumo = request.json['resumo']
            valor = request.json['valor']
            conta_nova = conta.Conta(nome=nome, resumo=resumo, valor=valor)
            resultado = contas_service.cadastrar_conta(conta_nova)
            return make_response(cs.jsonify(resultado), 200)
    def get(self):
            resultado = contas_service.listar_contas()
            cs = ContaSchema(many=True)
            return make_response(cs.jsonify(resultado), 200)


api.add_resource(ContaList, '/contas')
