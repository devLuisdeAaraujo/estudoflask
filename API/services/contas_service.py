from API import db
from ..entidades import operacao
from ..models.contas_model import  Contas

def listar_contas():
    contas = Contas.query.all()
    return contas

def cadastrar_conta(conta):
    conta_db = Contas(nome=conta.nome,resumo=conta.resumo,valor = conta.valor)
    db.session.add(conta_db)
    db.session.commit()
    return conta_db

def mostrar_contas_por_id(id):
    return Contas.query.get(id)

def excluir(id):
    conta = Contas.query.get(id)
    db.session.delete(conta)
    db.session.commit()
    return conta

def atualizar_conta(id, conta_nova):
    conta = Contas.query.get
    if conta is None:
        return None
    conta.nome = conta_nova.nome
    conta.resumo = conta_nova.resumo
    conta.valor = conta_nova.valor
    db.session.commit()

    return conta
def alterar_saldo_conta(conta_id, operacao, tipo_funcao, valor_antigo = None
                        ):
        conta = mostrar_contas_por_id(conta_id)

        if tipo_funcao == 1:
            if operacao.tipo == 'entrada':
                conta.valor += operacao.custo
            else:
                conta.valor -= operacao.custo

        elif tipo_funcao == 2:
            if operacao.tipo == 'entrada':
                conta.valor -= valor_antigo
                conta.valor += operacao.custo
            else:
                conta.valor += valor_antigo
                conta.valor -= operacao.custo

        else:
            if operacao.tipo == 'entrada':
                conta.valor -= operacao.custo
            else:
                conta.valor += operacao.custo

        db.session.commit()
