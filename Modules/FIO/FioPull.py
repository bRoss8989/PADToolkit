from Modules.FIO.FioAPIKEY import FIO_APIKEY
import requests
import json
import os
from CommonPaths import fio_base_dir

def FIO_PULL(location):
    
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
        FIO_PULL(location)
        
    if str(fiocontent) == '<Response [200]>':
        return json.loads(fiocontent.content)

def FIO_KEY_CHECK():
    if os.path.exists(fio_base_dir+'fiokey.json') == False:
        
        head = {'Authorization':FIO_APIKEY()}
        
        if head == "auth error":
            return 'auth error'
        
        with open(fio_base_dir+'fiokey.json', 'w') as fp:
            json.dump(head, fp)
            
    else:
        with open(fio_base_dir+'fiokey.json', 'r') as file:
            head = json.load(file)
            
    return head
    
