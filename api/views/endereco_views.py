from flask_restful import Resource
from api import api
from ..schemas import endereco_schema
from flask import request, make_response, jsonify
from ..entidades import endereco
from ..services import endereco_service


class EnderecoList(Resource):
    def get(self):
        enderecos = endereco_service.listar_enderecos()
        es = endereco_schema.EnderecoSchema(many=True)

        return make_response(es.jsonify(enderecos), 200)

    def post(self):
        es = endereco_schema.EnderecoSchema()
        validate = es.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            cep = request.json["cep"]
            rua = request.json["rua"]
            numero = request.json["numero"]
            bairro = request.json["bairro"]
            cidade = request.json["cidade"]
            estado = request.json["estado"]

            novo_endereco = endereco.Endereco(cep=cep, rua=rua, numero=numero, bairro=bairro, cidade=cidade, estado=estado)
            resultado = endereco_service.cadastrar_endereco(novo_endereco)
            x = es.jsonify(resultado)
            return make_response(x, 201)


class EnderecoDetail(Resource):
    def get(self, id):
        endereco = endereco_service.listar_endereco_id(id)
        if endereco is None:
            return make_response(jsonify("Endereço não foi encontrado."), 404)
        es = endereco_schema.EnderecoSchema()
        return make_response(es.jsonify(endereco), 200)

    def put(self, id):
        endereco_bd = endereco_service.listar_endereco_id(id)
        if endereco_bd is None:
            return make_response(jsonify("Endereço não foi encontrado."))
        es = endereco_schema.EnderecoSchema()
        validate = es.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            cep = request.json["cep"]
            rua = request.json["rua"]
            numero = request.json["numero"]
            bairro = request.json["bairro"]
            cidade = request.json["cidade"]
            estado = request.json["estado"]
            novo_endereco = endereco.Endereco(cep=cep, rua=rua, numero=numero, bairro=bairro, cidade=cidade, estado=estado)
            endereco_service.atualiza_endereco(endereco_bd, novo_endereco)
            endereco_atualizado = endereco_service.listar_endereco_id(id)
            return make_response(es.jsonify(endereco_atualizado), 200)

    def delete(self, id):
        endereco_bd = endereco_service.listar_endereco_id(id)
        if endereco_bd is None:
            return make_response(jsonify("Endereço não encontrado."), 404)
        endereco_service.remove_endereco(endereco_bd)
        return make_response("Endereço excluído com sucesso.", 204)


api.add_resource(EnderecoList, '/enderecos')
api.add_resource(EnderecoDetail, '/enderecos/<int:id>')
