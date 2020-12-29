import pyotp
import sqlite3
import hashlib
import uuid
import requests
import json
from flask import Flask, request, jsonify
from llave import token

app=Flask(__name__)

@app.route('/')
def index():
    return 'Welcome David Lopez APP'


@app.route('/dispositivos', methods=['GET','POST'])
def listar():
    url = 'https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device'
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': token
    }
    respuesta = requests.request('GET', url, headers=headers, verify=False)
    resultado = respuesta.text
    resultado = json.loads(resultado)
    return jsonify(resultado)


if __name__ == '__main__':
    app.run(debug=True)

