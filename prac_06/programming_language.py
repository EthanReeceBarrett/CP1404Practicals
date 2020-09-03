"""Intermediate Exercise 1, making a simple class."""


class ProgrammingLanguage:
    """class to store the information of a programing language."""

    def __init__(self, field="", typing="", reflection="", year=""):
        """initialise a programming language instance."""
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """returns output for printing"""
        return "{}, {} typing, reflection = {}, First appeared in 1991".format(self.field, self.typing, self.reflection,
                                                                               self.year)

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False
