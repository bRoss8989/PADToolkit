import numpy as np
import math
from multiprocessing import Pool
from Modules.Transformers.StaticBuildingArrays import full_dict_build_arrays
from Modules.Transformers.planet_req import planet_req
from Modules.Calcs.ppd_functions import dw_model_fromppd, ppd_from_dw_model, days_peramount
from GlobalVars import global_planets, default_buildreq_ppd, default_foodreq_ppd, default_buildings, default_prod_buildings


full_dictbui = full_dict_build_arrays()
planet_req_dict = planet_req()
req_combos = (34, 102, 170, 221, 2431, 114, 190, 2, 10, 38, 6, 714, 13, 42, 798, 247)

def daily_repair_cost(total_mat, days_since_build=89):
    return (total_mat - math.floor(total_mat * ((180 - min(days_since_build, 180)) / 180)))*(1/days_since_build)

def amortization(total_mat, amort_days=180):
    return total_mat * (1/amort_days)

base_amor = np.vectorize(amortization)
base_repair = np.vectorize(daily_repair_cost)

base_price = 50000 / np.array(default_buildreq_ppd, dtype=np.float32)
food_price = 50000 / np.array(default_foodreq_ppd, dtype=np.float32)



def operating_cost_by_baseday(building, days_since_build=89, amort_days=180):

    # start with food cost since it's the same amounts for every planet
    food = full_dictbui[building]['foodreq_array']
    index = default_buildings.index(building)
    plan = full_dictbui['planner'][building]
    food_multiple = plan[index] 
    plan = plan[:, np.newaxis]
    food_total = food * food_multiple
    food_cost_by_baseday = np.sum(food_price * food_total, axis=0)
    #temp_food_price = dw_model_fromppd(500.3118542313757,food_price, 70)
    #temp_base_price = dw_model_fromppd(500.3118542313757,base_price, 70)
    #food_cost_by_baseday = np.sum(temp_food_price * food_total, axis=0)

    hash_dict = {}
    
    for hash in req_combos:
        stacked_list = []
        for bui in default_buildings:  
            core = full_dictbui[bui]['buildreq_array']
            extra = full_dictbui[bui]['combos'][hash]
            complete = core + extra
            stacked_list.append(complete)
        stacked_array = np.vstack(stacked_list)

        full_stack = stacked_array*plan
        base_total = np.sum(full_stack, axis=0)

        amor = base_amor(base_total) 
        repair = base_repair(base_total)

        base_quant = amor + repair

        base_cost_by_baseday = np.sum(base_price* base_quant, axis=0)
        
        #base_cost_by_baseday = np.sum(temp_base_price * base_quant, axis=0)

        hash_dict[hash] = base_cost_by_baseday + food_cost_by_baseday

    final_list = []
    
    for planet in global_planets:
        planet_hash = planet_req_dict[planet]
        final_list.append(hash_dict[planet_hash])

    return np.array(final_list, dtype=np.float32)


def operating_cost_by_building():

    temp_list = []
    for x in default_prod_buildings:
        temp_list.append([x])

    with Pool() as p:
        return p.starmap(operating_cost_by_baseday, temp_list)
