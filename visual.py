import matplotlib
import matplotlib.pyplot as plt
import json
import argparse
import tqdm
import os
from textwrap import wrap

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", default="/home/salban/CoA/simulation/output/20_units", type=str)
    parser.add_argument("--output_dir", default="/home/salban/CoA/simulation/output/20_units/visual", type=str)
    args = parser.parse_args()


    for i in tqdm.trange(100):
        try:
            f = open(os.path.join(args.input_dir, f"generated_plan_{i}.json"))
            resp = json.load(f)


            units = resp['input_locations']
            friendly_aviation = [(unit['unit_id'], unit['position']['x'], unit['position']['y']) for unit in units if unit['alliance'] == 'Friendly' and unit['unit_type'] == 'Aviation']
            friendly_artillery = [(unit['unit_id'], unit['position']['x'], unit['position']['y']) for unit in units if unit['alliance'] == 'Friendly' and unit['unit_type'] == 'Artillery']
            friendly_armor = [(unit['unit_id'], unit['position']['x'], unit['position']['y']) for unit in units if unit['alliance'] == 'Friendly' and unit['unit_type'] == 'Armor']
            hostile_armor = [(unit['unit_id'], unit['position']['x'], unit['position']['y']) for unit in units if unit['alliance'] == 'Hostile' and unit['unit_type'] == 'Armor']
            hostile_artillery = [(unit['unit_id'], unit['position']['x'], unit['position']['y']) for unit in units if unit['alliance'] == 'Hostile' and unit['unit_type'] == 'Artillery']
            hostile_aviation = [(unit['unit_id'], unit['position']['x'], unit['position']['y']) for unit in units if unit['alliance'] == 'Hostile' and unit['unit_type'] == 'Aviation']

            plt.figure(figsize=(12, 12))
            plt.scatter([x for _, x, y in friendly_aviation], [y for _, x, y in friendly_aviation], color='cyan', marker='^', s=100)
            plt.scatter([x for _, x, y in friendly_artillery], [y for _, x, y in friendly_artillery], color='cyan', marker='o', s=100)
            plt.scatter([x for _, x, y in friendly_armor], [y for _, x, y in friendly_armor], color='cyan', marker='s', s=100)
            plt.scatter([x for _, x, y in hostile_armor], [y for _, x, y in hostile_armor], color='lightcoral', marker='s', s=100)
            plt.scatter([x for _, x, y in hostile_artillery], [y for _, x, y in hostile_artillery], color='lightcoral', marker='o', s=100)
            plt.scatter([x for _, x, y in hostile_aviation], [y for _, x, y in hostile_aviation], color='lightcoral', marker='^', s=100)

            for unit in resp['input_locations']:
                plt.annotate(unit['unit_id'], (unit['position']['x'], unit['position']['y']))

            plt.axvline(x=100, color='blue', linestyle='--', linewidth=2)
            plt.plot([98, 102], [150, 150], color='brown', linewidth=8)
            plt.annotate("BRIGE TIGER", (100, 150))
            plt.plot([98, 102], [50, 50], color='brown', linewidth=8)
            plt.annotate("BRIGE LION", (100, 50))

            tasks=[]
            for unit in resp['model_output']['coa_id_0']['task_allocation']:
                tasks.append({"unit_id" : unit['unit_id'],"tasks" : unit['command'].split("; ")})

            for task in tasks:
                unit_id = int(task['unit_id'])
                unit_position=resp['input_locations'][unit_id-1]['position']

                for command in task['tasks']:
                    if 'attack_move_unit' in command:
                        _, x_dest,y_dest=command[command.index("(")+1:command.index(")")].split(", ")
                        x_dest, y_dest = int(x_dest), int(y_dest)
                        plt.arrow(unit_position['x'], unit_position['y'], x_dest - unit_position['x'], y_dest - unit_position['y'], 
                                color='orange', head_width=3, length_includes_head=True)
                        unit_position={'x':x_dest, 'y':y_dest}
                    
                    if 'engage_target_unit' in command:
                        _, target_id =command[command.index("(")+1:command.index(")")].split(", ")
                        target_id = int(target_id)
                        target_position = resp['input_locations'][target_id-1]['position']
                        if target_position:
                            plt.arrow(unit_position['x'], unit_position['y'], target_position['x'] - unit_position['x'], target_position['y'] - unit_position['y'], 
                                    color='purple', head_width=3, length_includes_head=True)
                        unit_position=target_position
                    if 'stand_location' in command:
                        plt.scatter(unit_position['x'], unit_position['y'], color='green', marker="8", s=300, alpha=0.5)

            plt.title("\n"+'\n'.join(wrap(resp['model_output']['coa_id_0']['overview'], 130)))
            plt.xlabel('X Coordinate')
            plt.ylabel('Y Coordinate')
            plt.legend()
            plt.grid(True)
            plt.gca().invert_yaxis()
            plt.show()

            plt.savefig(os.path.join(args.output_dir, f"generated_plan_{i}.png"))
            plt.cla()
        except:
            pass