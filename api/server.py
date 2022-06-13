from flask import Flask, jsonify, redirect, request
from flasgger import Swagger
from flasgger.utils import swag_from
import pyrebase
import requests
import json
import logging

app = Flask(__name__)
app.config["SWAGGER"] = {"title": "Swagger-UI", "uiversion": 2}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec_1",
            "route": "/apispec_1.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/swagger/",
}

swagger = Swagger(app, config=swagger_config)

###### FIREBASE CONFIG ######

database = "https://cloudopss-4ce94-default-rtdb.firebaseio.com/"

firebaseConfig = {
    "apiKey": "AIzaSyCGxm4_igTOoxZVVNHfAPhhBDaCuEflWnQ",
    "authDomain": "cloudopss-4ce94.firebaseapp.com",
    "databaseURL": "https://cloudopss-4ce94-default-rtdb.firebaseio.com",
    "projectId": "cloudopss-4ce94",
    "storageBucket": "cloudopss-4ce94.appspot.com",
    "messagingSenderId": "573024716405",
    "appId": "1:573024716405:web:2150925b56d46b66621a3c"
}

firebase_storage = pyrebase.initialize_app(firebaseConfig)
storage = firebase_storage.storage()

##############################

log_format = '%(asctime)s: %(levelname)s: %(filename)s: %(message)s'

logging.basicConfig(filename='log_file.log',
                    # w -> sobrescreve o arquivo a cada log
                    # a -> não sobrescreve o arquivo
                    filemode='a',
                    level=logging.DEBUG,
                    format=log_format)

logger = logging.getLogger('root')


@swag_from("swagger_config.yml")
@app.route("/clientes")
def clientes():
    clientes = []
    requisicao = requests.get(f'{database}/Clientes/.json')
    dic_requisicao = requisicao.json()

    for ids in dic_requisicao:
        cliente = dic_requisicao[ids]['nome']
        clientes.append(cliente)

    return {'clientes': clientes}


@swag_from("swagger_config.yml")
@app.route("/enviar", methods=["POST"])
def enviar():
    nome = request.form.get('nome')
    telefone = request.form.get('telefone')
    email = request.form.get('email')
    endereco = request.form.get('endereco')
    profissao = request.form.get('profissao')
    file = request.files['file']
    storage.child(f'curriculos/{file.filename}').put(file)

    dados = {'nome': nome, 'telefone': telefone, 'email': email,
             'endereco': endereco, 'profissao': profissao, 'curriculo': file.filename}

    requisicao = requests.post(
        f'{database}/Clientes/.json', data=json.dumps(dados))

    return redirect('/clientes')


@swag_from("swagger_config.yml")
@app.route("/deletar", methods=['POST'])
def deletar():
    cliente = request.form.get('cliente')
    requisicao = requests.get(f'{database}Clientes/.json')
    dic_requisicao = requisicao.json()
    for ids in dic_requisicao:
        nome_cliente = dic_requisicao[ids]['nome']
        if nome_cliente == cliente:
            id_cliente = ids
            curriculo = dic_requisicao[id_cliente]['curriculo']
            storage.delete(f'curriculos/{curriculo}', None)
            requests.delete(f'{database}Clientes/{id_cliente}/.json')
    return redirect('/clientes')


if __name__ == '__main__':
    app.run(debug=True)
