from Modules.Storage.StoreMongo import StoreMongo
from Modules.Transformers.StaticRecipes import StaticRecipes
from Modules.Transformers.T2_StaticRecipeOutputs import T2_StaticRecipeOutputs

def StaticDataCreate(version):

    # tier 1

    fio_recipes = StaticRecipes()

    # tier 2 (dependant on t1)

    outputs = T2_StaticRecipeOutputs(fio_recipes)

    # write to mongo

    StoreMongo('PAD',1, version, {'recipes':fio_recipes,
                                 'recipe_outputs':outputs})
    