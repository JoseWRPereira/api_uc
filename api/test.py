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

api.add_resource(Equipe,'/equipe')

@test_bp.route('/api')
def api():
    return "API Blueprint"


