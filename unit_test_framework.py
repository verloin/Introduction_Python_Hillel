import inspect

def GetColor(color_name):
    assert color_name != "NAME" or color_name != "SUCCESS" or color_name != "FAILED"

    if color_name == "NAME":
        return '\033[95m'
    elif color_name == "SUCCESS":
        return '\033[92m'
    elif color_name == "FAILED":
        return '\033[91m'

def GetParameter(param_name):
    assert param_name != "TestName" or param_name != "TestLine"

    if param_name == "TestName":
        return lambda: str(inspect.stack()[2][3])
    elif param_name == "TestLine":
        return lambda: str(inspect.stack()[2][2])

def ExpectEqual(actual, expected):
    line_numer = GetParameter("TestLine")
    test_name = GetParameter("TestName")

    message = GetColor("NAME") + test_name() + f"(line:{line_numer()}) - \t"
    if actual == expected:
        message += GetColor("SUCCESS") + "SUCCESS"
    else:
        message += GetColor("FAILED") + f"FAILED: actual: {actual} , expected {expected}"
    print(message)

print(GetColor(133))