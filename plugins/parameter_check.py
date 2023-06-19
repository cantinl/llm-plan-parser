import pddl
import re

from .base import PluginBase

class ParameterCheck(PluginBase):

    error_template = "Incorrect number of parameters supplied on this line: {}"
    error_template2 = "Wrong argument type on this line: {}"

    def __init__(self):
        self.pattern = re.compile(r'\(\s*([\w-]+)(.*)\)')

    def validate(self, domain_file, problem_file, description, plan_file):
        
        domain = pddl.parse_domain(domain_file)
        problem = pddl.parse_problem(problem_file)
        actions = {
            action.name: action
            for action in domain.actions
        }
        objects = {
            obj.name: obj
            for obj in problem.objects
        }
        with open(plan_file) as f:
            plan = f.read()

        for line in plan.split('\n'):
            match_result = self.pattern.match(line)
            if match_result is None:
                continue

            action_name = match_result.group(1)
            action = actions[action_name]
            parameters = action.parameters
            
            arguments = match_result.group(2).split(' ')
            arguments = [objects[obj_name] for obj_name in arguments if obj_name != '']

            # Check that there are the correct number of parameters
            if len(parameters) != len(arguments):
                return False, self.error_template.format(line)

            # Check that they're the right type
            for param, arg in zip(parameters, arguments):
                param_types, arg_types = param.type_tags, arg.type_tags
                if not param_types.issubset(arg_types):
                    return False, self.error_template2.format(line)
            
        return True, None
