from Modules.FIO.FioAllSystemsDict import FioNaturalSystems
from Modules.FIO.FioNaturalSystems import FioNaturalSystemsList

def systemid_to_system():
    
    system_data = FioNaturalSystems()
    id_dict = {}
    systems_list = FioNaturalSystemsList()
    
    for system in systems_list:
        id = system_data[system]['SystemId']
        id_dict[id] = system
    return id_dict, system_data, systems_list


def system_conns():
    
    systems_connection_dict = {}
    id_dict, system_data, systems_list = systemid_to_system()
    
    for system in systems_list:
        connections = system_data[system]['Connections']
        value = []
        for connection in connections:
            raw_connection = connection['SystemConnectionId']
            next_system = str(raw_connection[33:65])
            next_system = id_dict[next_system]
            value.append([system + '->' + next_system, next_system])
            
        systems_connection_dict[system] = value
        
    return systems_connection_dict