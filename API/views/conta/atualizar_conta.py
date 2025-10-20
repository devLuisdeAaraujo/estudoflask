from API.entidades.conta import Conta
from API.services import contas_service
from flask_restful import Resource
from API.schemas.conta_schema import ContaSchema
from flask import make_response, jsonify, request
from API import api


class AtualizarConta(Resource):
    def put(self, id):

        conta_db = contas_service.mostrar_contas_por_id(id)
        if conta_db is None:
            return make_response(jsonify({'erro': 'Conta não encontrada'}), 404)

        cs = ContaSchema()
        erros = cs.validate(request.json)
        if erros:
            return make_response(jsonify(erros), 400)

        nome = request.json['nome']
        resumo = request.json['resumo']
        valor = request.json['valor']

        conta_nova = Conta(nome=nome, resumo=resumo, valor=valor)
        resultado = contas_service.atualizar_conta(id, conta_nova)

        return make_response(jsonify(cs.dump(resultado)), 200)


api.add_resource(AtualizarConta, '/atualizar_conta/<int:id>')
