from flask_restful import Resource
from api import api
from ..schemas import pedido_schema
from flask import request, make_response, jsonify
from ..entidades import pedido
from ..services import pedido_service


class PedidoList(Resource):
    def get(self):
        pedidos = pedido_service.listar_pedidos()
        ps = pedido_schema.PedidoSchema(many=True)

        return make_response(ps.jsonify(pedidos), 200)

    def post(self):
        ps = pedido_schema.PedidoSchema()
        validate = ps.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            data_compra = request.json["data_compra"]
            novo_pedido = pedido.Pedido(data_compra=data_compra)
            resultado = pedido_service.cadastrar_pedido(novo_pedido)
            x = ps.jsonify(resultado)
            return make_response(x, 201)


class PedidoDetail(Resource):
    def get(self, id):
        pedido = pedido_service.listar_pedido_id(id)
        if pedido is None:
            return make_response(jsonify("Pedido não foi encontrado."), 404)
        ps = pedido_schema.PedidoSchema()
        return make_response(ps.jsonify(pedido), 200)

    def put(self, id):
        pedido_bd = pedido_service.listar_pedido_id(id)
        if pedido_bd is None:
            return make_response(jsonify("Pedido não foi encontrado."))
        ps = pedido_schema.PedidoSchema()
        validate = ps.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            data_compra = request.json["data_compra"]

            novo_pedido = pedido.Pedido(data_compra=data_compra)

            pedido_service.atualiza_pedido(pedido_bd, novo_pedido)
            pedido_atualizado = pedido_service.listar_pedido_id(id)
            return make_response(ps.jsonify(pedido_atualizado), 200)

    def delete(self, id):
        pedido_bd = pedido_service.listar_pedido_id(id)
        if pedido_bd is None:
            return make_response(jsonify("Pedido não encontrado."), 404)
        pedido_service.remove_pedido(pedido_bd)
        return make_response("Pedido excluído com sucesso.", 204)


api.add_resource(PedidoList, '/pedidos')
api.add_resource(PedidoDetail, '/pedidos/<int:id>')
