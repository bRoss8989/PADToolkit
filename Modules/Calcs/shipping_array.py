from multiprocessing import Pool
import pandas as pd
import numpy as np
from Modules.Transformers.abc_planet_system_keygen import abc_key
from GlobalVars import global_planets_withcx

import Modules.Calcs.Shipping

def bp_array_insert(row, col, start, dest):
    val = Modules.Calcs.Shipping.shipping_optimizer_emptyback('HCB', 20000, start, dest)
    val = val.iloc[0]['empty back cost']
    return [row,col,val]

def shipping_array(output='np'):    

    ## creates array with 0 vals
    arr = np.zeros((4161, 4161), dtype=np.float32)

    ## creates a list of lists for the minimum runs needed
    row = 0
    col = 0
    pool_list = []
    unique_dict = {}
    for y in global_planets_withcx:
        for x in global_planets_withcx:
            if x == y:
                pass
            else:
                key = abc_key(x,y)
                unique_dict[key] = [row,col,x,y]
            col = col + 1
        row = row + 1
        col = 0
    for item in unique_dict:
        pool_list.append(unique_dict[item])
        
    ## runs the shipping calc for each list item
    with Pool() as p:
        final_list = p.starmap(bp_array_insert,pool_list)

    ## inserts the starmap output into original array
    for x in final_list:
        row = x[0]
        col = x[1]
        val = x[2]
        arr[row,col] = val
        arr[col,row] = val

    ## returns numpy or pandas
    if output == 'pd':
        df = pd.DataFrame(arr, index=global_planets_withcx, columns=global_planets_withcx)
        return df
    else:
        return arr
        