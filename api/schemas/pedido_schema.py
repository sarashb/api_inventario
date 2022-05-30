from api import ma
from ..models import pedido_model
from marshmallow import fields


class PedidoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = pedido_model.Pedido
        load_instance = True
        fields = ("id", "data_compra")

    data_compra = fields.Date(required=True)