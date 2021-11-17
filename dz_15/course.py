"""
class Course need for creating course for student
"""

class Course:
    """
    Args:
        name: title course
        description: for description course
        students: for indication what course is for whom 
        teacher: who is leading the course
        start_date: start date course
        end_date: end date course
        count_lessons: count courses in course
    """

    __slots__ = ('_name', '_description', '_students', '_teacher', '_start_date', '_end_date', '_count_lessons')

    def __init__(self, name, description, students, teacher, start_date, end_date, count_lessons):
        self._name = name
        self._description = description
        self._students = students
        self._teacher = teacher
        self._start_date = start_date
        self._end_date = end_date
        self._count_lessons = count_lessons

    def __str__(self):
        return super().__str__() + f"\nname: {self._name}" + f"\ndescription: {self._description}"

    def __repr__(self):
        return f"Name: {self._name}"