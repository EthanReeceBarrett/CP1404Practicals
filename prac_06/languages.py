"""file used to test programming_language class."""

from prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    field_list = [ruby, python, visual_basic]
    print("the dynamically typed languages are:")
    for field in field_list:
        if field.is_dynamic():
            print(field.field)


main()
