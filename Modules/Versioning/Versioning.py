

def PAD_Version(Version_List):            #0 Starting_PAD 1 Static 2 COG 3 COG_Miss 4 Outputs 5 Base_Amort 6 Ship_daily_Cost 7 Available_Ship_type 8 Natural_Planets
    PAD_Key = 'PAD_'
    for item in Version_List:
        PAD_Key = PAD_Key+'V'+str(item)
    return PAD_Key+'V'

def PAD_Version_Check(RunKey,RunVar):
    
    Var_Positions = []
    
    for var in range(len(RunKey)):
        if RunKey[var] == 'V':
            Var_Positions.append(var)
            
    Start = Var_Positions[RunVar]
    End = Var_Positions[RunVar+1]
    RunVar_Version = RunKey[Start+1:End]
    
    return RunVar_Version