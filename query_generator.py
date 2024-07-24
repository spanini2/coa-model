import random

class QueryGenerator:
    def __init__(self, input_seed=5514) -> None:
        self.unit_types = ["Armor", "Artillery", "Aviation"]
        random.seed(input_seed)
            
    def generate_troops(self, num_troops=20):
        troops = []
        for id in range(int(num_troops//2)):
            troops.append({
                'unit_id': id+1,
                'unit_type': self.unit_types[random.randint(0, 2)],
                'alliance' : 'Friendly',
                'position' : {
                    'x' : random.randint(0, 90),
                    'y' : random.randint(0, 200)
                }
            })
        for id in range(num_troops - int(num_troops//2)):
            troops.append({
                'unit_id': id+num_troops - int(num_troops/2)+1,
                'unit_type': self.unit_types[random.randint(0, 2)],
                'alliance' : 'Hostile',
                'position' : {
                    'x' : random.randint(105, 200),
                    'y' : random.randint(0, 200)
                }
            })
        return troops