"""
This module contains class Homework, it's needed for creation object homework 
"""


class Homework:
    """
    Needed for creation object homework 
    Args:
        name:  This arg needed for naming of created homework
        description:  This arg needed for description of created homework
        complexity:  This arg needed for specifying complexity of created homework
        status:  This arg needed for specifying status of created homework
    """

    __slots__ = ('name', 'description', 'complexity', 'status')

    def __init__(self, name, description, complexity, status):
        self.name = name
        self.description = description
        self.complexity = complexity
        self.status = status

    def __str__(self):
        return super().__str__() + f"\nname: {self.name}"

    def __repr__(self):
        return f"\nname: {self.name}"