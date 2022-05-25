from api import db

class Endereco(db.Model):
    __tablename__ = "endereco"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cep = db.Column(db.String(8), nullable=False)
    rua = db.Column(db.String(50), nullable=False)
    numero = db.Column(db.String(50), nullable=False)
    bairro = db.Column(db.String(50), nullable=False)
    cidade = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.String(50), nullable=False)
