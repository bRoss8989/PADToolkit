import pandas as pd
from datetime import datetime
import pytz
import gspread
from Modules.FIO.FioPull import FIO_PULL
from Modules.Discord.livedata_defs import base_summary

gc = gspread.service_account(filename='Data/aa_livedata.json')
spreadsheet = gc.open("AluminiumAllianceLiveData")
worksheet = spreadsheet.worksheet("RRSF")




def sf_msg():

    data = worksheet.get_all_records()
    df = pd.DataFrame(data)

    inv_dict = {}
    site_dict = {}

    planet = 'VH-778b'
    items = ['SF', 'AMM', 'GAL', 'H']
    project = 'Shesmu-PROD'
    
    summary, inv_dict, site_dict = base_summary(planet, items, project, df, inv_dict, site_dict) 
    
    df_vh778b = pd.DataFrame.from_dict(summary,orient = 'index', columns=items)

    planet = 'VH-331f'
    items = ['AMM']
    project = 'ODYSSEUS-PROD'
    
    summary, inv_dict, site_dict = base_summary(planet, items, project, df, inv_dict, site_dict) 
    
    df_vh331f = pd.DataFrame.from_dict(summary,orient = 'index', columns=items)

    planet = 'LB-599a'
    items = ['GAL']
    project = 'LB-599a-PROD'
    
    summary, inv_dict, site_dict = base_summary(planet, items, project, df, inv_dict, site_dict) 
    
    df_lb599a = pd.DataFrame.from_dict(summary,orient = 'index', columns=items)

    planet = 'VH-331i'
    items = ['H']
    project = 'Hydron-PROD'


    summary, inv_dict, site_dict = base_summary(planet, items, project, df, inv_dict, site_dict) 
    
    df_vh331i = pd.DataFrame.from_dict(summary,orient = 'index', columns=items)
    
    
    return df_vh778b, df_vh331f, df_lb599a, df_vh331i