from abc import ABC, abstractmethod
import logging
from math import sqrt
from typing import Any, Callable

logger = logging.getLogger("decorator_logger")

# ============================================ Decorators using classes ============================================

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

# ============================================ Decorators using python syntax ============================================

def log_arguments_and_return_value(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args, **kwargs):
        str_arguments = [str(argument) for argument in args]
        str_k_arguments = [f"{str(key)}={str(value)}" for key, value in kwargs.items()]
        args_log = f"The function has following positional arguments: {(", ").join(str_arguments)}." if len(args) > 0 else "The function has no positional arguments."
        kwargs_log = f"The function has following keyword arguments: {(", ").join(str_k_arguments)}." if len(kwargs) > 0 else "The function has no keyword arguments."
        logger.warning(args_log)
        logger.warning(kwargs_log)
        value = func(*args, **kwargs)
        return value

    return wrapper

@log_arguments_and_return_value
def add_numbers(num1: int, num2: int) -> int:
    return num1 + num2

@log_arguments_and_return_value
def greet() -> str:
    return "Hello world!"

@log_arguments_and_return_value
def say_name(name="name", surname="surname"):
    return f"I am {name} {surname}. Nice to meet you."

if __name__ == "__main__":
    def main():
        print(add_numbers(3, 7))
        print(greet())
        print(say_name(name="Foo", surname="Bar"))


    main()
