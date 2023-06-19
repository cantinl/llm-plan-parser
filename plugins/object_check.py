import pddl
import re

from .base import PluginBase

class ObjectCheck(PluginBase):

    error_template = "The object {} is not declared in the problem file."

    def __init__(self):
        self.pattern = re.compile(r'\(\s*[\w-]+(.*)\)')

    def validate(self, domain_file, problem_file, description, plan_file):
        
        problem = pddl.parse_problem(problem_file)
        valid_objects = set(obj.name for obj in problem.objects)
        with open(plan_file) as f:
            plan = f.read()

        for line in plan.split('\n'):
            match_result = self.pattern.match(line)
            if match_result:
                parameters = match_result.group(1).split(' ')
                parameters = filter(lambda x: x != '', parameters)
                for obj in parameters:
                    if obj not in valid_objects:
                        return False, self.error_template.format(obj)
        return True, None
