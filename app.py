from flask import Flask, render_template, jsonify

app = Flask(__name__)

SERVICES_DATA = {
    "mesa-ayuda": {"status": "Activo", "requests": 5},
    "nomina": {"status": "Disponible"},
    "dms-mobile": {"status": "Operativo"},
    "r-sales": {"status": "Mantenimiento"},
    "solicitudes-compra": {"status": "Pendiente"},
    "outlook": {"status": "Conectado a Outlook 365"},
    "conexion-arintia": {"status": "VPN activa en ARINTIA"},
    "sharepoint": {"status": "Acceso autorizado"},
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/<service_name>")
def get_service(service_name):
    return jsonify(SERVICES_DATA.get(service_name, {"error": "Servicio no encontrado"}))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
