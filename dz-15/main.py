"""
This module to test create homework and output results 
"""


from person import Person
import unit_test_framework as utf
from employee import Employee
from teacher import Teacher
from homework import Homework
from student import Student
from prettytable import PrettyTable
from table import Table
from course import Course


school = [
            Student("Ivan 1", 15, 0), 
            Student("Ivan 2", 25, 0), 
            Student("Ivan 3", 15, 0),
            Student("Petr", 18, 1),
            Student("Sergey", 22, 1)]

hw1 = Homework("OOP intorduction", "Extend logic for Student program", 2, False)
hw2 = Homework("Python web", "Extend logic for Student program", 2, False)


table = Table(name="Intro Python")

for st in school:
    st.add_homework(hw1)
    st.add_homework(hw2)
    table.add_student(st)


# valera = Student("Valera", 15, 0)
# valera.add_homework(hw1)

# print(valera)
# print(valera.homeworks)

print(table.get_summary_table())