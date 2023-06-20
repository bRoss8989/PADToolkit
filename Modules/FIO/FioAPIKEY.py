import json
import requests
import os

def FIO_APIKEY():
    with open('auth.json', 'r') as file:
        apiauth = json.load(file)
        
    FIOAPIKEY = requests.post('https://rest.fnar.net/auth/login',json=apiauth)
    
    if str(FIOAPIKEY) != '<Response [200]>':
        return "auth error"
    else:
        FIOAPIKEY = json.loads(FIOAPIKEY.content)
        return FIOAPIKEY['AuthToken']