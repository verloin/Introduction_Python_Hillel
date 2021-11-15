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

    __slots__ = ('name', 'description', 'students', 'teacher', 'start_date', 'end_date', 'count_lessons')

    def __init__(self, name, description, students, teacher, start_date, end_date, count_lessons):
        self.__name = name
        self.__description = description
        self.__students = students
        self.__teacher = teacher
        self.__start_date = start_date
        self.__end_date = end_date
        self.__count_lessons = count_lessons

    def __str__(self):
        return super().__str__() + f"\nname: {self.name}"

    def __repr__(self):
        return f"Name: {self._name}"