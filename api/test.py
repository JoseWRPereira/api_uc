from flask import Blueprint
from flask import request, json
from flask_restful import Resource, Api

test_bp = Blueprint('test_bp',__name__)
api = Api(test_bp)

equipe = [
    {   'id':0, 
        'nome':'José', 
        'cargo':'Programador' 
    },
    {   'id':1, 
        'nome':'William', 
        'cargo':'Cientista de dados' 
    }
]

class Equipe(Resource):
    def get(self):
        return equipe

    def post(self):
        dados = json.loads(request.data)
        posicao = len(equipe)
        dados['id'] = posicao
        equipe.append(dados)
        return equipe[posicao]

class EquipeUser(Resource):
    def get(self, id):
        try:
            response = equipe[id]
        except IndexError:
            mensagem = "Tarefa com ID {} não existe!".format(id)
            response = {"status": "erro", "mensagem": mensagem }
        except Exception:
            mensagem = "Erro desconhecido. Procure o administrador da API!"
            response = {"status": "erro", "mensagem": mensagem }
        return response

    def put(self, id):
        dados = json.loads(request.data)
        equipe[id] = dados
        return dados
    
    def delete(self, id):
        equipe.pop(id)
        return {'status':'Sucesso', 'mensagem':'Registro excluído'}






api.add_resource(Equipe,'/equipe')
api.add_resource(EquipeUser,'/equipe/<int:id>')

@test_bp.route('/api')
def api():
    return "API Blueprint"


