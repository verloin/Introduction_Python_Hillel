"""
This module contain class Teache which inheritance from class Person
"""


from person import Person
from prettytable import PrettyTable

resultTable = PrettyTable()


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
        return super().__str__() + f"\ncourses: {self.courses}"

    def __repr__(self):
        return f"Score: {self.score}"


    def teacher_add_course(self, course):
        self.courses.append(course)
        

    def get_summary_table_courses(self):
        """
        This method for output of summary data in the form table teachers
        Returns: resultTable: result table teachers
        """

        resultTable.field_names = [
            "Name",
            "Description",
            "Students",
            "Teacher",
            "Start_date",
            "end_date",
            "count_lessons"
        ]
        for course in self.courses:
            resultTable.add_row(
                [
                    course._name,
                    course._description,
                    course._students,
                    course._teacher,
                    course._start_date,
                    course._end_date,
                    course._count_lessons,
                ]
            )
        return resultTable