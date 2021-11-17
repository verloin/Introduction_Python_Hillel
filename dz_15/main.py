"""
This module to test create homework and output results 
"""


# from person import Person
# import unit_tests.unit_test_framework as utf
# from employee import Employee
from teacher import Teacher
from homework import Homework
from student import Student
# from prettytable import PrettyTable
from table import Table
from course import Course


hw1 = Homework("OOP introduction", "Extend logic for Student program", 2, False)
hw2 = Homework("Python web", "Extend logic for Student program", 2, False)

course1 = Course('Python Introduction', 'base Python', 'valera,Petr', 'Teacher 1', '01.01', '10.01', '16')
course2 = Course('Python Advanced', 'middle Python', 'Sergey, ivan 2', 'Teacher 1', '01.01', '10.01', '32')

table = Table(name="Intro Python")
teacher1 = Teacher('Teacher1', '41')
teacher2 = Teacher('Teacher2', '11')

teacher1.teacher_add_course(course1)
teacher1.teacher_add_course(course2)


school = [
            Student("Ivan 1", 15, 0, teacher2), 
            Student("Ivan 2", 25, 0, teacher2), 
            Student("Ivan 3", 15, 0, teacher1),
            Student("Sergey", 22, 1, teacher2)]


for st in school:
    st.add_homework(hw1)
    st.add_homework(hw2)
    table.add_student(st)
    st.subscribe_on_course(course1)


petr = Student("Petr", 18, 1, teacher1)
petr.add_homework(hw1)
table.add_student(petr)


valera = Student("Valera", 15, 0, teacher1)
valera.add_homework(hw1)
table.add_student(valera)


print(table.get_summary_table())
print(teacher1.get_summary_table_courses())