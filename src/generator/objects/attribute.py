from typing import List

from .indentable import Indentable
from .access_modifier import AccessModifier

from .decoratorable import Decoratorable


class Attribute(Decoratorable, Indentable):
    def __init__(
        self, name: str, type: str, access_modifier: AccessModifier | None = None
    ) -> None:
        Indentable.__init__(self)
        Decoratorable.__init__(self)
        self.name = name
        self.type = type
        self.access_modifier = access_modifier
