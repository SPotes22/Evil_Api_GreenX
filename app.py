from flask import Flask, request, jsonify , render_template
from marshmallow import ValidationError
from schema import TransaccionSchema
from models import db, Transaccion
import uuid
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Configuración SQLite
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'transacciones.db')

# Por esta:
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flaskuser:flaskpass@localhost/transacciones'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Crear la base de datos al inicio
with app.app_context():
    db.create_all()

@app.route('/transaccion', methods=['POST'])
def crear_transaccion():
    schema = TransaccionSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({"errores": err.messages}), 400

    transaction_id = str(uuid.uuid4())
    nueva_transaccion = Transaccion(
        transaction_id=transaction_id,
        **data
    )

    db.session.add(nueva_transaccion)
    db.session.commit()
    ''' RESPUESTA API
    return jsonify({
        "status": "aprobado",
        "transaction_id": transaction_id,
        "timestamp": nueva_transaccion.fecha.isoformat()
    }), 200
    '''
    # Respuesta Malvada :0
    # Guardar log en archivo plano
    log_entry = f"{transaction_id},{data['titular']},{data['pan']},{data['monto']},{data['marca_tarjeta']},{data['direccion']},{data['ciudad']},{data['departamento']},{data['codigo_postal']},{nueva_transaccion.fecha.isoformat()}\n"
    with open("transacciones_log.csv", "a") as f:
        f.write(log_entry)

    return render_template('return.html', transaction_id=transaction_id)
# Crud malvado
@app.route('/dashboard')
def dashboard():
    transacciones = Transaccion.query.all()
    return render_template('dashboard.html', transacciones=transacciones)


if __name__ == "__main__":
    app.run(debug=True)


