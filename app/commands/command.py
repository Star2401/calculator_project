from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, a, b): 
        # Execute the command with two operands.
        pass

