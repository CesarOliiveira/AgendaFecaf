from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:toor@localhost/agendafecaf'

##mydb = mysql.connector.connect(
  ##  host='localhost',
   ## user='root',
   ## password='toor',
   ## database='agendafecaf'
##)

db = SQLAlchemy(app)

class usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    email = db.Column(db.String(255))
    senha = db.Column(db.String(255))

    def to_json(self):
        return {"id": self.id, "nome": self.nome, "email": self.email, "senha": self.senha}

    def aut_response(self, code):
        return {"id": self.id, "nome": self.nome, "code": code}

with app.app_context():
    db.create_all()