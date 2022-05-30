from flask_restful import Resource
from api import api
from ..schemas import cliente_schema
from flask import request, make_response, jsonify
from ..entidades import cliente
from ..services import cliente_service, endereco_service


class ClienteList(Resource):
    def get(self):
        clientes = cliente_service.listar_clientes()
        cs = cliente_schema.ClienteSchema(many=True)

        return make_response(cs.jsonify(clientes), 200)

    def post(self):
        cs = cliente_schema.ClienteSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            cpf = request.json["cpf"]
            email = request.json["email"]
            telefone = request.json["telefone"]
            endereco = request.json["endereco"]
            endereco_cliente = endereco_service.listar_endereco_id(endereco)
            if endereco_cliente is None:
                return make_response(jsonify("Endereço nao foi encontrado."), 404)
            novo_cliente = cliente.Cliente(nome=nome, cpf=cpf, email=email,
                                           telefone=telefone, endereco=endereco_cliente)
            resultado = cliente_service.cadastrar_cliente(novo_cliente)
            x = cs.jsonify(resultado)
            return make_response(x, 201)


class ClienteDetail(Resource):
    def get(self, id):
        cliente = cliente_service.listar_cliente_id(id)
        if cliente is None:
            return make_response(jsonify("Cliente não foi encontrado."), 404)
        cs = cliente_schema.ClienteSchema()
        return make_response(cs.jsonify(cliente), 200)

    def put(self, id):
        cliente_bd = cliente_service.listar_cliente_id(id)
        if cliente_bd is None:
            return make_response(jsonify("Cliente não foi encontrado."))
        cs = cliente_schema.ClienteSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            cpf = request.json["cpf"]
            email = request.json["email"]
            telefone = request.json["telefone"]
            endereco = request.json["endereco_id"]
            endereco_cliente = endereco_service.listar_endereco_id(endereco)
            if endereco_cliente is None:
                return make_response(jsonify("Endereço nao foi encontrado."), 404)
            novo_cliente = cliente.Cliente(nome=nome, cpf=cpf, email=email,
                                           telefone=telefone, endereco=endereco_cliente)
            cliente_service.atualiza_cliente(cliente_bd, novo_cliente)
            cliente_atualizado = cliente_service.listar_cliente_id(id)
            return make_response(cs.jsonify(cliente_atualizado), 200)

    def delete(self, id):
        cliente_bd = cliente_service.listar_cliente_id(id)
        if cliente_bd is None:
            return make_response(jsonify("Cliente não encontrado."), 404)
        cliente_service.remove_cliente(cliente_bd)
        return make_response("Cliente excluído com sucesso.", 204)


api.add_resource(ClienteList, '/clientes')
api.add_resource(ClienteDetail, '/clientes/<int:id>')
