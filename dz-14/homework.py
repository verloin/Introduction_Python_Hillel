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

    def __init__(self, name, description, complexity, status):
        self.name = 'name'
        self.description = 'description'
        self.complexity = 0
        self.status = status