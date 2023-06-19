from abc import ABC, abstractmethod

class PluginBase(ABC):

    @abstractmethod
    def validate(self, domain_file, problem_file, description, plan_file):
        pass