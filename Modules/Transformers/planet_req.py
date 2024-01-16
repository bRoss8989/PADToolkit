from Modules.Transformers.StaticPlanetRequirements import build_requirements_dict
from GlobalVars import req_hash

build_req = build_requirements_dict()

def planet_req():

    combos = {}
    for planet in build_req:
        startingval = 1
        for mat in build_req[planet]:
            startingval = startingval * req_hash[mat]
        combos[planet] = startingval
    return combos