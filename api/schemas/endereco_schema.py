from api import ma
from ..models import endereco_model
from marshmallow import fields
from ..schemas import cliente_schema


class EnderecoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = endereco_model.Endereco
        load_instance = True
        fields = ("id", "cep", "rua", "numero", "bairro", "cidade", "estado", "clientes")

    cep = fields.String(required=True)
    rua = fields.String(required=True)
    numero = fields.String(required=True)
    bairro = fields.String(required=True)
    cidade = fields.String(required=True)
    estado = fields.String(required=True)
    clientes = fields.List(fields.Nested(cliente_schema.ClienteSchema, only=('id', 'nome')))
