"""
This module contains class Employee 

class Employee inherited from Person needed for creation of object employee
Returns:
    room: returns room of employee in string format
"""


from person import Person

class Employee(Person):
    """
    This class needed for creation of object employee
    Args:
        Person:
            name: this args is needed for naming object of employee
            age: this args is needed for age of employee
        room: this args is needed for naming room of employee

    Returns:
        room: returns room of employee in string format
    """
    def __init__(self, name, age):
        super().__init__(name, age)
        self.room = 'room'

    def __str__(self):
        return super().__str__() + f"\nroom: {self.room}"