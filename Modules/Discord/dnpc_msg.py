import pandas as pd
from datetime import datetime
import pytz
from Modules.FIO.FioPull import FIO_PULL

df = pd.read_csv('Data/dnpc.csv')

def base_pull(name,planet):
    return FIO_PULL('/Storage/'+name+'/'+planet)

def store_pull(name):    
    inv_dict[name] = FIO_PULL('/Storage/'+name)
    site_dict[name] = FIO_PULL('/sites/warehouses/'+name)
    

def mat_count(full_base, ticker):
    item_count = 0

    try:
        for mat in full_base['StorageItems']:
            if mat['MaterialTicker'] == ticker:
                item_count = item_count + mat['MaterialAmount']
    except:
        item_count = 0
        
    return item_count

def wh_count(name, item, planet):

    #pull the full inv for warehouse storage if it's not already pulled
    if name not in inv_dict.keys():
       store_pull(name)

    #checks if auth error and returns 0
    if site_dict[name] == 'repeating auth error':
        return 0

    # get the store id for the warehouse
    for ware in site_dict[name]:
        if ware['LocationNaturalId'] == planet:
            site_code = ware['StoreId']
        else:
            site_code = None

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

def burn_from_df(person,project,item):
    
    condition1 = (df['Key1'] == project)
    condition2 = (df['Key2'] == person)
    
    return df.loc[condition1 & condition2,item].sum()

def base_summary(persons, planet, items, project):
    dict = {}

    for person in persons:
        
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
            burn = burn_from_df(person,project,item)
            try:
                base_mats= mat_count(full_base, item)
            except:
                base_mats = 0
            temp_inv.append(round(base_mats + (days_since * burn)) + wh_count(person, item, planet) )
    
        dict[person] = temp_inv
    return dict

inv_dict = {}
site_dict = {}

def dnpc_msg():

    persons = ['BoJangles', 'xflqr_', 'Yinxx', 'Septin']
    planet = 'ZV-759c'
    items = ['ALO', 'O', 'C']
    project = 'DEIMOS-SUPPLY'
    
    summary = base_summary(persons, planet, items, project) 
    summary['xflqr_'][0] = 0
    summary['xflqr_'][1] = 0
    
    df_ZV759c = pd.DataFrame.from_dict(summary,orient = 'index', columns=items)

    persons = ['KZ_Kawasaki', 'roganartu', 'kaosaur', 'CptColeslaw', 'australis']
    planet = 'ZV-194a'
    items = ['AL', 'LST']
    project = 'NIKE-SUPPLY'
    
    summary = base_summary(persons, planet, items, project) 
    
    df_ZV194a = pd.DataFrame.from_dict(summary,orient = 'index', columns=items)

    persons = ['australis','CptColeslaw', 'kaosaur', 'roganartu']
    planet = 'ZV-759c'
    items = ['AL', 'ALO', 'O', 'C',]
    project = 'DEIMOS-PROD'


    summary = base_summary(persons, planet, items, project) 
    
    df2_ZV759c = pd.DataFrame.from_dict(summary,orient = 'index', columns=items)

    persons = ['australis', 'Jacchus', 'jvaler', 'Paris_In_Springtime', 'roganartu', 'Yinxx']
    planet = 'ZV-194a'
    items = ['BBH', 'BSE', 'AL', 'LST']
    project = 'NIKE-PROD'
    
    summary = base_summary(persons, planet, items, project) 
    
    df2_ZV194a = pd.DataFrame.from_dict(summary,orient = 'index', columns=items)
    
    return df_ZV759c, df_ZV194a, df2_ZV759c, df2_ZV194a