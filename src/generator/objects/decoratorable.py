from typing import List

from .decorator import Decorator


class Decoratorable:
    def __init__(self) -> None:
        self.decorators: List[Decorator] = []

    def add_decorator(self, decorator: Decorator):
        self.decorators.append(decorator)
