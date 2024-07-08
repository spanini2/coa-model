import json
from typing import Dict

class BattlefieldValidation:
    def __init__(self, file_name:str) -> None:
        f = open(file_name)
        self.resp = json.load(f)
        self.input=self.get_initial_positions()
        self.output=self.get_model_output()

    def get_model_output(self):
        return self.resp['model_output']
    
    def get_initial_positions(self):
        return self.resp['input_locations']
    
    def extract_positions(self, troops):
        positions = []
        for unit in range(int(len(troops)/2)):
            positions.append(troops[unit]['position'])
        return positions
    
    def check_metadata(self):
        self.p_id=0
        self.p_type=0
        self.p_alliance=0
        self.p_pos=0
        for unit in self.output['coa_id_0']['task_allocation']:
            if (unit['unit_id']==self.input[int(unit['unit_id'])-1]['unit_id']) : self.p_id+=1
            if (unit['unit_type']==self.input[int(unit['unit_id'])-1]['unit_type']) : self.p_type+=1
            if (unit['alliance']==self.input[int(unit['unit_id'])-1]['alliance']) : self.p_alliance+=1
            if (unit['position']==self.input[int(unit['unit_id'])-1]['position']) : self.p_pos+=1
        self.p_id/=len(self.output['coa_id_0']['task_allocation'])
        self.p_type/=len(self.output['coa_id_0']['task_allocation'])
        self.p_alliance/=len(self.output['coa_id_0']['task_allocation'])
        self.p_pos/=len(self.output['coa_id_0']['task_allocation'])
    
    def get_tasks(self):
        tasks=[]
        for unit in self.output['coa_id_0']['task_allocation']:
            tasks.append({"unit_id" : unit['unit_id'],"tasks" : unit['command'].split("; ")})
        return tasks
    
    def check_movement(self):
        self.movement_check_arr=[]
        for index, unit_tasks in enumerate(self.get_tasks()):
            is_valid=True
            location=self.input[index]['position']
            for task in unit_tasks['tasks']:
                if not self.input[int(unit_tasks['unit_id'])-1]['unit_type']=="Aviation":
                    try:
                        if "attack_move_unit" in task:
                            move_location=task[task.index("(")+1:task.index(")")].split(", ")
                            print(move_location)
                            if not self.check_bridge_cross(location, {"x":int(move_location[1]), "y":int(move_location[2])}): is_valid=False
                            location={"x":int(move_location[1]), "y":int(move_location[2])}
                        elif "engage_target_unit" in task:
                            move_location=task[task.index("(")+1:task.index(")")].split(", ")
                            print(move_location)
                            if not self.check_bridge_cross(location, self.input[int(move_location[1])-1]['position']): 
                                is_valid=False
                    except:
                        is_valid=False
            if not is_valid:
                self.movement_check_arr.append(False)
            else:
                self.movement_check_arr.append(True)
        


        return -1

    def check_bridge_cross(self, location1:Dict, location2:Dict) -> bool:
        print(location1, location2)
        x1=location1['x']
        y1=location1['y']
        x2=location2['x']
        y2=location2['y']
        if x2==175 and y2==175 : print("HI")
        if((x1<100 and x2>100) and (x1!=100 and not (y1==50 or y1==150))):
            return False
        return True
