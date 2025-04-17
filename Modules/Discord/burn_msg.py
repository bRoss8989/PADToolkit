import pandas as pd
from datetime import datetime
import pytz
import gspread
from Modules.FIO.FioPull import FIO_PULL
from Modules.Discord.livedata_defs import base_summary

gc = gspread.service_account(filename='Data/aa_livedata.json')
spreadsheet = gc.open("AluminiumAllianceLiveData")
worksheet = spreadsheet.worksheet("BURN")




def burn_msg():

    data = worksheet.get_all_records()
    df = pd.DataFrame(data)

    inv_dict = {}
    site_dict = {}

    planet = 'FK-794b'
    items = ['H2O']
    project = 'Boucher-PROD'
    
    summary, inv_dict, site_dict = base_summary(planet, items, project, df, inv_dict, site_dict) 
    
    df_fk794b = pd.DataFrame.from_dict(summary,orient = 'index', columns=items)

    planet = 'ZV-896c'
    items = ['H2O', 'HCP', 'MAI', 'GRN', 'NS']
    project = 'ZV-896c-PROD'
    
    summary, inv_dict, site_dict = base_summary(planet, items, project, df, inv_dict, site_dict)
    
    df_zv896c = pd.DataFrame.from_dict(summary,orient = 'index', columns=items)

    planet = 'ZV-896b'
    items = ['H2O', 'MAI', 'GRN']
    project = 'Harmonia-PROD'
    
    summary, inv_dict, site_dict = base_summary(planet, items, project, df, inv_dict, site_dict)
    
    df_zv896b = pd.DataFrame.from_dict(summary,orient = 'index', columns=items)

    planet = 'QJ-149c'
    items = ['C', 'HCP', 'MAI', 'GRN']
    project = 'Nascent-PROD'


    summary, inv_dict, site_dict = base_summary(planet, items, project, df, inv_dict, site_dict) 
    
    df_qj149c = pd.DataFrame.from_dict(summary,orient = 'index', columns=items)
    
    
    return df_fk794b, df_zv896c, df_zv896b, df_qj149c