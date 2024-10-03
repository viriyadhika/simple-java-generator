from typing import Dict, List


class Decorator:
    def __init__(self, name: str, parameters: Dict[str, str] | List[str]) -> None:
        self.name = name
        self.parameters = parameters
