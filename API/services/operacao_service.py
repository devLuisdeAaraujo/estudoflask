from API import db
from ..models.operacao_model import Operacao
from ..services import contas_service
from ..models.contas_model import Contas

def cadastrar_operacao(operacao):
    operacao_db = Operacao(nome=operacao.nome,
                                          resumo=operacao.resumo,
                                          custo=operacao.custo,
                                          tipo=operacao.tipo,
                                          conta_id=operacao.conta)
    db.session.add(operacao_db)
    db.session.commit()
    contas_service.alterar_saldo_conta(operacao.conta,operacao,1)
    return operacao_db

def listar_operacao():
    operacao1= Operacao.query.all()
    return operacao1

def listar_operacao_por_id(id):
    return Operacao.query.get(id)

def atualizar_operacao(operacao, operacao_nova):

    valor_antigo = operacao.custo
    operacao.nome = operacao_nova.nome
    operacao.resumo = operacao_nova.resumo
    operacao.custo = operacao_nova.custo
    operacao.tipo = operacao_nova.tipo
    operacao.conta = operacao_nova.conta
    db.session.commit()
    contas_service.alterar_saldo_conta(operacao_nova.conta,operacao_nova,2,valor_antigo)

    return operacao


def excluir(id):
    contas = Operacao.query.get(id)
    if contas is None:
        return None
    db.session.delete(contas)
    db.session.commit()
    contas_service.alterar_saldo_conta(contas.conta_id, contas, 3)

