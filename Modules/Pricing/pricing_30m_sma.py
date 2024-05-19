from Modules.FIO.FioPull import FIO_PULL

import pandas as pd
from datetime import timedelta

def pricing_sma(ticker, xx='NC1'):

    data = FIO_PULL('exchange/cxpc/'+ticker+'.'+xx)

    test_dict = {}
    for item in data:
        key = item['Interval']
    
        if key not in test_dict.keys():
            test_dict[key] = 0
    
        test_dict[key] = test_dict[key] + 1

    df = pd.DataFrame(data)
    df['avg_price'] = df['Volume'] / df['Traded']
    
    # renaming for use with prophet
    df.rename(columns={"DateEpochMs": "ds", "Traded": "y"})

    df_filtered = df[df['Interval'] == 'MINUTE_THIRTY']
    df_filtered = df_filtered.rename(columns={"DateEpochMs": "ds", "Traded": "y"})
    df_filtered['ds'] = df_filtered['ds'] /1000
    df_filtered['ds'] = pd.to_datetime(df_filtered['ds'], unit='s')
    try:
        days = df_filtered['ds'].max() - df_filtered['ds'].min()
        days = days.total_seconds() / 86400
    except:
        days = 1

    return [(df_filtered['avg_price'] * df_filtered['y']).sum() / df_filtered['y'].sum(), df_filtered['y'].sum(), days]