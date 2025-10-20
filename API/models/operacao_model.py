import enum

from API import db

class TipoEnum(enum.Enum):
    entrada = 1
    saida = 2

class Operacao(db.Model):
    __tablename__ = 'operacao'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True,nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    resumo = db.Column(db.String(50), nullable=False)
    custo = db.Column(db.String(50),nullable=False)
    tipo = db.Column(db.Enum(TipoEnum),nullable=False)
    conta_id = db.Column(db.Integer, db.ForeignKey("contas.id"))

