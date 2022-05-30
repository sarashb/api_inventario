from api import db

class Pedido(db.Model):
    __tablename__ = "pedido"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_compra = db.Column(db.Date, nullable=False)


