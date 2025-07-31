from marshmallow import Schema, fields

class TransaccionSchema(Schema):
    monto = fields.Float(required=True)
    titular = fields.Str(required=True)
    pan = fields.Str(required=True, validate=lambda s: len(s) == 16)  # ⚠️ CRÍTICO
    ultimos_4_digitos = fields.Str(required=True, validate=lambda s: len(s) == 4)
    marca_tarjeta = fields.Str(required=True)
    direccion = fields.Str(required=True)
    ciudad = fields.Str(required=True)
    departamento = fields.Str(required=True)
    codigo_postal = fields.Str(required=True)

