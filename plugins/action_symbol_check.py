import pddl
import re

from .base import PluginBase

class ActionSymbolCheck(PluginBase):

    error_template = "The action {} is not valid in the supplied domain."

    def __init__(self):
        self.pattern = re.compile(r'\(\s*([\w-]+).*\)')

    def validate(self, domain_file, problem_file, description, plan_file):
        
        domain = pddl.parse_domain(domain_file)
        valid_actions = set(action.name for action in domain.actions)
        with open(plan_file) as f:
            plan = f.read()

        for line in plan.split('\n'):
            match_result = self.pattern.match(line)
            if match_result:
                action_name = match_result.group(1)
                if not action_name in valid_actions:
                    return False, self.error_template.format(line.strip())
        return True, None


