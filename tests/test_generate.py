import os
from src.generator.generator.generate import (
    generate_attribute,
    generate_class,
    generate_file,
    generate_method,
    generate_method_parameter,
)
from src.generator.objects.attribute import Attribute
from src.generator.objects.cls import ClassType
from src.generator.objects.decorator import Decorator
from src.generator.objects.access_modifier import AccessModifier
from src.generator.objects.file import File
from src.generator.objects.method import Method
from src.generator.objects.method_params import MethodParameter
from src.generator.builder.class_builder import ClassBuilder


class TestGenerateMethod:
    def test_generate_method_parameter(self):
        assert (
            generate_method_parameter(MethodParameter("AbcLolol"))
            == "AbcLolol abcLolol"
        )

    def test_generate_method_parameter_with_decorator(self):
        m = MethodParameter("AbcLolol")
        m.add_decorator(Decorator("name", {"lala": "lolo", "decor1": "decor_val"}))
        assert (
            generate_method_parameter(m)
            == "@name(lala = lolo, decor1 = decor_val) AbcLolol abcLolol"
        )

    def test_generate_method(self):
        params = []
        m = Method(AccessModifier.PUBLIC, "blalala", "BigInteger", params)
        assert generate_method(m) == """public BigInteger blalala() {\n\n}"""

    def test_generate_method_with_indentation_and_decorator(self):
        params = []
        m = Method(AccessModifier.PUBLIC, "blalala", "BigInteger", params)
        m.set_indent(2)
        m.add_decorator(Decorator("DecoratorName", {}))
        assert (
            generate_method(m)
            == """    @DecoratorName\n    public BigInteger blalala() {\n    \n    }"""
        )

    def test_generate_attribute(self):
        attr = Attribute("attributeA", "BigInteger")
        assert generate_attribute(attr) == "BigInteger attributeA;"

    def test_generate_attribute_with_decorator(self):
        attr = Attribute("attributeA", "BigInteger")
        attr.add_decorator(Decorator("DecoratorName", {}))
        assert generate_attribute(attr) == "@DecoratorName\nBigInteger attributeA;"

    def test_generate_attribute_with_decorator_indented(self):
        attr = Attribute("attributeA", "BigInteger")
        attr.add_decorator(Decorator("DecoratorName", {}))
        attr.set_indent(1)
        assert generate_attribute(attr) == "  @DecoratorName\n  BigInteger attributeA;"

    def test_generate_class(self):
        cls = ClassBuilder().add_name("ClassName").build()

        assert generate_class(cls) == "class ClassName {\n\n}"

    def test_generate_class_with_method(self):
        cls = (
            ClassBuilder()
            .add_name("ClassName")
            .add_method(
                Method(
                    AccessModifier.PUBLIC,
                    "blala",
                    "BigInteger",
                    [MethodParameter("Param1")],
                )
            )
            .add_method(
                Method(
                    AccessModifier.PUBLIC,
                    "blala",
                    "BigInteger",
                    [MethodParameter("Param1")],
                )
            )
            .add_attribute(Attribute("attrName", "BigInteger", AccessModifier.PRIVATE))
            .build()
        )

        assert (
            generate_class(cls)
            == "class ClassName {\n\n  private BigInteger attrName;\n\n  public BigInteger blala(Param1 param1) {\n  \n  }\n\n  public BigInteger blala(Param1 param1) {\n  \n  }\n\n}"
        )

    def test_generate_interface(self):
        interface = (
            ClassBuilder()
            .set_class_type(ClassType.INTERFACE)
            .add_name("BigInteger")
            .build()
        )

        assert generate_class(interface) == "interface BigInteger {\n\n}"

    def test_generate_interface_with_decorator(self):
        m = Method(
            AccessModifier.PUBLIC, "method1", "BigInteger", [MethodParameter("Integer")]
        )
        m.add_decorator(Decorator("Override", {}))
        interface = (
            ClassBuilder()
            .set_class_type(ClassType.INTERFACE)
            .add_decorator(
                Decorator("SpringBootTest", {"classes": "Configuration.class"})
            )
            .add_method(m)
            .add_name("BigInteger")
            .build()
        )

        assert (
            generate_class(interface)
            == "@SpringBootTest(classes = Configuration.class)\ninterface BigInteger {\n\n  @Override\n  public BigInteger method1(Integer integer) {\n  \n  }\n\n}"
        )

    def test_generate_file(self):
        cls = ClassBuilder().add_name("BigInteger").build()
        f = File(cls, "./aa")
        try:
            generate_file(f)
            with open("./aa/BigInteger.java") as f:
                result = []
                for row in f:
                    result.append(row)

                assert "".join(result) == "class BigInteger {\n\n}"
        finally:
            try:
                os.remove("./aa/BigInteger.java")
                os.rmdir("./aa")
            except Exception as ex:
                print(f"Exception encountered {ex}")
