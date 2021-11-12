import unit_test_framework as utf
from homework import Homework


class HomeworkTest:

    def __init__(self):
        self.test_name = 'name'
        self.test_description = 'description'
        self.test_complexity = 0
        self.test_status = True

    
    def Homework_Set_Test(self):
        self.test_homework = Homework(self.test_name, self.test_description, self.test_complexity, self.test_status)

    def Homework_Name_Test(self):
        self.Homework_Set_Test()
        actual = self.test_homework.name
        expected = self.test_name
        utf.ExpectEqual(actual, expected)

    def Homework_Description_Test(self):
        self.Homework_Set_Test()
        actual = self.test_homework.description
        expected = self.test_description
        utf.ExpectEqual(actual, expected)


#######################################


employee_test = HomeworkTest()

employee_test.Homework_Name_Test()
employee_test.Homework_Description_Test()