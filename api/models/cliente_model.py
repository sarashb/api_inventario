from api import db
# from ..models import endereco_model


class Cliente(db.Model):
    __tablename__ = "cliente"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.String(50), nullable=False)

    # endereco_id = db.Column(db.Integer, db.ForeignKey("endereco.id"))
    # endereco = db.relationship(endereco_model.Endereco, backref=db.backref("clientes", lazy="dynamic"))
