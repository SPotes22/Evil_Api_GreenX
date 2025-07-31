from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Transaccion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transaction_id = db.Column(db.String(36), unique=True, nullable=False)
    monto = db.Column(db.Float, nullable=False)
    titular = db.Column(db.String(100), nullable=False)
    pan = db.Column(db.String(16), nullable=False)  # ⚠️ CRÍTICO
    ultimos_4_digitos = db.Column(db.String(4), nullable=False)
    marca_tarjeta = db.Column(db.String(20), nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    ciudad = db.Column(db.String(100), nullable=False)
    departamento = db.Column(db.String(100), nullable=False)
    codigo_postal = db.Column(db.String(10), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)

