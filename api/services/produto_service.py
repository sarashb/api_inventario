from ..models import produto_model
from api import db


def cadastrar_produto(produto):
    produto_db = produto_model.Produto(descricao=produto.descricao, velocidade=produto.velocidade, preco=produto.preco,
                                       disponibilidade=produto.disponibilidade)
    db.session.add(produto_db)
    db.session.commit()
    return produto_db


def listar_produtos():
    produtos = produto_model.Produto.query.all()
    return produtos

def listar_produto_id(id):
    produto = produto_model.Produto.query.filter_by(id=id).first()
    return produto


def atualiza_produto(produto_anterior, produto_novo):
    produto_anterior.descricao = produto_novo.descricao
    produto_anterior.velocidade = produto_novo.velocidade
    produto_anterior.preco = produto_novo.preco
    produto_anterior.disponibilidade = produto_novo.disponibilidade

    db.session.commit()


def remove_produto(produto):
    db.session.delete(produto)
    db.session.commit()
