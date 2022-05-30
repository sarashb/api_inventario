from ..models import pedido_model
from api import db


def cadastrar_pedido(pedido):
    pedido_db = pedido_model.Pedido(data_compra=pedido.data_compra)
    db.session.add(pedido_db)
    db.session.commit()
    return pedido_db

def listar_pedidos():
    pedidos = pedido_model.Pedido.query.all()
    return pedidos

def listar_pedido_id(id):
    pedido = pedido_model.Pedido.query.filter_by(id=id).first()
    return pedido


def atualiza_pedido(pedido_anterior, pedido_novo):
    pedido_anterior.data_compra = pedido_novo.data_compra
    db.session.commit()


def remove_pedido(pedido):
    db.session.delete(pedido)
    db.session.commit()
