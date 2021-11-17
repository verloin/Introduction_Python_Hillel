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

    __slots__ = ('_name', '_age')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return f"Name: {self._name}\nage: {self._age}"

    def __repr__(self):
        return f"Name: {self._name}"

