from flask import Flask, jsonify

app = Flask(__name__)

# Datos de ejemplo (pueden ser cualquier cosa)
datos = [
    {"id": 1, "nombre": "Producto 1", "precio": 10.99},
    {"id": 2, "nombre": "Producto 2", "precio": 20.49},
    {"id": 3, "nombre": "Producto 3", "precio": 5.99}
]

# Ruta para obtener todos los datos
@app.route('/productos', methods=['GET'])
def obtener_productos():
    return jsonify({"productos": datos})

# Ruta para obtener un producto por su ID
@app.route('/productos/<int:id>', methods=['GET'])
def obtener_producto(id):
    producto = next((p for p in datos if p['id'] == id), None)
    if producto:
        return jsonify(producto)
    else:
        return jsonify({"mensaje": "Producto no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
