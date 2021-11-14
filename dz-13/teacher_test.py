"""
This method contain class TeacherTest
Methods:
    TeacherTestSetUp
    Teacher_Name_Test
    Teacher_Age_Test
    Teacher_Score_Test
    Teacher_Courses_Test
"""


import unit_test_framework as utf
from teacher import Teacher  


class TeacherTest:
    """
    This class for testing of creation object teacher
    Args:
        test_name:  This arg needed for naming a new object
        test_age:  This arg needed for specifying age of object teacher
        test_score:  This arg needed for specifying score
        test_courses:  This arg needed for specifying courses by teacher
        test_teacher:  This arg needed for creation of test object Teacher
    """

    def __init__(self):
        self.test_name = "test_name"
        self.test_age = "99"
        self.test_score = '0'
        self.test_courses = []
        self.test_teacher = Teacher("", "")


    def TeacherTestSetUp(self):
        """
        This method needed for transfer data of homework to variable
        """

        self.test_teacher = Teacher(self.test_name, self.test_age)

    def Teacher_Name_Test(self):
        """
        This method needed for testing of naming name teacher
        """

        self.TeacherTestSetUp()
        actual = self.test_teacher.name
        expected = self.test_name
        utf.ExpectEqual(actual, expected)

    def Teacher_Age_Test(self):
        """
        This method is needed for testing creation age of teacher
        """

        self.TeacherTestSetUp()
        actual = self.test_teacher.age
        expected = self.test_age
        utf.ExpectEqual(actual, expected)

    def Teacher_Score_Test(self):
        """
        This method is needed for testing score of teacher
        """

        self.TeacherTestSetUp()
        actual = self.test_teacher.score
        expected = self.test_score
        utf.ExpectEqual(actual, expected)

    def Teacher_Courses_Test(self):
        """
        This method for testing of available courses with a teacher
        """

        self.TeacherTestSetUp()
        actual = self.test_teacher.courses
        expected = self.test_courses
        utf.ExpectEqual(actual, expected)


#######################

teacher_test = TeacherTest()

teacher_test.Teacher_Name_Test()
teacher_test.Teacher_Age_Test()
teacher_test.Teacher_Score_Test()
teacher_test.Teacher_Courses_Test()