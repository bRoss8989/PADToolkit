import numpy as np
from Modules.FIO.FioAllBuildingsDict import FioBuildingsDict
from Modules.FIO.workforce_req import workforce_req
from Modules.Calcs.ppd_functions import reqhash_to_array
from GlobalVars import default_buildings, global_buildreq, planner

buildings = FioBuildingsDict()
req_dict = workforce_req()

req_combos = (34, 102, 170, 221, 2431, 114, 190, 2, 10, 38, 6, 714, 13, 42, 798, 247)

cost_per_area = {
    'INS':10,
    'AEF':0.33333333,
    'SEA':1,
    'MCG':4
}
cost_per_array = [0] * len(global_buildreq)
for key, value in cost_per_area.items():
    index = global_buildreq.index(key)
    cost_per_array[index] = value
cost_per_array = np.array(cost_per_array)



def planner_bui_count():
    base_plan_bui = {}
    for key in planner:
    
        temp_list = []
        for x in default_buildings:
            temp_list.append(0)
        
        for building, value in planner[key].items():
            index = default_buildings.index(building)
            temp_list[index] = value
            
        base_plan_bui[key] = np.array(temp_list)

    return base_plan_bui

def full_dict_build_arrays():

    # each building will have keys (buildingreq_array, foodreq_array, combos, planner bui count)
    full_dict_building_arrays = {}
    for bui in default_buildings:
    
        data = buildings[bui]
    
        temp_buildreq = [0] * len(global_buildreq)
        #adding areacost into dict
        full_dict_building_arrays[bui] = {}
        area = data['AreaCost']
        
        for cost in data['BuildingCosts']:
            index = global_buildreq.index(cost['CommodityTicker'])
            temp_buildreq[index] = cost['Amount']
    
        # adding buildingreq_array
        full_dict_building_arrays[bui]['buildreq_array'] = np.array(temp_buildreq)
    
        pio = data['Pioneers']
        set = data['Settlers']
        tech = data['Technicians']
        eng = data['Engineers']
        sci = data['Scientists']
    
        temp_food = (np.array(req_dict['PIONEER']) * pio
                     + np.array(req_dict['SETTLER']) * set
                     + req_dict['TECHNICIAN'] * tech
                     + req_dict['ENGINEER'] * eng
                     + req_dict['SCIENTIST'] * sci
                    )
        # adding foodreq
        full_dict_building_arrays[bui]['foodreq_array'] = temp_food / 100
    
        combos = {}
    
        for combo in req_combos:
            combos[combo] = reqhash_to_array(combo)
            area_multiple = cost_per_array*area
            area_multiple2 = []
            for x in area_multiple:
                if x != 0:
                   area_multiple2.append(x)
                else:
                    area_multiple2.append(1)
            combos[combo] = combos[combo] * area_multiple2  
           
        # adding combos
        full_dict_building_arrays[bui]['combos'] = combos
    
    # adding planner bui counts
    full_dict_building_arrays['planner'] = planner_bui_count()

    return full_dict_building_arrays
        