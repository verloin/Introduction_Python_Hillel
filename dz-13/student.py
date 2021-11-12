from person import Person
from school_exceptions import HomeworkException, HomeworkStatusException
from homework import Homework


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
        self.subscribed_courses = []
        self.homeworks = []

    def __str__(self):
        return super().__str__() + f"\ngrade:{self.grade}"

    def add_homework(self, homework):
        if homework.status == 1:
            raise HomeworkStatusException("Status for new homework already done.")
        self.homeworks.append(homework)

    def is_homework_done(self):
        if len(self.homeworks) == 0:
            raise HomeworkException("Homeworks is empty")
        return self.homeworks[0].status