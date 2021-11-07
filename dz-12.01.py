# pip install prettytable
# from prettytable import PrettyTable

# resultTable = PrettyTable()


class Homework:
    def __init__(self, name, description, complexity, status):
        self.name = name
        self.description = description
        self.complexity = complexity
        self.status = status

    def __repr__(self):
        return f"{self.name} | {self.status}"


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.subscribed_courses = []
        self.homeworks = {}

    def __repr__(self):
        return f"{self.name} | {self.age} | {self.homeworks}"

    def add_homework(self, hw_number, homework):
        self.homeworks[hw_number] = homework

    def is_homework_done(self, hw_number):
        if len(self.homeworks) == 0:
            raise Exception("Homeworks is empty")
        current_hw = self.homeworks.get(hw_number)
        if current_hw:
            return current_hw.status
        return Exception("No such homework")

    def change_homework_status(self, hw_number, status=True):
        current_hw = self.homeworks.get(hw_number)
        if current_hw:
            current_hw.status = status
            return current_hw
        return Exception("No such homework")


class Table:
    def __init__(self, name):
        self.name = name
        self.students = []

    def __str__(self):
        return self.name

    def add_student(self, student_obj):
        self.students.append(student_obj)

    def get_summary(self):
        summary = []
        for student in self.students:
            summary.append(
                [
                    student.name,
                    student.age,
                    student.grade,
                    student.subscribed_courses,
                    student.homeworks,
                ]
            )
        return summary


school = [Student("Ivan", 25, 0), 
          Student("Ivan 2", 35, 0), 
          Student("Ivan 3", 35, 0)
          ]

hw1 = Homework("OOP intorduction", "Extend logic for Student program", 2, False)
hw2 = Homework("Python web", "Extend logic for Student program", 2, False)

table = Table(name="Intro Python")
# table_b = Table(name="Python web")

for student in school:
    student.add_homework(1, hw1)
    student.add_homework(2, hw2)
    table.add_student(student)


summary = table.get_summary()
for item in summary:
    print(item)


