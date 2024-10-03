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
        self.implemented_interfaces: List[str] = []
        self.extended_class: str | None = None

    def add_method(self, method: Method):
        self.method.append(method)

    def add_attribute(self, attribute: Attribute):
        self.attribute.append(attribute)

    def set_extended_class(self, extended_class: str):
        self.extended_class = extended_class

    def add_interface(self, implemented_interface: str):
        self.implemented_interfaces.append(implemented_interface)
