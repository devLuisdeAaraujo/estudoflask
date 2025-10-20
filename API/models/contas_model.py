from API import db

class Contas(db.Model):
    __tablename__ = 'contas'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    resumo = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.Float, nullable=False)








