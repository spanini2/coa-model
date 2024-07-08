import json 
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output_dir", default="/home/salban/CoA/simulation/output/20_units/20_units_post/post.json", type=str)
    args=parser.parse_args()
    post_dict=json.load(open(args.output_dir))
    id_sum=0
    type_sum=0
    alliance_sum=0
    pos_sum=0
    m_amt=0
    m_sum=0
    for trial in post_dict:
        id_sum+=trial['p_id']
        if trial['p_type'] != 1 : print("type", trial['input_file'])
        if trial['p_id'] != 1 : print("id", trial['input_file'])
        if trial['p_pos'] != 1 : print("pos", trial['input_file'])
        if trial['p_alliance'] != 1 : print("alliance", trial['input_file'])
        type_sum+=trial['p_type']
        alliance_sum+=trial['p_alliance']
        pos_sum+=trial['p_pos']
        for i, m in enumerate(trial["movement_check_arr"]):
            m_amt+=1
            if m==True : m_sum+=1
            if not m : print("movement", trial['input_file'] + "  " + str(i))
    print("CORRECT ID RECALL PERCENTAGE", id_sum)
    print("CORRECT TYPE RECALL PERCENTAGE", type_sum)
    print("CORRECT ALLIANCE RECALL PERCENTAGE", alliance_sum)
    print("CORRECT POSITION RECALL PERCENTAGE", pos_sum)
    print("VALID MOVEMENT PERCENTAGE", m_sum/m_amt)