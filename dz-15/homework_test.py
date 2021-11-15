"""
class HomeworkTest needed for testing the creation of object homework

Methods:
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

    __slots__ = ('__test_name', '__test_description', '__test_complexity', '__test_status', 'test_homework')

    def __init__(self):
        self.__test_name = 'name'
        self.__test_description = 'description'
        self.__test_complexity = 0
        self.__test_status = True

    
    def __Homework_Set_Test(self):
        """ This method needed for transfer data of homework to variable """

        self.test_homework = Homework(self.__test_name, self.__test_description, self.__test_complexity, self.__test_status)

    def Homework_Name_Test(self):
        """ This method needed for testing of naming name homework """

        self.__Homework_Set_Test()
        actual = self.test_homework.name
        expected = self.__test_name
        utf.ExpectEqual(actual, expected)

    def Homework_Description_Test(self):
        """ This method needed for testing of description homework """

        self.__Homework_Set_Test()
        actual = self.test_homework.description
        expected = self.__test_description
        utf.ExpectEqual(actual, expected)


#######################################


employee_test = HomeworkTest()

employee_test.Homework_Name_Test()
employee_test.Homework_Description_Test()