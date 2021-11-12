import unit_test_framework as utf
# from prettytable import PrettyTable
# from table import Table
# from student import Student
# from homework import Homework



test_students = [
            ['Ivan 11', 10, 10, [], [["OOP intorduction", "Extend logic for Student program", 2, False]]],
            ['Sergey 5', 22, 13, [], [["OOP intorduction", "Extend logic for Student program", 2, False]]],
            ['Ivan 22', 25, 7, [], [["OOP intorduction", "Extend logic for Student program", 2, False]]],
            ['Petr 1', 18, 1, [], [["OOP intorduction", "Extend logic for Student program", 2, False]]],
            ['Ivan 33', 2, 20, [], [["OOP intorduction", "Extend logic for Student program", 2, False]]]
                ]

sorted_students_age = [
            ['Ivan 33', 2, 20, [], [["OOP intorduction", "Extend logic for Student program", 2, False]]],
            ['Ivan 11', 10, 10, [], [["OOP intorduction", "Extend logic for Student program", 2, False]]],
            ['Petr 1', 18, 1, [], [["OOP intorduction", "Extend logic for Student program", 2, False]]],
            ['Sergey 5', 22, 13, [], [["OOP intorduction", "Extend logic for Student program", 2, False]]],
            ['Ivan 22', 25, 7, [], [["OOP intorduction", "Extend logic for Student program", 2, False]]]
                ]

sorted_students_grade = [
            ['Petr 1', 18, 1, [], [["OOP intorduction", "Extend logic for Student program", 2, False]]],
            ['Ivan 22', 25, 7, [], [["OOP intorduction", "Extend logic for Student program", 2, False]]],
            ['Ivan 11', 10, 10, [], [["OOP intorduction", "Extend logic for Student program", 2, False]]],
            ['Sergey 5', 22, 13, [], [["OOP intorduction", "Extend logic for Student program", 2, False]]],
            ['Ivan 33', 2, 20, [], [["OOP intorduction", "Extend logic for Student program", 2, False]]]
                ]


def sort_students_by_age(students):
    students.sort(key=lambda i: i[1])
    return students


def sort_students_by_grade(students):
    students.sort(key=lambda i: i[2])
    return students

sort_students_by_age(test_students)
sort_students_by_grade(test_students)

def helper_tests():
    utf.ExpectEqual(sort_students_by_age(test_students), sorted_students_age)
    utf.ExpectEqual(sort_students_by_grade(test_students), sorted_students_grade)

helper_tests()


