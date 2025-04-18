import pandas as pd
from datetime import datetime
import pytz
import gspread
from Modules.FIO.FioPull import FIO_PULL
from Modules.Discord.livedata_defs import base_summary

gc = gspread.service_account(filename='Data/aa_livedata.json')
spreadsheet = gc.open("AluminiumAllianceLiveData")
worksheet = spreadsheet.worksheet("RR")




def rr_msg():

    data = worksheet.get_all_records()
    df = pd.DataFrame(data)

    inv_dict = {}
    site_dict = {}
    
    planet = 'VH-778b'
    items = ['H', 'HE3', 'FF']
    project = 'Shesmu-PROD'
    
    summary, inv_dict, site_dict = base_summary(planet, items, project, df, inv_dict, site_dict) 
    
    df_vh778 = pd.DataFrame.from_dict(summary,orient = 'index', columns=items)
    
    planet = 'VH-043e'
    items = ['HE3']
    project = 'Rathar-PROD'
    
    summary, inv_dict, site_dict = base_summary(planet, items, project, df, inv_dict, site_dict) 
    
    df_vh043 = pd.DataFrame.from_dict(summary,orient = 'index', columns=items)
    
    planet = 'VH-331i'
    items = ['H']
    project = 'Hydron-PROD'
    
    summary, inv_dict, site_dict = base_summary(planet, items, project, df, inv_dict, site_dict) 
    
    df_hydron = pd.DataFrame.from_dict(summary,orient = 'index', columns=items)
    
    return df_vh778, df_vh043, df_hydron
