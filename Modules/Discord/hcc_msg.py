import pandas as pd
from datetime import datetime
import pytz
import gspread
from Modules.FIO.FioPull import FIO_PULL
from Modules.Discord.livedata_defs import base_summary

gc = gspread.service_account(filename='Data/aa_livedata.json')
spreadsheet = gc.open("AluminiumAllianceLiveData")
worksheet = spreadsheet.worksheet("HCC")




def hcc_msg():

    data = worksheet.get_all_records()
    df = pd.DataFrame(data)

    inv_dict = {}
    site_dict = {}

    planet = 'FK-794b'
    items = ['H2O']
    project = 'BOUCHER-PROD'
    
    summary, inv_dict, site_dict = base_summary(planet, items, project, df, inv_dict, site_dict) 
    
    df_fk794b = pd.DataFrame.from_dict(summary,orient = 'index', columns=items)

    planet = 'FK-794c'
    items = ['H2O', 'CAF']
    project = 'FK-794c-SUPPLY'
    
    summary, inv_dict, site_dict = base_summary(planet, items, project, df, inv_dict, site_dict) 
    
    df_fk794c = pd.DataFrame.from_dict(summary,orient = 'index', columns=items)

    planet = 'FK-794d'
    items = ['H2O', 'CAF', 'NS']
    project = 'FK-794d-SUPPLY'
    
    summary, inv_dict, site_dict = base_summary(planet, items, project, df, inv_dict, site_dict) 
    
    df_fk794d = pd.DataFrame.from_dict(summary,orient = 'index', columns=items)

    planet = 'HRT'
    items = ['H2O']
    project = 'HRT-SUPPLY'


    summary, inv_dict, site_dict = base_summary(planet, items, project, df, inv_dict, site_dict) 
    
    df_HRT = pd.DataFrame.from_dict(summary,orient = 'index', columns=items)

    planet = 'VH-331g'
    items = ['H2O', 'HER', 'HOP', 'AMM']
    project = 'AVALON-SUPPLY'
    
    summary, inv_dict, site_dict = base_summary(planet, items, project, df, inv_dict, site_dict)  
    
    df_vh331g = pd.DataFrame.from_dict(summary,orient = 'index', columns=items)

    planet = 'VH-331a'
    items = ['H2O', 'NS', 'DDT']
    project = 'PROMITOR-SUPPLY'
    
    summary, inv_dict, site_dict = base_summary(planet, items, project, df, inv_dict, site_dict)  
    
    df_vh331a = pd.DataFrame.from_dict(summary,orient = 'index', columns=items)
    
    
    return df_fk794b, df_fk794c, df_fk794d, df_HRT, df_vh331g, df_vh331a