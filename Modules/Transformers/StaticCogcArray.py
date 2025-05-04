from Modules.FIO.FioCogc import fio_cogc
from GlobalVars import default_prod_buildings, global_planets
from Modules.FIO.FioAllBuildingsDict import FioBuildingsDict
import numpy as np





############ returns of dict of the default prod building keys with two dicts for main cog type and workforce bonus weights
def cog_info():
    bui_cogc_info = {}
    buildings = FioBuildingsDict()

    for bui in default_prod_buildings:
        temp_work_list = []
        weights = {}
        main_cog_search = buildings[bui]['Expertise']
        
        temp_work_list.append(buildings[bui]['Pioneers'])
        temp_work_list.append(buildings[bui]['Settlers'])
        temp_work_list.append(buildings[bui]['Technicians'])
        temp_work_list.append(buildings[bui]['Engineers'])
        temp_work_list.append(buildings[bui]['Scientists'])
    
        temp_work_list = np.array(temp_work_list, dtype=np.float32)
        total = temp_work_list.sum()
    
        temp_work_list2 = temp_work_list / total
    
        weights['pioneers'] = temp_work_list2[0]
        weights['settlers'] = temp_work_list2[1]
        weights['technicians'] = temp_work_list2[2]
        weights['engineers'] = temp_work_list2[3]
        weights['scientists'] = temp_work_list2[4]
    
        bui_cogc_info[bui] = {}
        bui_cogc_info[bui]['main_cog_search'] = main_cog_search.lower()
        bui_cogc_info[bui]['workforce_cog_weights'] = weights

    return bui_cogc_info

########### returns a dict with default prod building keys and the the cogc bonus for that building for each prod planet
def cog_arrays():

    cog_array = {}

    cogc = fio_cogc()
    bui_cogc_info = cog_info()

    for bui in default_prod_buildings:
        
        arr = np.ones((4155, 1), dtype=np.float32)
        main = bui_cogc_info[bui]['main_cog_search']
        weights = bui_cogc_info[bui]['workforce_cog_weights']
        
        index = 0
        
        for planet in global_planets:
            
            current_cog = cogc[planet]
            
            if current_cog == None:
                index = index + 1
                continue
            current_cog = current_cog.lower()
    
            if main in current_cog:
                arr[index] = 1.25
                index = index + 1
                continue
    
            for worker in weights:
    
                if worker in current_cog:
                    arr[index] = 0.1 * weights[worker] + 1
                    break
            index = index + 1
        cog_array[bui] = arr

    return cog_array
