from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

alunos = [
    {"id": 1, "nome": "João", "idade": 20},
    {"id": 2, "nome": "Maria", "idade": 21},
    {"id": 3, "nome": "José", "idade": 22},
    {"id": 4, "nome": "Ana", "idade": 23},
]

class Alunos(Resource):
    def get(self, id=None):
        if id:
            aluno = next(filter(lambda x: x["id"] == id, alunos), None)
            if aluno:
                return jsonify(aluno), 200
            else:
                return {"message": "Aluno não encontrado."}, 404
        else:
            return jsonify(alunos), 200

    def post(self):
        data = request.get_json()
        novo_id = alunos[-1]["id"] + 1 if alunos else 1
        novo_aluno = {"id": novo_id, "nome": data["nome"], "idade": data["idade"]}
        alunos.append(novo_aluno)
        return jsonify(novo_aluno), 201

    def put(self, id):
        data = request.get_json()
        aluno = next(filter(lambda x: x["id"] == id, alunos), None)
        if aluno:
            aluno.update(data)
            return jsonify(aluno), 200
        else:
            return {"message": "Aluno não encontrado."}, 404

    def delete(self, id):
        global alunos
        alunos = list(filter(lambda x: x["id"] != id, alunos))
        return {"message": "Aluno excluído com sucesso."}, 200

api.add_resource(Alunos, "/alunos", "/alunos/<int:id>")
