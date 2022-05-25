from api import ma
from ..models import produto_model
from marshmallow import fields

class ProdutoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = produto_model.Produto
        load_instance = True
        fields = ("id", "descricao", "velocidade", "preco", "disponibilidade")

    descricao = fields.String(required=True)
    velocidade = fields.String(required=True)
    preco = fields.Float(required=True)
    disponibilidade = fields.String(required=True)

