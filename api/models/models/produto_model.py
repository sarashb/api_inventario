from api import db

class Produto(db.Model):
    __tablename__ = "produto"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String(50), nullable=False)
    velocidade = db.Column(db.String(50), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    disponibilidade = db.Column(db.String(50), nullable=False)

    #endereco_id = db.Column(db.Integer, db.ForeignKey("endereco.id"))
    #endereco = db.relationship(endereco_model.Endereco, backref=db.backref("clientes", lazy="dynamic"))
