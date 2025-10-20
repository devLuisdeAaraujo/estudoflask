from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

from flask_restful import Api
app = Flask(__name__)


app.config.from_object('configurate')

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
api = Api(app)



from .models.contas_model import  Contas
from API.views.conta.conta_view import  ContaList
from API.views.conta.conta_por_id import  MostrarContaPorId
from API.views.conta.delete_id import DeleteContas
from API.views.conta.atualizar_conta import AtualizarConta
from .models.operacao_model import  Operacao
if __name__ == '__main__':
    app.run(debug=True)
