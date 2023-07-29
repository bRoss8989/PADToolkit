import subprocess
import json
from CommonPaths import base_dir

def JumpList():
    jumplist = subprocess.run(['python3',base_dir+'/JumpCalc.py'],capture_output=True)
    return json.loads(jumplist.stdout)

def JumpDict():
    jump_list = JumpList()
    jump_dict = {}
    
    for pair in jump_list:
        jump_dict[pair[0]] = [pair[1],pair[2]]

    return jump_dict