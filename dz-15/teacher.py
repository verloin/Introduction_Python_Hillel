"""
This module contain class Teache which inheritance from class Person
"""


from person import Person

class Teacher(Person):
    """
    class Teacher creates object teacher

    Args:
        name:  This arg needed for naming a new object of teacher
        age:  This arg needed for indication of age a new object of teacher
        score:  This arg needed for indication of scores teacher
        courses:  This arg needed for indication of courses teacher
    Returns:
        score:  score teacher
        courses:  courses teacher
    """

    __slots__ = ('score', 'courses')

    def __init__(self, name, age):
        super().__init__(name, age)
        self.score = '0'
        self.courses = []

    def __str__(self):
        return super().__str__() + f"\nscore: {self.score}" + f"\ncourses: {self.courses}"

    def __repr__(self):
        return f"Score: {self.score}"
