import requests
import json

url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
headers = {
    'Content-type': 'application/json',
    'Accept': 'application/json'
}
respuesta = requests.post(url, auth=('devnetuser', 'Cisco123!'), headers=headers)
token = respuesta.text
token = json.loads(token)
token = token['Token']
