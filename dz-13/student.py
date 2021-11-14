"""
This module contains class Student 

class Student inherited from Person need for creation object student
Raises:
    HomeworkStatusException: [description]
    HomeworkException: [description]
"""

from person import Person
from school_exceptions import HomeworkException, HomeworkStatusException
# from homework import Homework


class Student(Person):
    """
    This class needed for creation object student

    Args:
        name: for naming object student
        age: for indicating age of student
        subscribed_courses: indicates the student's courses
        homeworks: to display the student's homework
    Methods:
        add_homework: This method added homework for student
        is_homework_done: This method for checking whether the work is done
    """
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
        self.subscribed_courses = []
        self.homeworks = []

    def __str__(self):
        return super().__str__() + f"\ngrade:{self.grade}"

    def add_homework(self, homework):
        """
        This method added homework for student
        Args: 
            homework
        Raises: 
            HomeworkStatusException: [description]
        """

        if homework.status == 1:
            raise HomeworkStatusException("Status for new homework already done.")
        self.homeworks.append(homework)

    def is_homework_done(self):
        """
        This method check homework for srudent
        Raises:
            HomeworkException:
        Returns:
            homework: status
        """

        if len(self.homeworks) == 0:
            raise HomeworkException("Homeworks is empty")
        return self.homeworks[0].status

