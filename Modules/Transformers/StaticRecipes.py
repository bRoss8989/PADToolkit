from Modules.FIO.FioRecipesDict import FioRecipesDict
from Modules.FIO.FioMaterialsDict import FioMaterialsDict

def StaticRecipes():
    fio_recipes = FioRecipesDict()
    fio_mat = FioMaterialsDict()
    re = ['minerals','gases','ores','liquids']
    
    for key, value in fio_mat.items():
        if value['CategoryName'] in re:
            fio_recipes['=>'+key] = {'RecipeName': '=>'+key, 'Inputs': [], 'Outputs': [{'Ticker': key, 'Amount': 0}]}

    fio_recipes['2xZIR=>1xZR 2xSIO']['Outputs'] = [{'Ticker': 'ZR', 'Amount': 1},{'Ticker': 'SIO', 'Amount': 2}]
    fio_recipes['2xBER=>1xBE 1xAL 1xSIO']['Outputs'] = [{'Ticker': 'BE', 'Amount': 1}, {'Ticker': 'AL', 'Amount': 1}, {'Ticker': 'SIO', 'Amount': 1}]
    fio_recipes['1xTCO=>1xTC 1xO']['Outputs'] = [{'Ticker': 'TC', 'Amount': 1}, {'Ticker': 'O', 'Amount': 1}]
    fio_recipes['2xTAI=>1xTA 1xFE']['Outputs'] = [{'Ticker': 'TA', 'Amount': 1}, {'Ticker': 'FE', 'Amount': 1}]
    fio_recipes['3xHAL 1xH2O=>2xNA 1xCL']['Outputs'] = [{'Ticker': 'CL', 'Amount': 1}, {'Ticker': 'NA', 'Amount': 2}]
    
    return fio_recipes
    