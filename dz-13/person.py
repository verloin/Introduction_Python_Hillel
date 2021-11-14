"""
This module contain class Person
"""


class Person:
    """
    class Person creates object person

    Args:
        name:  This arg needed for naming a new object of person
        age:  This arg needed for indication of age a new object of person
    Returns:
        name:  name person
        age:  age person
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}\nage: {self.age}"
