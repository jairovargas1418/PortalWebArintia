import tkinter as tk
from tkinter import messagebox
import requests

# Configuración de colores
BG_COLOR = "#FFFFFF"  # Fondo blanco
COLORS = ["#28A745", "#FF8C00", "#0078D7", "#FFD700"]  # Verde, Anaranjado, Azul, Amarillo

SERVER_URL = "http://localhost:5000"

def fetch_data(endpoint):
    """Función para obtener datos del servidor"""
    try:
        response = requests.get(f"{SERVER_URL}/{endpoint}")
        if response.status_code == 200:
            data = response.json()
            messagebox.showinfo("Respuesta del Servidor", f"{data}")
        else:
            messagebox.showerror("Error", f"Estado HTTP: {response.status_code}")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo conectar: {e}")

# Crear ventana principal
root = tk.Tk()
root.title("Servicios TI Arintia")
root.geometry("800x500")
root.configure(bg=BG_COLOR)

# Mensaje de bienvenida
welcome_label = tk.Label(root, text="Bienvenido al Portal Corporativo ARINTIA", fg="black", bg=BG_COLOR, font=("Arial", 16, "bold"))
welcome_label.pack(pady=20)

# Crear contenedor de botones
frame = tk.Frame(root, bg=BG_COLOR)
frame.pack(pady=10)

# Lista de servicios
services = [
    ("Mesa de Ayuda", "mesa-ayuda"),
    ("Nómina", "nomina"),
    ("DMS Mobile", "dms-mobile"),
    ("R-Sales", "r-sales"),
    ("Solicitudes Compra", "solicitudes-compra"),
]

# Dibujar botones rombo con colores diferentes
canvas = tk.Canvas(frame, width=800, height=200, bg=BG_COLOR, highlightthickness=0)
canvas.pack()

def create_rhombus_button(x, y, text, endpoint, color):
    """Crea un botón en forma de rombo con un color específico"""
    points = [x, y+30, x+50, y, x+100, y+30, x+50, y+60]
    canvas.create_polygon(points, fill=color, outline="black", width=2)
    btn = tk.Button(frame, text=text, fg="black", bg=color, font=("Arial", 10, "bold"), command=lambda: fetch_data(endpoint))
    btn.place(x=x+10, y=y+15, width=80, height=30)

# Crear los botones con diferentes colores
start_x, start_y = 50, 50
spacing = 120  # Espaciado entre botones

for i, (label, endpoint) in enumerate(services):
    create_rhombus_button(start_x + (i * spacing), start_y, label, endpoint, COLORS[i % len(COLORS)])

# Ejecutar la aplicación
root.mainloop()
