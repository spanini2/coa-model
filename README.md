# Course-of-Action Preliminary Viability Study - Using LLMs to generate unit movement

## Setup Environment

Create and activate a python virtual environment with Python 3.9

Then install all required modules by running:

```
pip install -r requirements.txt
```

## Running 

First create a Hugging Face account and setup a user access token in order to access Gemma 2 (https://huggingface.co/docs/hub/security-tokens)



Then run the following:

```bash
export OUTPUT_DIR=path/to/your/output/file
export NUM_TRIALS=[number of trials]
export GPUS=[CUDA numbers of gpus (i.e 4,5)]

python eval.py --output_dir=$OUTPUT_DIR --num_trials=$NUM_TRIALS --gpus=GPUS
```

## Postprocess

The following checks the recall of the model (whether or not the model hallucinates values between the input json and the model output) and the accuracy of the movements outlined in the CoA (whether or not the model asks grounded units to cross the river)

```bash
export OUTPUT_DIR=path/to/your/output/file
export INPUT_DIR=path/to/your/input/file

python postproc.py --output_dir=$OUTPUT_DIR --input_dir=$INPUT_DIR
```
Then run the following to print out the

ID RECALL PERCENTAGE,

TYPE RECALL PERCENTAGE,

ALLIANCE RECALL PERCENTAGE,

POSITION RECALL PERCENTAGE,

VALID MOVEMENT PERCENTAGE

```bash
export INPUT_DIR=path/to/your/input/file

python stat.py --input_dir=$INPUT_DIR
```

## Visualization

Create visualization of model generated CoAs by running

```bash
export OUTPUT_DIR=path/to/your/output/file
export INPUT_DIR=path/to/your/input/file

python visual.py --output_dir=$OUTPUT_DIR --input_dir=$INPUT_DIR
```

## Examples

Example model outputs, a postprocess file and visuals are in the output/20_units folder

