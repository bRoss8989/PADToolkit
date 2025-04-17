import pandas as pd
from datetime import datetime
import pytz
from Modules.FIO.FioPull import FIO_PULL



def base_pull(name,planet):
    return FIO_PULL('/Storage/'+name+'/'+planet)

def store_pull(name, inv_dict, site_dict):    
    inv_dict[name] = FIO_PULL('/Storage/'+name)
    site_dict[name] = FIO_PULL('/sites/warehouses/'+name)
    return inv_dict, site_dict
    

def mat_count(full_base, ticker):
    item_count = 0

    try:
        for mat in full_base['StorageItems']:
            if mat['MaterialTicker'] == ticker:
                item_count = item_count + mat['MaterialAmount']
    except:
        item_count = 0
        
    return item_count

def wh_count(name, item, planet, inv_dict, site_dict):

    #pull the full inv for warehouse storage if it's not already pulled
    if name not in inv_dict.keys():
       inv_dict, site_dict = store_pull(name, inv_dict, site_dict)

    #checks if auth error and returns 0
    if site_dict[name] == 'repeating auth error':
        return 0

    # get the store id for the warehouse
    site_code = None
    for ware in site_dict[name]:
        if ware['LocationNaturalId'] == planet:
            site_code = ware['StoreId']
            

    # get the item quantity from the warehouse
    for storage in inv_dict[name]:
        if storage['StorageId'] == site_code:
            for mat in storage['StorageItems']:
                if mat['MaterialTicker'] == item:
                    ware_items = mat['MaterialAmount']
    # return the amount unless there is no warehouse or item
    try:
        return ware_items
    except:
        return 0
    
    

def iso_delta_clip(delta):
    delta = str(delta)
    delta =  delta.split('.')[0]
    return datetime.fromisoformat(delta).replace(tzinfo=pytz.utc)

def day_frac(start):
    
    start = iso_delta_clip(start)
    current  = iso_delta_clip(datetime.now(pytz.utc))
    
    iso_delta = current - start
    
    return (iso_delta.days
            + iso_delta.seconds / 86400)

def burn_from_df(person,project,item, df):
    
    condition1 = (df['Key1'] == project)
    condition2 = (df['Key2'] == person)
    
    return df.loc[condition1 & condition2,item].sum()

def base_summary(planet, items, project, df, inv_dict, site_dict):
    dict = {}

    persons = df[df["Key1"] == project]["Key2"].tolist()

    for person in persons:

        if person == 'placeholder':
            continue
        
        temp_inv = []
        full_base = base_pull(person, planet)
        
        if full_base == 'no content' or full_base == None or full_base == 'repeating auth error':
            full_base = 0

        try:
            days_since = day_frac(full_base['Timestamp'])
        except:
            days_since = 0
            
        if days_since > 16:
            continue
        
        for item in items:
            try:
                burn = burn_from_df(person,project,item, df)
                burn = float(burn)
                if isinstance(burn, (int, float)) == False:
                    temp_inv.append(0)
                    continue
            except:
                temp_inv.append(0)
                continue
            try:
                base_mats= mat_count(full_base, item)
            except:
                base_mats = 0
            temp_inv.append(round(base_mats + (days_since * burn)) + wh_count(person, item, planet, inv_dict, site_dict) )
    
        dict[person] = temp_inv
    return dict, inv_dict, site_dict