import validation
import argparse
import os
import validation
import glob
import json



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", default="/home/salban/CoA/simulation/output/20_units")
    parser.add_argument("--output_dir", default="/home/salban/CoA/simulation/output/20_units/20_units_post", type=str)
    args = parser.parse_args()
    input_list=list(glob.glob(os.path.join(args.input_dir, "generated_plan_*")))

    final_output_arr=[]

    for file in input_list:
        field = validation.BattlefieldValidation(file)
        
        output = field.get_model_output()
        input = field.get_initial_positions()
        field.check_metadata()
        output_dict={"input_file" : file}
        output_dict['p_id'] = field.p_id
        output_dict['p_type'] = field.p_type
        output_dict['p_alliance'] = field.p_alliance
        output_dict['p_pos'] = field.p_pos
        field.check_movement()
        output_dict["movement_check_arr"] = field.movement_check_arr
        final_output_arr.append(output_dict)
        print(final_output_arr)
    
    with open(os.path.join(args.output_dir, "post.json"), 'w') as f:
                json.dump(final_output_arr, f, indent=4)


    

