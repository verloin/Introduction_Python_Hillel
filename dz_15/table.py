"""
This module contain class Table

Mothods:
    add_student
    get_summary_table
"""


from prettytable import PrettyTable

from teacher import Teacher
from course import Course


resultTable = PrettyTable()


class Table:
    """
    This class creates instance of table contain students

    Arg: name:  This arg for naming object table
    Returns:
        name:  returns naming object table
        resultTable:  returns table of students
    """

    __slots__ = ('name', 'students')

    def __init__(self, name):
        self.name = name
        self.students = []
        # self.courses = Teacher.courses

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"\nname: {self.name}"

    def add_student(self, student_obj):
        """
        This method for add student to list of students
        Args: student_obj:  for indication student for add to list
        """

        self.students.append(student_obj)


    def get_summary_table(self):
        """
        This method for output of summary data in the form table
        Returns: resultTable: result table students
        """

        resultTable.field_names = [
            "Name",
            "Age",
            "Grade",
            "Teacher",
            "Subscribed courses",
            "Homeworks",
        ]
        for student in self.students:
            resultTable.add_row(
                [
                    student._name,
                    student._age,
                    student._grade,
                    student.teacher,
                    student._subscribed_courses,
                    student._homeworks,
                ]
            )
        return resultTable
