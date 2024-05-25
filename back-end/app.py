
from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:toor@localhost/agendafecaf'

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




#Selecionar todos os usuarios
@app.route("/", methods=['GET'])
def getAllUsers():
    getUser = usuario.query.all()
    getUser_json = [usuario.to_json() for usuario in getUser]

    return gera_response(200, "usuarios", getUser_json)

@app.route("/usuario/<id>")
def getOneUser(id):
    user_object = usuario.query.filter_by(id=id).first()
    user_json = user_object.to_json()

    return gera_response(200, "usuario", user_json, "User Found")


@app.route("/authentic", methods=['POST'])
def authenticUser():
    body = request.get_json()
    user_object = usuario.query.filter_by(id=body["id"], senha=body["senha"]).first()


    if user_object:
        userResponse_json = user_object.to_json()
        if body["id"] == userResponse_json["id"] and body["senha"] == userResponse_json["senha"]:
            user_json = user_object.aut_response(1)
            return gera_response(200, "Authenticate", user_json, "Usuario encontrado")

    elif user_object == None:
        content = {"code": 0}
        return gera_response(404, "Authenticate", content, "Usuario ou Senha não encontrado.")






##DTO

def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if(mensagem):
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")

def authentic_response(conteudo, code):
   return {"id": conteudo.id, "email": conteudo.senha, "code": code}