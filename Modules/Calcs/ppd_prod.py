import numpy as np
from Modules.FIO.FioAllPlanetsDict import FioNaturalPlanets
from GlobalVars import global_planets, default_prod_buildings, planner

planets_data = FioNaturalPlanets()


def fert__multiplier_array():
    fert_list = []
    for planet in global_planets:
        fert = planets_data[planet]['Fertility']
        if fert == -1:
            fert = 0
        else:
            fert = fert*(10/33) + 1
        fert_list.append(fert)
    return np.array(fert_list)


def bui_multiple_array():
    bui_list = []

    for prod_bui in default_prod_buildings:
        mult = planner[prod_bui][prod_bui]
        bui_list.append(mult)
    return np.array(bui_list)