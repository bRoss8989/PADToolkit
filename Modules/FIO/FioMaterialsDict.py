from Modules.FIO.FioPull import FIO_PULL

def FioMaterialsDict():

    materials_list = FIO_PULL('/material/allmaterials')         #re = ['minerals','gases','ores','liquids']

    materials_dict = {}

    for fiomat in materials_list:        

        mat = fiomat['Ticker']

        if mat == 'CMK':
            continue
        
        materials_dict[mat] = fiomat

    ## correcting bad vol and weight data from json pull
    mat_df = FIO_PULL('/csv/materials')

    for mat in materials_dict:
        
        try:
            new_vol = mat_df.loc[mat_df['Ticker'] == mat, 'Volume'].values[0]
            new_weight = mat_df.loc[mat_df['Ticker'] == mat, 'Weight'].values[0]
    
            materials_dict[mat]['Volume'] = new_vol
            materials_dict[mat]['Weight'] = new_weight
        except:
            continue

    return materials_dict