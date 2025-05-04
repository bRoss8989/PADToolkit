import numpy as np
from Modules.FIO.FioPull import FIO_PULL
from GlobalVars import global_foodreq

def workforce_req():

    req = FIO_PULL('global/workforceneeds')
    
    req_dict = {}
    
    for worker in req:
    
        temp_list = []
        for item in global_foodreq:
            temp_list.append(0)
    
        worker_name = worker['WorkforceType']
        
        for consum in worker['Needs']:
            index_pos = global_foodreq.index(consum['MaterialTicker'])
            amount = consum['Amount']
            temp_list[index_pos] = amount
            
        req_dict[worker_name] = np.array(temp_list, dtype=np.float32)

    return req_dict