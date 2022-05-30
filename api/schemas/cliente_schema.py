from api import ma
from ..models import cliente_model
from marshmallow import fields


class ClienteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = cliente_model.Cliente
        load_instance = True
        fields = ("id", "nome", "cpf", "email", "telefone", "endereco_id")

    nome = fields.String(required=True)
    cpf = fields.String(required=True)
    email = fields.String(required=True)
    telefone = fields.String(required=True)
    endereco_id = fields.String(required=True)

