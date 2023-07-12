from Modules.FIO.FioRecipesDict import FioRecipesDict
from Modules.FIO.FioMaterialsDict import FioMaterialsDict
from Modules.Storage.StoreMongo import StoreMongo

def StaticRecipes(version):
    fio_recipes = FioRecipesDict()
    fio_mat = FioMaterialsDict()
    re = ['minerals','gases','ores','liquids']
    
    for key, value in fio_mat.items():
        if value['CategoryName'] in re:
            fio_recipes['=>'+key] = {'RecipeName': '=>'+key, 'Inputs': [], 'Outputs': [{'Ticker': key, 'Amount': 0}]}
    
    return StoreMongo('PAD',1, version, {'recipes':fio_recipes})
    