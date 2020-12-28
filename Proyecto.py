import pyotp
import sqlite3
import hashlib
import uuid
import requests
import json
from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return 'Welcome David Lopez APP'

@app.route('/permiso')
def lista():
    url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
    headers = {
        'Content-type': 'application/json',
        'Accept': 'application/json'
    }
    respuesta = requests.post(url, auth=('devnetuser', 'Cisco123!'), headers=headers)
    token = respuesta.text
    token = json.loads(token)
    token = token['Token']
    return token


if __name__ == '__main__':
    app.run()

