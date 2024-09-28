from typing import List


def pascal_to_camel_case(st: str):
    return st[0].lower() + st[1:]


size = 2


def __get_indent(indentation: int):
    return " " * size * indentation


def generate_indented(indent: int, lines: List[str]):
    indented_lines = [__get_indent(indent) + line for line in lines]

    return indented_lines


def generate_str_from_lines(lines: List[str]):
    return "\n".join(lines)
