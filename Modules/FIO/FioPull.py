from Modules.FIO.FioAPIKEY import FIO_APIKEY
import requests
import json
import os
import time
from CommonPaths import fio_base_dir

def FIO_PULL(location, loop=0):             #1. gets api headers via key check
                                            #2. pulls api data, gets new key if auth fails
    while loop != 2:
        head = FIO_KEY_CHECK()
        
        if head == "auth error":
            return head
        
        fiocontent = requests.get('https://rest.fnar.net/'+location,headers=head)

        if str(fiocontent) == '<Response [400]>':
            return "parse error"

        if str(fiocontent) == '<Response [204]>':
            return "path error"  

        if str(fiocontent) == '<Response [401]>':       
            os.remove(fio_base_dir+'fiokey.json')
            time.sleep(5)
            if loop == 2:
                return 'repeating auth error'
            loop = loop + 1

        if str(fiocontent) == '<Response [200]>':
            return json.loads(fiocontent.content)

def FIO_KEY_CHECK():
    if os.path.exists(fio_base_dir+'fiokey.json') == False:
        
        head = {'Authorization':FIO_APIKEY()}
        
        if head == "auth error":
            head = 'auth error'
        else:
            with open(fio_base_dir+'fiokey.json', 'w') as fp:
                json.dump(head, fp)
            
    else:
        with open(fio_base_dir+'fiokey.json', 'r') as file:
            head = json.load(file)
            
    return head
    
