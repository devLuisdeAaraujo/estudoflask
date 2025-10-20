from API.services import contas_service
from flask_restful import Resource
from API.schemas.conta_schema import ContaSchema
from flask import make_response, jsonify
from API import api


class DeleteContas(Resource):
    def delete(self, id):
        conta = contas_service.excluir(id)
        if conta is None:
            return make_response(jsonify({'erro': 'Conta não encontrada'}), 404)

        cs = ContaSchema()
        return make_response(jsonify(cs.dump(conta)), 200)


api.add_resource(DeleteContas, '/delete/<int:id>')
