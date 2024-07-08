import argparse
import agents
import os
import prompts
import query_generator
from tqdm import tqdm
import json
from datetime import datetime

class Executor():
    """Loads COA queries and stores responses"""
    def __init__(self) -> None:
        os.environ["CUDA_VISIBLE_DEVICES"] = args.gpus # GPU(s) that the model will load on to/forward pass
        self.agent=agents.GemmaAgent()
        self.qgenerator=query_generator.QueryGenerator()
        self.num_trials=args.num_trials

    def evaluate(self):
        """Loads COA queries and stores responses"""
        for trial in tqdm(range(self.num_trials)):
            output_file = os.path.join(args.output_dir, f'generated_plan_{trial}.json')

            output_dict={"model_name" : "gemma2:27b-instruct"}

            #generate and store randomized queries
            troops = self.qgenerator.generate_troops() 
            output_dict["input_locations"]=troops

            #convert query dict into string from model to parse
            troop_str = json.dumps(troops, indent=4)

            start=datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            response=self.agent.send_query(prompts.coa_agent_prompt.format(locations=troop_str))
            end=datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            output_dict["start"]=start
            output_dict["end"]=end

            response_json = {}

            # formatting gemma responses for in order to go from string -> dict
            response=response[response.index("```json"):]
            response=response.replace("\n", "").replace("```", "").replace("json", "").replace("\"", '"').replace("\t", "").replace("<eos>", "").replace("<end_of_turn>", "")

            print(response)
            try:
                response_json=json.loads(response)
            except:
                pass
            output_dict["model_output"]=response_json
            
            with open(output_file, 'w') as f:
                json.dump(output_dict, f, indent=4)


    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--num_trials", default=1, type=int)
    parser.add_argument("--output_dir", default="/home/salban/CoA/simulation/output/", type=str)
    parser.add_argument("--gpus")
    args = parser.parse_args()

    executor = Executor()
    executor.evaluate()
    