import unit_test_framework as utf
from homework import Homework
from student import Student
from school_exceptions import HomeworkException
from school_exceptions import HomeworkStatusException

class StudentTest:

    def __init__(self):
        self.test_name = "test_name"
        self.test_age = "99"
        self.test_grade = 650
        self.test_student = Student("", 0, 0)

    def StudentTestSetUp(self):
        self.test_student = Student(self.test_name, self.test_age, self.test_grade)

    def Student_Name_Test_1(self):
        self.StudentTestSetUp()
        actual = self.test_student.name
        expected = self.test_name
        utf.ExpectEqual(actual, expected)

    def Student_Age_Test_1(self):
        self.StudentTestSetUp()
        actual = self.test_student.age
        expected = self.test_age
        utf.ExpectEqual(actual, expected)

    def Student_Grade_Test_1(self):
        self.StudentTestSetUp()
        actual = self.test_student.grade
        expected = self.test_grade
        utf.ExpectEqual(actual, expected)

    def Student_AddHomework_Test_1(self):
        self.StudentTestSetUp()
        self.test_student.add_homework(Homework("", "", 0, 0))
        actual = len(self.test_student.homeworks)
        expected = 1
        utf.ExpectEqual(actual, expected)

    def Student_AddHomework_Test_2(self):
        self.StudentTestSetUp()
        self.test_student.add_homework(Homework("", "", 0, 0))
        self.test_student.add_homework(Homework("", "", 0, 0))
        self.test_student.add_homework(Homework("", "", 0, 0))
        actual = len(self.test_student.homeworks)
        expected = 3
        utf.ExpectEqual(actual, expected)

    def Student_AddHomework_Test_3(self):
        self.StudentTestSetUp()
        actual = len(self.test_student.homeworks)
        expected = 0
        utf.ExpectEqual(actual, expected)

    def Student_AddHomework_Exception_Test_1(self):
        self.StudentTestSetUp()
        def block():
            self.test_student.add_homework(Homework("", "", 0, True))
        utf.ExpectThrown(block, HomeworkStatusException())

    def Student_is_homework_done_Exception_test(self):
        self.StudentTestSetUp()
        def block():
            self.test_student.is_homework_done()
        utf.ExpectThrown(block, HomeworkException())

    #######################


    def Student_AddHomework_ExpectNotThrown_test(self):
        self.StudentTestSetUp()
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
student_test.Student_is_homework_done_Exception_test()

student_test.Student_AddHomework_ExpectNotThrown_test()