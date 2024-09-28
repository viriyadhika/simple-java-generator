from .decoratorable import Decoratorable


class MethodParameter(Decoratorable):
    def __init__(self, class_name: str) -> None:
        super().__init__()
        self.class_name = class_name
