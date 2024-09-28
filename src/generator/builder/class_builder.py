from typing import List
from src.generator.objects.attribute import Attribute
from src.generator.objects.decorator import Decorator
from src.generator.objects.method import Method
from src.generator.objects.cls import Class, ClassType


class ClassBuilder:
    def __init__(self) -> None:
        self.name: str | None = None
        self.cls_type: ClassType = ClassType.CLASS
        self.attributes: List[Attribute] = []
        self.methods: List[Method] = []
        self.decorators: List[Decorator] = []

    def set_class_type(self, cls_type: ClassType):
        self.cls_type = cls_type
        return self

    def add_name(self, name: str):
        self.name = name
        return self

    def add_method(self, method: Method):
        self.methods.append(method)
        return self

    def add_attribute(self, attribute: Attribute):
        self.attributes.append(attribute)
        return self

    def add_decorator(self, decorator: Decorator):
        self.decorators.append(decorator)
        return self

    def build(self):
        if self.name is None:
            raise Exception("Name must be declared")

        cls = Class(self.name, self.cls_type)
        for attribute in self.attributes:
            cls.add_attribute(attribute)
        for decorator in self.decorators:
            cls.add_decorator(decorator)
        for method in self.methods:
            cls.add_method(method)

        return cls
