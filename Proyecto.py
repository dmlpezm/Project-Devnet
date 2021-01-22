import pyotp
import sqlite3
import hashlib
import uuid
import requests
import json
from flask import Flask, request, jsonify, render_template
from llave import token

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("Base.html",content =["Listar Dispositivos : /dispositivos","Agregar Dispositivos : /dispositivos/add","Eliminar Dispositivos : /dispositivos/del"])

#funcion que me permite listar los dispositivos de DNA
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

#Funcion que permite agregar dispositivos
@app.route('/dispositivos/add',methods=['GET','POST'])
def agregar():
    url = 'https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device'
    headers = {
        'Content-type': 'application/json',
        'Accept': 'application/json',
        'X-Auth-Token': token
    }
    body = {
        'macAddress': 'g8:4b:10:66:62:85',
        'managementIpAddress': '100.100.220.1',
        'softwareType': 'IOS-XE',
        'type': 'Cisco Catalyst 9300 Switch'
    }

    respuesta = requests.request('POST', url, headers=headers,data=body, verify=False)
    return "Dispositivo agregado: "+str(respuesta.status_code)


if __name__ == '__main__':
    app.run(debug=True)

#Linea desde branch master on a new directory
