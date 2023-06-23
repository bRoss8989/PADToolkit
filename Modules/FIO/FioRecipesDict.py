from Modules.FIO.FioPull import FIO_PULL

def FioRecipesDict():

    recipes_list = FIO_PULL('/recipes/allrecipes')

    recipes_dict = {}

    for fiorecipe in recipes_list:        

        recipe = fiorecipe['RecipeName']
        
        if recipe == '=>':
            continue
        
        recipes_dict[recipe] = fiorecipe
        

    return recipes_dict