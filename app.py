# app.py
#Importar en app.py la función frotar de bayeta.py
from bayeta import frotar

#Importar flask
from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    frases = frotar(5)
    return jsonify({'frases': frases})

@app.route('/frotar/<int:n_frases>', methods=['GET'])
def obtener_frases(n_frases):
    frases = frotar(n_frases)
    return jsonify({'frases': frases})

if __name__ == '__main__':
    app.run(host='0.0.0.0')