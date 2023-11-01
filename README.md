# GPT Competency Experiments


## Running Instructions
In order to run any of the top level directories on a 

## Directories

- **3.5turbo** is the directory with all of the ChatGPT generated code for this experiment.
- **humanCode** is the directory with all of the human-written code for this experiment
- **Datasets** directory is all of the testing data that we 
- **analysis** contain various figures used when studying the programs that were produced.
- **data** contains some of the final and most important csv files used to compare the code produced.

## Top Level Files
- **generate.py** generates the GPT code by parsing the prompts listed in the ideas.md file. This is how the `3.5turbo` directory and its subdirectories were generated.
- **ideas.md** lists all of the prompts given to both the humans and chatgpt, 
as well as the sources of the ideas if they were retrieved online, 
and the sources of code in the `humanCode` directory if it was retrieved online.
- **metrics.py** used to generate either the `humanCode` directory, or the `3.5turbo` directories for the complexity and other measures we used in our study.
- **prediction_model.ipynb** the code for the model used to predict if a piece of code was written by chatGPT or by a human.
