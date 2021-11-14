"""
class EmployeeTest need for testing the creation of object employee

methods:
    Employee_Set_Test
    Employee_Name_Test
    Employee_Age_Test
    Employee_Room_Test
"""


import unit_test_framework as utf
from employee import Employee


class EmployeeTest:
    """
    This class is needed for testing the creation of object employee
    Args:
        name: this args is needed for naming object of employee
        age: this args is needed for age of employee
        test_room: this args is needed for naming room of employee
    """
    
    def __init__(self):
        self.test_name = "name"
        self.test_age = "20"
        self.test_room = 'room'

    def Employee_Set_Test(self):
        self.test_employee = Employee(self.test_name, self.test_age)

    def Employee_Name_Test(self):
        """
        This method is needed for testing creation name of employee
        """

        self.Employee_Set_Test()
        actual = self.test_employee.name
        expected = self.test_name
        utf.ExpectEqual(actual, expected)

    def Employee_Age_Test(self):
        """
        This method is needed for testing creation age of employee 
        """

        self.Employee_Set_Test()
        actual = self.test_employee.age
        expected = '20'
        utf.ExpectEqual(actual, expected)

    def Employee_Room_Test(self):
        """
        This method is needed for testing creation room of employee
        """

        self.Employee_Set_Test()
        actual = self.test_employee.room
        expected = self.test_room
        utf.ExpectEqual(actual, expected)


##############################


employee_test = EmployeeTest()

employee_test.Employee_Name_Test()
employee_test.Employee_Age_Test()
employee_test.Employee_Room_Test()