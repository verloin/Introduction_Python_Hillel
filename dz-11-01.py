import unit_test_framework
import operator

class FormulaError(Exception): 
    pass

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv
}

string = '1 + 2 = 3 % 4'

def calculation(string):
    try:
        lst = string.split()
        lst[0], lst[2] = int(lst[0]), int(lst[2])    
        return ops[lst[1]](lst[0], lst[2])
    except KeyError:
        raise FormulaError(f"{lst[1]} is not a valid operator")
    except ValueError:
        raise FormulaError('The first and third input value must be numbers')

def check_input(string):
    lst = string.split()

    # if len(start_list) != 3:
    #     raise FormulaError('Input does not consist of three elements')
    try:
        num1 = float(lst[0])
        num2 = float(lst[2])
    except ValueError:
        raise FormulaError('The first and third input value must be numbers')
    return num1, num2

check_input(string)

def culc(string):
    lst = string.split()

    if len(lst) == 3:
        try:
           return calculation(string)
        except KeyError:
            raise FormulaError(f"{lst[1]} is not a valid operator")
        except ZeroDivisionError:
            raise FormulaError("one of the numbers is zero, this is not allowed")

    if len(lst) > 3:
        num = calculation(string)
        del lst[:3]
        lst.insert(0, str(num))
        string = ' '.join(lst)
        return culc(string)

print(culc(string))

assert unit_test_framework.ExpectEqual(culc("1 + 1"), 2) == "SUCCESS", "SUCCESS in culc('1 + 1')"
assert unit_test_framework.ExpectEqual(culc("10 - 1"), 9) == "SUCCESS", "SUCCESS in culc('10 / 0')"
assert unit_test_framework.ExpectEqual(culc("10 + 5 * 4 / 2"), 30.0) == "SUCCESS", "SUCCESS in culc('10 + 5 * 4 / 2')"
