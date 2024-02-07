#Importar en app.py la función frotar de bayeta.py
from bayeta import frotar, insertar_frases

#Importar flask
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    frases = frotar(5)
    return jsonify({'frases': frases})

@app.route('/frotar/<int:n_frases>', methods=['GET'])
def obtener_frases(n_frases):
    frases = frotar(n_frases)
    return jsonify({'frases': frases})

@app.route('/frotar/add', methods=['POST'])
def agregar_frases():
    data = request.json
    frases = data.get('frases', [])
    if frases:
        insertar_frases(frases)
        return jsonify({'message': 'Frases añadidas correctamente.'}), 200
    else:
        return jsonify({'error': 'No se proporcionaron frases.'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0')
