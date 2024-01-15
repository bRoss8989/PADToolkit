from Modules.Transformers.StaticRecipes import StaticRecipes
from Modules.Transformers.T2_StaticRecipeOutputs import T2_StaticRecipeOutputs

recipes = StaticRecipes()
recipe_outputs = T2_StaticRecipeOutputs(recipes)

#creates two dicts with all the mats as keys
#recipe_outputs has a list of all the recipes for each output and a list of all the inputs for every recipe
output_list = {}
pending_outputs = {}
for output in recipe_outputs:
    output_list[output] = None
    pending_outputs[output] = None


# removes mats from pending_outputs as all the inputs for each recipe are met
# ending dict is the order in which all recipes can be co-processed without any inputs not being met by the output mat
# RE items and NA have no inputs

def recipe_order():
    count = 0
    recipe_order = {}
    
    while len(pending_outputs) != None:
        temp_list = []
        
        for output in pending_outputs:
            check = 1
            
            if recipe_outputs[output][1] == []:
                temp_list.append(output)
                continue
                
            for mat in recipe_outputs[output][1]:
                if mat in pending_outputs.keys():
                    check =  0
            if check == 1:
                temp_list.append(output)
                
        if temp_list == []:
            break
    
        recipe_order[count] = []
        for item in temp_list:
            recipe_order[count].append(item)
    
        for item in temp_list:
            del(pending_outputs[item])
        count = count + 1
    
    return recipe_order