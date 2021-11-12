import unit_test_framework as utf
from teacher import Teacher  


class TeacherTest:

    def __init__(self):
        self.test_name = "test_name"
        self.test_age = "99"
        self.test_score = '0'
        self.test_courses = []
        self.test_teacher = Teacher("", "")


    def TeacherTestSetUp(self):
        self.test_teacher = Teacher(self.test_name, self.test_age)

    def Teacher_Name_Test(self):
        self.TeacherTestSetUp()
        actual = self.test_teacher.name
        expected = self.test_name
        utf.ExpectEqual(actual, expected)

    def Teacher_Age_Test(self):
        self.TeacherTestSetUp()
        actual = self.test_teacher.age
        expected = self.test_age
        utf.ExpectEqual(actual, expected)

    def Teacher_Score_Test(self):
        self.TeacherTestSetUp()
        actual = self.test_teacher.score
        expected = self.test_score
        utf.ExpectEqual(actual, expected)

    def Teacher_Courses_Test(self):
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