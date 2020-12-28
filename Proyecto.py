import pyotp
import sqlite3
import hashlib
import uuid
from flask import Flask, request

app=Flask(__name__)


@app.route('/welcome')
def index():
    return 'Welcome David Lopez APP'

if __name__ == '__main__':
    app.run(host='sandboxdnac.cisco.com', ssl_context='adhoc')

