from typing import Dict


class Decorator:
    def __init__(self, name: str, parameters: Dict[str, str]) -> None:
        self.name = name
        self.parameters = parameters
