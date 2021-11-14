"""
This module contains two functions for sorting students

Functions:
    sort_students_by_age: This function needed for sorting students by age
    sort_students_by_grade: This function needed for sorting students by grade
Returns:
    sort_students_by_age
    sort_students_by_age        
"""


import unit_test_framework as utf


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
    """
    This function needed for sorting students by age

    Args:
        students: passes the list of students to sort
    Returns:
        students: returns a list of sorted students by age
    """

    students.sort(key=lambda i: i[1])
    return students


def sort_students_by_grade(students):
    """
    This function needed for sorting students by grade

    Args:
        students: passes the list of students to sort
    Returns:
        students: returns a list of sorted students by grade
    """

    students.sort(key=lambda i: i[2])
    return students

sort_students_by_age(test_students)
sort_students_by_grade(test_students)

def helper_tests():
    """
    This function needed for testing functions
    """

    utf.ExpectEqual(sort_students_by_age(test_students), sorted_students_age)
    utf.ExpectEqual(sort_students_by_grade(test_students), sorted_students_grade)

helper_tests()


