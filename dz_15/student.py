"""
This module contains class Student 

class Student inherited from Person need for creation object student
Raises:
    HomeworkStatusException
    HomeworkException
"""

from person import Person
from teacher import Teacher
from school_exceptions import HomeworkException, HomeworkStatusException


class Student(Person):
    """
    This class described student and needed for creation object student

    Args:
        name: for naming object student
        age: for indicating age of student
        subscribed_courses: indicates the student's courses
        homeworks: to display the student's homework
    Methods:
        add_homework: This method added homework for student
        is_homework_done: This method for checking whether the work is done
    """

    __slots__ = ('_grade', '_subscribed_courses', '_homeworks', 'teacher')

    def __init__(self, name, age, grade, teacher):
        super().__init__(name, age)
        self._grade = grade
        self._subscribed_courses = []
        self._homeworks = []
        self.teacher = teacher


    def __str__(self):
        return super().__str__() + f"\ngrade: {self._grade}"    

    def __repr__(self):
        return f"\nname: {self.name}"

    def add_homework(self, homework):
        """
        This method added homework to homework collections
        Args: homework
        Raises: HomeworkStatusException
        """

        if homework.status == 1:
            raise HomeworkStatusException("Status for new homework already done.")
        self._homeworks.append(homework)

    def subscribe_on_course(self, course):
        """
        This method added course to subscribed_courses collections
        Args: course
        """

        self._subscribed_courses.append(course)

    def is_homework_done(self):
        """
        This method check homework for srudent
        Raises: HomeworkException
        Returns: homework: returns status homework
        """

        if len(self._homeworks) == 0:
            raise HomeworkException("Homeworks is empty")
        return self.homeworks[0].status
