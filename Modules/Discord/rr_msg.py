import pandas as pd
from datetime import datetime
import pytz
from Modules.FIO.FioPull import FIO_PULL

def base_pull(name,planet):
    return FIO_PULL('/Storage/'+name+'/'+planet)

def mat_count(full_base, ticker):
    item_count = 0

    try:
        for mat in full_base['StorageItems']:
            if mat['MaterialTicker'] == ticker:
                item_count = item_count + mat['MaterialAmount']
    except:
        item_count = 0
        
    return item_count

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

def base_summary(persons, planet, items, burn):
    dict = {}

    for person in persons:
        
        temp_inv = []
        full_base = base_pull(person, planet)
        if full_base == 'no content' or full_base == None :
            continue

        days_since = day_frac(full_base['Timestamp'])
    
        if days_since > 16:
            continue
        
        for item in items:
            temp_inv.append(round(mat_count(full_base, item) + (days_since * burn[planet][item])) )
    
        dict[person] = temp_inv
    return dict

def rr_msg():

    persons = ['MemoryAlpha', 'Aeper', 'roganartu','FUC_Prozer','xflqr_']
    planet = 'VH-778b'
    items = ['H', 'HE3', 'FF']
    burn = {
        'VH-778b': {
            'H': -556.4,
            'HE3': -278.2,
            'FF': 13910},
        'VH-043e': {
            'HE3': 332.37},
        'VH-331i': {
            'H': 1547.32}
    }
    
    summary = base_summary(persons, planet, items, burn) 
    
    df_vh778 = pd.DataFrame.from_dict(summary,orient = 'index', columns=items)
    
    persons = ['MemoryAlpha', 'Paris_In_Springtime', 'FUC_Prozer', 'Septin']
    planet = 'VH-043e'
    items = ['HE3']
    
    summary = base_summary(persons, planet, items, burn) 
    
    df_vh043 = pd.DataFrame.from_dict(summary,orient = 'index', columns=items)
    
    persons = ['xflqr_', 'Jacchus']
    planet = 'VH-331i'
    items = ['H']
    
    summary = base_summary(persons, planet, items, burn) 
    
    df_hydron = pd.DataFrame.from_dict(summary,orient = 'index', columns=items)
    
    return df_vh778, df_vh043, df_hydron
