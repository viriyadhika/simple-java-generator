import os
from typing import List

from src.generator.generator.utils import (
    generate_indented,
    generate_str_from_lines,
    pascal_to_camel_case,
)
from src.generator.objects.attribute import Attribute
from src.generator.objects.cls import Class
from src.generator.objects.decorator import Decorator
from src.generator.objects.file import File
from src.generator.objects.method import Method
from src.generator.objects.method_params import MethodParameter


def generate_decorator(decorator: Decorator):
    if isinstance(decorator.parameters, List):
        return "@" + decorator.name + "(" + ", ".join(decorator.parameters) + ")"

    if len(decorator.parameters) == 0:
        return "@" + decorator.name

    parameter_val: List[str] = []
    for param_key, param_value in decorator.parameters.items():
        parameter_val.append(param_key + " = " + param_value)

    return "@" + decorator.name + "(" + ", ".join(parameter_val) + ")"


def generate_method_parameter(method_parameter: MethodParameter):
    formatted = []
    for decor in method_parameter.decorators:
        formatted.append(generate_decorator(decor))

    return (
        "".join(formatted)
        + (" " if len(formatted) > 0 else "")
        + method_parameter.class_name
        + " "
        + pascal_to_camel_case(method_parameter.class_name)
    )


def __generate_method_lines(method: Method):
    formatted_params = [
        generate_method_parameter(parameter) for parameter in method.parameters
    ]

    lines = []
    for decorator in method.decorators:
        lines.append(generate_decorator(decorator))

    lines.append(
        method.access_modifier.value
        + " "
        + method.return_type
        + " "
        + method.name
        + "("
        + ", ".join(formatted_params)
        + ") "
        + "{"
    )
    if len(method.body) == 0:
        lines.append("")
    else:
        for body_line in generate_indented(1, method.body):
            lines.append(body_line)

    lines.append("}")

    return generate_indented(method.indentation, lines)


def generate_method(method: Method):
    return generate_str_from_lines(__generate_method_lines(method))


def __generate_attribute_lines(attribute: Attribute):
    lines = []

    for decorator in attribute.decorators:
        lines.append(generate_decorator(decorator))

    lines.append(
        (
            attribute.access_modifier.value + " "
            if attribute.access_modifier is not None
            else ""
        )
        + attribute.type
        + " "
        + attribute.name
        + ";"
    )

    return generate_indented(attribute.indentation, lines)


def generate_attribute(attribute: Attribute):
    return generate_str_from_lines(__generate_attribute_lines(attribute))


def _generate_class_header(cls: Class):
    line = "public " + cls.cls_type.value + " " + cls.name + " "
    if cls.extended_class != None:
        line += f"extends {cls.extended_class} "
    if len(cls.implemented_interfaces) > 0:
        line += f"implements {','.join(cls.implemented_interfaces)} "

    line += "{"
    return line


def generate_class(cls: Class):
    lines = []

    for decorator in cls.decorators:
        lines.append(generate_decorator(decorator))

    lines.append(_generate_class_header(cls))
    lines.append("")

    for attribute in cls.attribute:
        attribute.set_indent(1)
        for line in __generate_attribute_lines(attribute):
            lines.append(line)
        lines.append("")

    for method in cls.method:
        method.set_indent(1)
        for line in __generate_method_lines(method):
            lines.append(line)
        lines.append("")

    lines.append("}")

    return generate_str_from_lines(lines)


def generate_file(f: File):
    if not os.path.exists(f.path):
        os.mkdir(f.path)

    with open(os.path.join(f.path, f.cls.name + ".java"), "w") as file:
        lines = []
        if len(f.import_statements) > 0:
            lines.append("\n".join(f.import_statements))
            lines.append("")

        lines.append(generate_class(f.cls))
        file.write(generate_str_from_lines(lines))
