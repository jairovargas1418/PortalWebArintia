from flask import Flask, jsonify

app = Flask(__name__)

# Datos simulados del servidor de pruebas
TEST_DATA = {
    "mesa-ayuda": {"status": "Activo", "requests": 5},
    "nomina": {"status": "Disponible"},
    "dms-mobile": {"status": "Operativo"},
    "r-sales": {"status": "Mantenimiento"},
    "solicitudes-compra": {"status": "Pendiente"}
}

@app.route("/<service_name>", methods=["GET"])
def get_service(service_name):
    return jsonify(TEST_DATA.get(service_name, {"error": "Servicio no encontrado"}))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Servidor de pruebas en el puerto 5000
