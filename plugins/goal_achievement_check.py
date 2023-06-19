import re

from .base import PluginBase

import subprocess

class GoalAchievementCheck(PluginBase):

    def __init__(self):
        self.pattern = re.compile(r'\(\s*([\w-]+).*\)')

    def run_val(self, domain_file, problem_file, plan_file, verbose=False):
        # Run the val command and capture the output
        command = f"~/.planutils/packages/val/bin/Validate {'-v ' if verbose else ''} {domain_file} {problem_file} {plan_file}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Return the result
        return result.stdout

    def validate(self, domain_file, problem_file, description, plan_file):
        
        result = self.run_val(domain_file, problem_file, plan_file)
        if 'Plan valid' in result:
            return True, None

        else:
            result = self.run_val(domain_file, problem_file, 'sas_plan.1', verbose=True)
            lines = result.split('\n')
            index = lines.index('Plan failed because of unsatisfied precondition in:')

            return False, lines[index] + ' ' + lines[index + 1]
