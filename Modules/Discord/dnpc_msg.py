import pandas as pd
from datetime import datetime
import pytz
import gspread
from Modules.FIO.FioPull import FIO_PULL
from Modules.Discord.livedata_defs import base_summary

gc = gspread.service_account(filename='Data/aa_livedata.json')
spreadsheet = gc.open("AluminiumAllianceLiveData")
worksheet = spreadsheet.worksheet("DNPC")




def dnpc_msg():

    data = worksheet.get_all_records()
    df = pd.DataFrame(data)

    inv_dict = {}
    site_dict = {}

    planet = 'ZV-759c'
    items = ['ALO', 'O', 'C']
    project = 'DEIMOS-SUPPLY'
    
    summary, inv_dict, site_dict = base_summary(planet, items, project, df, inv_dict, site_dict) 
    
    df_ZV759c = pd.DataFrame.from_dict(summary,orient = 'index', columns=items)

    planet = 'ZV-194a'
    items = ['AL', 'LST']
    project = 'NIKE-SUPPLY'
    
    summary, inv_dict, site_dict = base_summary(planet, items, project, df, inv_dict, site_dict)
    
    df_ZV194a = pd.DataFrame.from_dict(summary,orient = 'index', columns=items)

    planet = 'ZV-759c'
    items = ['AL', 'ALO', 'O', 'C']
    project = 'DEIMOS-PROD'


    summary, inv_dict, site_dict = base_summary(planet, items, project, df, inv_dict, site_dict) 
    
    df2_ZV759c = pd.DataFrame.from_dict(summary,orient = 'index', columns=items)

    planet = 'ZV-194a'
    items = ['BBH', 'BSE', 'AL', 'LST']
    project = 'NIKE-PROD'
    
    summary, inv_dict, site_dict = base_summary(planet, items, project, df, inv_dict, site_dict) 
    
    df2_ZV194a = pd.DataFrame.from_dict(summary,orient = 'index', columns=items)
    
    return df_ZV759c, df_ZV194a, df2_ZV759c, df2_ZV194a