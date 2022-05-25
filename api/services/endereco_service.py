from ..models import endereco_model
from api import db


def cadastrar_endereco(endereco):
    endereco_db = endereco_model.Endereco(cep=endereco.cep, rua=endereco.rua, numero=endereco.numero, bairro=endereco.bairro, cidade=endereco.cidade, estado=endereco.estado)
    db.session.add(endereco_db)
    db.session.commit()
    return endereco_db

def listar_enderecos():
    enderecos = endereco_model.Endereco.query.all()
    return enderecos

def listar_endereco_id(id):
    endereco = endereco_model.Endereco.query.filter_by(id=id).first()
    return endereco


def atualiza_endereco(endereco_anterior, endereco_novo):
    endereco_anterior.cep = endereco_novo.cep
    endereco_anterior.rua = endereco_novo.rua
    endereco_anterior.numero = endereco_novo.numero
    endereco_anterior.bairro = endereco_novo.bairro
    endereco_anterior.cidade = endereco_novo.cidade
    endereco_anterior.estado = endereco_novo.estado

    db.session.commit()

def remove_endereco(endereco):
    db.session.delete(endereco)
    db.session.commit()
