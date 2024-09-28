class Indentable:
    def __init__(self, indentation: int = 0) -> None:
        self.indentation = indentation

    def set_indent(self, indentation: int):
        self.indentation += indentation
