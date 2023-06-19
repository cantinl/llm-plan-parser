
# LLM Planning Parser

TODO: Add project description.

## Components
### Planner / NL Converter
The script `generate_plans.sh` generates plans for all the domain/problems in a folder. It also generates natural language descriptions of those plans by using the `convert.py` script. To tailor the script to your domain, edit the `translation_dict` dictionary, where the keys are the action names and the values are format strings describing the action.

Example usage: `./generate_plans.sh data/domains/blocksworld`

### Parser / corrective re-prompter
The script `main.py` runs a parser on a natural language description of the plan and generates a PDDL plan. The plan then goes through a series of plugins to assess the quality of the plan. Plugins can be found in the `plugins/` folder. The current plugins are:
1. Regex check: makes sure the plan is in the correct format
2. Action symbol check: makes sure all the action symbols exist in the domain file
3. Object check: makes sure all the actions exist inthe problem file
4. Parameter check: makes sure all the parameters are of the correct type and quantity
5. Goal achievement check: makes sure that the plan achieves the goal

TODO: when there is an error, prompt the LLM to fix the plan. Not implemented yet.

Sample command to run the script:
`python3 main.py data/domains/blocksworld domain.pddl p06.pddl p06.steps`