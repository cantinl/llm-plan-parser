import re

from .base import PluginBase

class RegexCheck(PluginBase):

    error_template = "The line '{}' is incorrectly formatted."
    default_regex = r"\s*\(\s*([\w-]+\s+)*\w+\s*\)\s*"

    def __init__(self, regex_pattern=None):
        if regex_pattern is None:
            regex_pattern = self.default_regex
        self.pattern = re.compile(regex_pattern)

    def validate(self, domain_file, problem_file, description, plan_file):
        
        with open(plan_file) as f:
            plan = f.read()

        for line in plan.split('\n'):
            if self.pattern.fullmatch(line) is None:
                if line.strip() == '' or line.strip()[0] == ';':
                    continue
                else:
                    return False, self.error_template.format(line.strip())
        return True, None


