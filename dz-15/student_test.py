"""
This module contain class StudentTest for testing by creation object of student

methods:
    StudentTestSetUp
    Student_Name_Test_1 
    Student_Age_Test_1 
    Student_Grade_Test_1
    Student_AddHomework_Test_1
    Student_AddHomework_Test_2
    Student_AddHomework_Test_3
    Student_AddHomework_Exception_Test_1
    Student_is_homework_done_Exception_test_1
    Student_AddHomework_ExpectNotThrown_test_1
"""


import unit_test_framework as utf
from homework import Homework
from student import Student
from school_exceptions import HomeworkException
from school_exceptions import HomeworkStatusException

class StudentTest:
    """
    This class for testing data from creating of object student
    """

    __slots__ = ('__test_name', '__test_age', '__test_grade', 'test_student')

    def __init__(self):
        self.__test_name = "test_name"
        self.__test_age = "99"
        self.__test_grade = 650
        self.test_student = Student("", 0, 0)

    def __StudentTestSetUp(self):
        """ This method needed for transfer data of Student to variable """

        self.test_student = Student(self.__test_name, self.__test_age, self.__test_grade)

    def Student_Name_Test_1(self):
        """ This module needed for testing  of naming by object student """

        self.__StudentTestSetUp()
        actual = self.test_student._name
        expected = self.__test_name
        utf.ExpectEqual(actual, expected)

    def Student_Age_Test_1(self):
        """ This module needed for testing the age of object student """

        self.__StudentTestSetUp()
        actual = self.test_student._age
        expected = self.__test_age
        utf.ExpectEqual(actual, expected)

    def Student_Grade_Test_1(self):
        """ This module needed for testing the grade of object student """

        self.__StudentTestSetUp()
        actual = self.test_student._grade
        expected = self.__test_grade
        utf.ExpectEqual(actual, expected)

    def Student_AddHomework_Test_1(self):
        """ This module needed for testing is homework added to student """

        self.__StudentTestSetUp()
        self.test_student.add_homework(Homework("", "", 0, 0))
        actual = len(self.test_student._homeworks)
        expected = 1
        utf.ExpectEqual(actual, expected)

    def Student_AddHomework_Test_2(self):
        """ This module needed for testing is homework added to student """

        self.__StudentTestSetUp()
        self.test_student.add_homework(Homework("", "", 0, 0))
        self.test_student.add_homework(Homework("", "", 0, 0))
        self.test_student.add_homework(Homework("", "", 0, 0))
        actual = len(self.test_student._homeworks)
        expected = 3
        utf.ExpectEqual(actual, expected)

    def Student_AddHomework_Test_3(self):
        """ This module needed for testing is homework added to student """

        self.__StudentTestSetUp()
        actual = len(self.test_student._homeworks)
        expected = 0
        utf.ExpectEqual(actual, expected)

    def Student_AddHomework_Exception_Test_1(self):
        """ This module needed for testing is exceptions of homework added to student """

        self.__StudentTestSetUp()
        def block():
            self.test_student.add_homework(Homework("", "", 0, True))
        utf.ExpectThrown(block, HomeworkStatusException())

    def Student_is_homework_done_Exception_test_1(self):
        """ This module needed for testing exceptions is the student's homework done """

        self.__StudentTestSetUp()
        def block():
            self.test_student.is_homework_done()
        utf.ExpectThrown(block, HomeworkException())

    #######################


    def Student_AddHomework_ExpectNotThrown_test_1(self):
        """ This module needed for testing is exceptions of homework added to student """
        
        self.__StudentTestSetUp()
        def block():
            self.test_student.add_homework(Homework("", "", 0, False))
        utf.ExpectNotThrown(block)


#######################

student_test = StudentTest()

student_test.Student_AddHomework_Test_1()
student_test.Student_AddHomework_Test_2()
student_test.Student_AddHomework_Test_3()
student_test.Student_Name_Test_1()
student_test.Student_Age_Test_1()
student_test.Student_Grade_Test_1()
student_test.Student_AddHomework_Exception_Test_1()
student_test.Student_is_homework_done_Exception_test_1()

student_test.Student_AddHomework_ExpectNotThrown_test_1()