from ..models import cliente_model
from api import db


def cadastrar_cliente(cliente):
    cliente_db = cliente_model.Cliente(nome=cliente.nome, cpf=cliente.cpf, email=cliente.email,
                                       telefone=cliente.telefone, endereco=cliente.endereco)
    db.session.add(cliente_db)
    db.session.commit()
    return cliente_db

def listar_clientes():
    clientes = cliente_model.Cliente.query.all()
    return clientes

def listar_cliente_id(id):
    cliente = cliente_model.Cliente.query.filter_by(id=id).first()
    return cliente


def atualiza_cliente(cliente_anterior, cliente_novo):
    cliente_anterior.nome = cliente_novo.nome
    cliente_anterior.cpf = cliente_novo.cpf
    cliente_anterior.email = cliente_novo.email
    cliente_anterior.telefone = cliente_novo.telefone
    cliente_anterior.endereco = cliente_novo.endereco
    db.session.commit()


def remove_cliente(cliente):
    db.session.delete(cliente)
    db.session.commit()