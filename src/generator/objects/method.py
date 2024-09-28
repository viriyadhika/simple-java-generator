from enum import Enum
from typing import List

from src.generator.objects.access_modifier import AccessModifier

from .indentable import Indentable
from .decoratorable import Decoratorable
from .method_params import MethodParameter


class Method(Decoratorable, Indentable):
    def __init__(
        self,
        access_modifier: AccessModifier,
        name: str,
        return_type: str,
        parameters: List[MethodParameter],
    ) -> None:
        Decoratorable.__init__(self)
        Indentable.__init__(self)
        self.access_modifier = access_modifier
        self.name = name
        self.return_type = return_type
        self.parameters = parameters
