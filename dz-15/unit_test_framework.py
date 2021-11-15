import inspect

def GetColor(color_name):
    assert color_name != "NAME" or color_name != "SUCCESS" or color_name != "FAILED" or color_name != "LINE"

    if color_name == "NAME":
        return '\033[95m'
    elif color_name == "SUCCESS":
        return '\033[92m'
    elif color_name == "FAILED":
        return '\033[91m'
    elif color_name == "LINE":
        return '\033[39m'

def GetParameter(param_name):
    assert param_name != "TestName" or param_name != "TestLine"

    if param_name == "TestName":
        return lambda: str(inspect.stack()[2][3])
    elif param_name == "TestLine":
        return lambda: str(inspect.stack()[2][2])

def ExpectEqual(actual, expected):
    line_numer = GetParameter("TestLine")
    test_name = GetParameter("TestName")

    message = GetColor("NAME") + test_name() + "(" + GetColor("LINE") + f"line:{line_numer()}" + GetColor("NAME") + ") - \t"
    if actual == expected:
        message += GetColor("SUCCESS") + "SUCCESS"
    else:
        message += GetColor("FAILED") + f"FAILED: actual: {actual} , expected {expected}"
    print(message)

def ExpectNotEqual(actual, expected):
    line_numer = GetParameter("TestLine")
    test_name = GetParameter("TestName")

    message = GetColor("NAME") + test_name() + "(" + GetColor("LINE") + f"line:{line_numer()}" + GetColor("NAME") + ") - \t"
    if not actual == expected:
        message += GetColor("SUCCESS") + "SUCCESS"
    else:
        message += GetColor("FAILED") + f"FAILED: actual: {actual} , expected {expected}"
    print(message)

def ExpectThrown(block, exception):
    line_numer = GetParameter("TestLine")
    test_name = GetParameter("TestName")
    message = GetColor("NAME") + test_name() + "(" + GetColor("LINE") + f"line:{line_numer()}" + GetColor("NAME") + ") - \t"
    try:
        block()
    except type(exception):
        message += GetColor("SUCCESS") + "SUCCESS"
    else:
        message += GetColor("FAILED") + f" exception {type(exception)} don't thrown."
    print(message)

def ExpectNotThrown(block):
    line_numer = GetParameter("TestLine")
    test_name = GetParameter("TestName")
    message = GetColor("NAME") + test_name() + "(" + GetColor("LINE") + f"line:{line_numer()}" + GetColor("NAME") + ") - \t"
    try:
        block()
    except Exception as e:
        message += GetColor("FAILED") + f" exception {e.__str__()} don't thrown."
    else:
        message += GetColor("SUCCESS") + "SUCCESS"
    print(message)