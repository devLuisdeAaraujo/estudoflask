from flask_restful import Resource
from ...schemas.operacao_schema import  OperacaoSchema
from flask import request,jsonify,make_response
from ...entidades.operacao import Operacao
from API import api
from ...services.contas_service import mostrar_contas_por_id
from ...services.operacao_service import atualizar_operacao,listar_operacao_por_id

class AtualizarOperacao(Resource):
    def put(self,id):
        operacao_db = listar_operacao_por_id(id)
        if operacao_db is None:
            return make_response(jsonify({'erro': 'Operacao não encontrada'}), 404)
        os = OperacaoSchema()
        validate = os.validate(request.json)
        if validate:
            return make_response(jsonify(validate),400)
        else:
            nome = request.json['nome']
            resumo = request.json['resumo']
            custo = request.json['custo']
            tipo = request.json['tipo']
            conta = request.json['conta_id']



            operacao_nova = Operacao(nome=nome,
                                     resumo=resumo,
                                     custo=custo,
                                     tipo=tipo,
                                        conta=  conta)
            resultado = atualizar_operacao(operacao_db,operacao_nova)
            return  make_response(os.dump(resultado),200)


api.add_resource(AtualizarOperacao,'/atualizar_operacao/<int:id>')

