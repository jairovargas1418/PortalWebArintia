from flask import Flask, jsonify

app = Flask(__name__)

SERVICES_DATA = {
    "mesa-ayuda": {"status": "Activo", "requests": 23},
    "nomina": {"status": "Disponible", "last_update": "2025-05-14"},
    "dms-mobile": {"status": "Operativo"},
    "r-sales": {"status": "Mantenimiento"},
    "solicitudes-compra": {"status": "En revisión"}
}

@app.route("/<service_name>", methods=["GET"])
def get_service(service_name):
    return jsonify(SERVICES_DATA.get(service_name, {"error": "Servicio no encontrado"}))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
