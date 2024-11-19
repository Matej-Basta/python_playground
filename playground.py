from abc import ABC, abstractmethod
from math import sqrt 

class AbstractComponent(ABC):
    @abstractmethod
    def execute(self, number: int) -> bool:
        pass

class AbstractDecorator(AbstractComponent):
    def __init__(self, component: AbstractComponent) -> None:
        self._decorated = component

class PrimeDeterminingComponent(AbstractComponent):
    def execute(self, number: int) -> bool:
        if number < 2:
            return False
        elif number == 2:
            return True
        for i in range(2, int(sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True

class ConcreteDecorator(AbstractDecorator):
    def execute(self, number: int) -> bool:
        print("my decorator running")
        result = self._decorated.execute(number)
        print(f"The result is {result}")
        print("my decorator stopping")

component = PrimeDeterminingComponent()
decorator = ConcreteDecorator(component)
decorator.execute(9)