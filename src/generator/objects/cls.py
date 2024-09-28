from enum import Enum
from typing import List

from .decoratorable import Decoratorable
from .attribute import Attribute
from .method import Method


class ClassType(Enum):
    CLASS = "class"
    INTERFACE = "interface"


class Class(Decoratorable):
    def __init__(self, name: str, cls_type: ClassType = ClassType.CLASS) -> None:
        super().__init__()
        self.cls_type = cls_type
        self.attribute: List[Attribute] = []
        self.method: List[Method] = []
        self.name = name

    def add_method(self, method: Method):
        self.method.append(method)

    def add_attribute(self, attribute: Attribute):
        self.attribute.append(attribute)
