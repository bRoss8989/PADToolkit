from Modules.FIO.FioAllPlanetsDict import FioNaturalPlanets

planets = FioNaturalPlanets()

def fio_cogc():

    ## gets first list of most recent cogs
    cogc_dict = {}
    for planet in planets:
        try:
            cogc_list = planets[planet]['COGCPrograms']
            sorted_list = sorted(cogc_list, key=lambda x: x['StartEpochMs'], reverse=True)
            cogc_dict[planet] = [sorted_list[0]['ProgramType'], sorted_list[0]['StartEpochMs']]
        except:
            cogc_dict[planet] = None

    ## removes 3 week old cog and replaces the val with only the program
    highnum = 0
    for planet in cogc_dict:
        try:
            num = cogc_dict[planet][1]
            if num > highnum:
                highnum = num
        except:
            continue
    ## 4 weeks in ms
    cutoff = highnum - 2419200000
    for planet in cogc_dict:
        try:
            if cogc_dict[planet][1] < cutoff:
                cogc_dict[planet] = None
            else:
                cogc_dict[planet] = cogc_dict[planet][0]
        except:
            continue
            
    return cogc_dict