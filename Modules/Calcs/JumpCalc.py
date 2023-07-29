
from multiprocessing import Pool
from itertools import starmap
from Modules.Transformers.abc_planet_system_keygen import abc_key
from Modules.Transformers.StaticPairs import system_pairs
from Modules.Transformers.StaticSystemConns import system_conns
from Modules.Transformers.Parsec import parsec
from Modules.FIO.FioNaturalSystems import FioNaturalSystemsList
import json

conns = system_conns()
systems = FioNaturalSystemsList()
parsec_dict = parsec()



def next_path(path_list, complete_path, system_lowest_path,end):
      
    new_path_list = []
    for path in path_list:
        starting_parsecs = path[0]
        for con in conns[path[-1]]:
            new_path = path[:]
            new_path[0] = new_path[0] + parsec_dict[con[0]]
            
            if new_path[0] > system_lowest_path[con[1]] or new_path[0] > complete_path[0]:
                continue
            system_lowest_path[con[1]] = new_path[0]
            new_path.append(con[1])
    
            if con[1] == end:
                complete_path = new_path
            
            new_path_list.append(new_path)
    return new_path_list, complete_path, system_lowest_path


def fastest_path(start,end):
    
    path_list = [[0,start]]
    complete_path = [1000,'']
    system_lowest_path = {}

    for system in systems:
        system_lowest_path[system] = 1000

    bounds = 0
    while bounds != 100:

        path_list, complete_path, system_lowest_path = next_path(path_list, complete_path, system_lowest_path, end)
        bounds = bounds +1
        if path_list == []:
            break
    final = [abc_key(start,end),complete_path[0],len(complete_path)-2]
    return final


def all_systempairs_fastest_path():            # returns a list of all paths [pair,parsecs,jump count]

    pairs = system_pairs()
    
    map_list = []
    for pair in pairs.items():
        map_list.append(pair[1])

    if __name__ == "__main__":  
        with Pool() as p:
            return p.starmap(fastest_path,map_list)

print(json.dumps(all_systempairs_fastest_path()))



