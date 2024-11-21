from abc import ABC, abstractmethod
import functools
import logging
from math import sqrt
import time
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
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.warning(f"The function {func.__name__} has following positional arguments: {args}.")
        logger.warning(f"The function {func.__name__} has following keyword arguments: {kwargs}.")
        value = func(*args, **kwargs)
        return value

    return wrapper

def measure_execution_time(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        time_diff = end_time - start_time
        logger.warning(f"The function {func.__name__} took {time_diff} seconds.")
        return value

    return wrapper

@log_arguments_and_return_value
@measure_execution_time
def add_numbers(num1: int, num2: int) -> int:
    return num1 + num2

@log_arguments_and_return_value
@measure_execution_time
def greet() -> str:
    return "Hello world!"

@log_arguments_and_return_value
@measure_execution_time
def say_name(name="name", surname="surname"):
    return f"I am {name} {surname}. Nice to meet you."

if __name__ == "__main__":
    def main():
        print(add_numbers(3, 7))
        print(greet())
        print(say_name(name="Foo", surname="Bar"))


    main()
