from flask_restful import Resource
from api import api
from ..schemas import produto_schema
from flask import request, make_response, jsonify
from ..entidades import produto
from ..services import produto_service


class ProdutoList(Resource):
    def get(self):
        produtos = produto_service.listar_produtos()
        ps = produto_schema.ProdutoSchema(many=True)

        return make_response(ps.jsonify(produtos), 200)

    def post(self):
        ps = produto_schema.ProdutoSchema()
        validate = ps.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            descricao = request.json["descricao"]
            velocidade = request.json["velocidade"]
            preco = request.json["preco"]
            disponibilidade = request.json["disponibilidade"]

            novo_produto = produto.Produto(descricao=descricao, velocidade=velocidade, preco=preco,
                                           disponibilidade=disponibilidade)
            resultado = produto_service.cadastrar_produto(novo_produto)
            x = ps.jsonify(resultado)
            return make_response(x, 201)


class ProdutoDetail(Resource):
    def get(self, id):
        produto = produto_service.listar_produto_id(id)
        if produto is None:
            return make_response(jsonify("Produto não foi encontrado."), 404)
        ps = produto_schema.ProdutoSchema()
        return make_response(ps.jsonify(produto), 200)

    def put(self, id):
        produto_bd = produto_service.listar_produto_id(id)
        if produto_bd is None:
            return make_response(jsonify("Produto não foi encontrado."))
        ps = produto_schema.ProdutoSchema()
        validate = ps.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            descricao = request.json["descricao"]
            velocidade = request.json["velocidade"]
            preco = request.json["preco"]
            disponibilidade = request.json["disponibilidade"]

            novo_produto = produto.Produto(descricao=descricao, velocidade=velocidade, preco=preco,
                                           disponibilidade=disponibilidade)
            produto_service.atualiza_produto(produto_bd, novo_produto)
            produto_atualizado = produto_service.listar_produto_id(id)
            return make_response(ps.jsonify(produto_atualizado), 200)

    def delete(self, id):
        produto_bd = produto_service.listar_produto_id(id)
        if produto_bd is None:
            return make_response(jsonify("Produto não encontrado."), 404)
        produto_service.remove_produto(produto_bd)
        return make_response("Produto excluído com sucesso.", 204)


api.add_resource(ProdutoList, '/produtos')
api.add_resource(ProdutoDetail, '/produtos/<int:id>')
