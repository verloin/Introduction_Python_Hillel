"""
class HomeworkTest needed for testing the creation of object homework

class:
    HomeworkTest

methods:
    Homework_Set_Test
    Homework_Name_Test
    Homework_Description_Test
"""


import unit_test_framework as utf
from homework import Homework


class HomeworkTest:
    """
    This class needed for testing the creation of object homework
    Args:
        test_name: This arg needed for naming title object homework
        test_description: This arg needed for description homework
        test_complexity: This agr needed for specifying complexity homework
        test_status: This arg needed for specifying of status homework
    """

    def __init__(self):
        self.test_name = 'name'
        self.test_description = 'description'
        self.test_complexity = 0
        self.test_status = True

    
    def Homework_Set_Test(self):
        """
        This method needed for transfer data of homework to variable
        """

        self.test_homework = Homework(self.test_name, self.test_description, self.test_complexity, self.test_status)

    def Homework_Name_Test(self):
        """
        This method needed for testing of naming name homework
        """

        self.Homework_Set_Test()
        actual = self.test_homework.name
        expected = self.test_name
        utf.ExpectEqual(actual, expected)

    def Homework_Description_Test(self):
        """
        This method needed for testing of description homework
        """

        self.Homework_Set_Test()
        actual = self.test_homework.description
        expected = self.test_description
        utf.ExpectEqual(actual, expected)


#######################################


employee_test = HomeworkTest()

employee_test.Homework_Name_Test()
employee_test.Homework_Description_Test()