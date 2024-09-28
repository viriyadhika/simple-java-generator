from typing import List

from src.generator.objects.cls import Class


class File:
    def __init__(self, cls: Class, path: str) -> None:
        self.cls = cls
        self.path = path
        self.import_statements: List[str] = []

    def add_import_statement(self, package_to_import: str):
        self.import_statements.append(package_to_import)
