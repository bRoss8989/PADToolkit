import numpy as np
from Modules.FIO.FioAllBuildingsDict import FioBuildingsDict
from Modules.FIO.workforce_req import workforce_req
from Modules.Calcs.ppd_functions import reqhash_to_array
from GlobalVars import default_buildings, global_buildreq

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

planner = {
    'AAF':{
        'CM':1,
        'HB4':3,
        'HB5':2,
        'STO':2,
        'AAF':7},
    'AML':{
        'CM':1,
        'HB3':2,
        'HB4':3,
        'STO':2,
        'AML':8},
    'APF':{
        'CM':1,
        'HB3':5,
        'HB4':2,
        'STO':3,
        'APF':8},
    'ASM':{
        'CM':1,
        'HB3':5,
        'HB4':2,
        'STO':2,
        'ASM':10},
    'BMP':{
        'CM':1,
        'HB1':20,
        'STO':2,
        'BMP':20},
    'CHP':{
        'CM':1,
        'HB1':3,
        'HB2':9,
        'HBB':1,
        'STO':2,
        'CHP':16},
    'CLF':{
        'CM':1,
        'HB2':4,
        'STO':3,
        'CLF':10},
    'CLR':{
        'CM':1,
        'HB2':3,
        'HB3':2,
        'HBC':1,
        'STO':1,
        'CLR':14},
    'COL':{
        'CM':1,
        'HB1':11,
        'STO':2,
        'COL':22},
    'DRS':{
        'CM':1,
        'HB3':5,
        'HB4':3,
        'STO':1,
        'DRS':11},
    'ECA':{
        'CM':1,
        'HBC':3,
        'STO':2,
        'ECA':11},
    'EDM':{
        'CM':1,
        'HB2':6,
        'STO':2,
        'EDM':12},
    'EEP':{
        'CM':1,
        'HB4':2,
        'HB5':1,
        'HBL':1,
        'EEP':4},
    'ELP':{
        'CM':1,
        'HB3':5,
        'STO':1,
        'ELP':11},
    'EXT':{
        'CM':1,
        'HB1':9,
        'STO':2,
        'EXT':14},
    'FER':{
        'CM':1,
        'HB2':9,
        'STO':1,
        'FER':14},
    'FP':{
        'CM':1,
        'HB1':12,
        'STO':1,
        'FP':28},
    'FRM':{
        'CM':1,
        'HB1':7,
        'STO':1,
        'FRM':13},
    'FS':{
        'CM':1,
        'HB2':7,
        'STO':2,
        'FS':14},
    'GF':{
        'CM':1,
        'HB2':10,
        'STO':2,
        'GF':12},
    'HWP':{
        'CM':1,
        'HB2':5,
        'HB3':1,
        'HBC':1,
        'STO':2,
        'HWP':14},
    'HYF':{
        'CM':1,
        'HB1':4,
        'HBB':6,
        'STO':2,
        'HYF':21},
    'INC':{
        'CM':1,
        'HB1':13,
        'STO':1,
        'INC':32},
    'IVP':{
        'CM':1,
        'HB3':7,
        'STO':3,
        'IVP':10},
    'LAB':{
        'CM':1,
        'HB2':2,
        'HB3':8,
        'HBC':1,
        'STO':1,
        'LAB':12},
    'MCA':{
        'CM':1,
        'HB2':2,
        'HB3':2,
        'HBC':1,
        'STO':1,
        'MCA':11},
    'ORC':{
        'CM':1,
        'HB2':2,
        'HBC':1,
        'STO':2,
        'ORC':3},
    'PHF':{
        'CM':1,
        'HB2':2,
        'HB3':2,
        'HBC':1,
        'STO':1,
        'PHF':11},
    'POL':{
        'CM':1,
        'HB1':1,
        'HB2':5,
        'HBB':2,
        'STO':1,
        'POL':24},
    'PP1':{
        'CM':1,
        'HB1':13,
        'STO':2,
        'PP1':16},
    'PP2':{
        'CM':1,
        'HBB':5,
        'STO':2,
        'PP2':15},
    'PP3':{
        'CM':1,
        'HB2':1,
        'HB3':3,
        'HBC':2,
        'STO':2,
        'PP3':11},
    'PP4':{
        'CM':1,
        'HB3':3,
        'HB4':2,
        'HBM':1,
        'STO':1,
        'PP4':9},
    'PPF':{
        'CM':1,
        'HB2':11,
        'PPF':21},
    'REF':{
        'CM':1,
        'HB1':8,
        'HB2':3,
        'STO':2,
        'REF':13},
    'RIG':{
        'CM':1,
        'HB1':11,
        'STO':1,
        'RIG':35},
    'SCA':{
        'CM':1,
        'HB3':4,
        'STO':2,
        'SCA':11},
    'SD':{
        'CM':1,
        'HB3':9,
        'SD':17},
    'SE':{
        'CM':1,
        'HB4':6,
        'STO':1,
        'SE':18},
    'SKF':{
        'CM':1,
        'HB2':4,
        'HB3':1,
        'STO':3,
        'SKF':9},
    'SL':{
        'CM':1,
        'HB5':4,
        'SL':20},
    'SME':{
        'CM':1,
        'HB1':10,
        'STO':2,
        'SME':20},
    'SPF':{
        'CM':1,
        'HB4':3,
        'HBL':3,
        'SPF':9},
    'SPP':{
        'CM':1,
        'HB3':3,
        'HB4':2,
        'STO':2,
        'SPP':6},
    'TNP':{
        'CM':1,
        'HB3':9,
        'STO':1,
        'TNP':11},
    'UPF':{
        'CM':1,
        'HB1':2,
        'HB2':4,
        'STO':3,
        'UPF':7},
    'WEL':{
        'CM':1,
        'HB1':12,
        'STO':2,
        'WEL':17},
    'WPL':{
        'CM':1,
        'HB2':7,
        'STO':2,
        'WPL':9}
}

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
            combos[combo] = combos[combo] * area_multiple
           
        # adding combos
        full_dict_building_arrays[bui]['combos'] = combos
    
    # adding planner bui counts
    full_dict_building_arrays['planner'] = planner_bui_count()

    return full_dict_building_arrays
        