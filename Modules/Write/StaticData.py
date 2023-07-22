from Modules.Storage.StoreMongo import StoreMongo
from Modules.Write.StaticRecipes import StaticRecipes
from Modules.Write.StaticT2RecipeOutputs import StaticT2RecipeOutputs

def StaticDataCreate(version):

    # tier 1

    fio_recipes = StaticRecipes()

    # tier 2 (dependant on t1)

    outputs = StaticT2RecipeOutputs(fio_recipes)

    # write to mongo

    StoreMongo('PAD',1, version, {'recipes':fio_recipes,
                                 'recipe_outputs':outputs})
    