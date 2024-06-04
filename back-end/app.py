
from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:toor@localhost/agendafecaf'

db = SQLAlchemy(app)


class usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255))
    email = db.Column(db.String(255))
    senha = db.Column(db.String(255))

    def to_json(self):
        return {"id": self.id, "nome": self.nome, "email": self.email, "senha": self.senha}

    def aut_response(self, code):
        return {"id": self.id, "nome": self.nome, "code": code}

class agendamento(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    professor = db.Column(db.String(255))
    materia = db.Column(db.String(255))
    laboratorio = db.Column(db.String(255))
    data = db.Column(db.String(255))

    def to_json(self):
        return {"id": self.id, "professor": self.professor, "materia": self.materia, "laboratorio": self.laboratorio, "data": self.data}

    def response(self, code):
        return {"id": self.id, "professor": self.professor, "materia": self.materia, "laboratorio": self.laboratorio, "data": self.data, "code": code}

with app.app_context():
    db.create_all()


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

@app.route("/agendamento", methods=['POST'])
def agendar():
    body = request.get_json()

    try:
        bodyRequest = agendamento(professor=body["professor"], materia=body["materia"],
                                  laboratorio=body["laboratorio"], data=body["data"])
        db.session.add(bodyRequest)
        db.session.commit()
        return gera_response(201, "Agendamento", bodyRequest.response(code=1), "Agendamento Cadastrado.")
    except Exception as e:
        print(e)
        return gera_response(400, "", {}, "Erro ao cadastrar")

@app.route("/agendamento", methods=['GET'])
def pegarAgendamento():
    getAgendamento = agendamento.query.all()
    getAgendamento_json = [agendamento.to_json() for agendamento in getAgendamento]

    return gera_response(200, "Agendamento", getAgendamento_json)

##DTO
def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if(mensagem):
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")

def authentic_response(conteudo, code):
   return {"id": conteudo.id, "email": conteudo.senha, "code": code}