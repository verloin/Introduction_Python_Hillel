

# ########################################################
# # 3
def sum_digit(n):
    if n > 0:
        return n % 10 + sum_digit(n // 10)
    elif n < 0:
        return 'Not supported'
    else:
        return 0
n = int(input())
sum_digit(n)

# тесты
assert sum_digit(-5) == 'Not supported', "Should be - Not supported"
assert sum_digit(0) == 0, "Should be - 0"
assert sum_digit(1) == 1, "Should be - 1"
assert sum_digit(5) == 5, "Should be - 5"
assert sum_digit(11332) == 10, "Should be - 10"

# ########################################################
# # 4
def fibonachi(n):
    if n in (1, 2):
        return 1
    elif n < 0:
        return 'Not supported'
    elif n == 0:
        return 0
    else:
        return fibonachi(n-2) + fibonachi(n-1)

n = int(input())
fibonachi(n)

# тесты
assert fibonachi(-5) == 'Not supported', "Should be - Not supported"
assert fibonachi(0) == 0, "Should be - 0"
assert fibonachi(1) == 1, "Should be - 1"
assert fibonachi(5) == 5, "Should be - 5"
assert fibonachi(11) == 89, "Should be - 89"


# ########################################################
# # 5
def multiply(lst):
    if len(lst) > 1:
        return lst[-1] * multiply(lst[:-1])
    else:
        return lst[0]

multiply([1,-2,3])

# # тесты
assert multiply([1,-2,3]) == -6, "Should be - -6"
assert multiply([0]) == 0, "Should be - 0"
assert multiply([1]) == 1, "Should be - 1"
assert multiply([1,2,3]) == 6, "Should be - 6"
assert multiply([1,3,0]) == 0, "Should be - 0"

# ########################################################
# # 6
def is_power(n):
    n = n/2
    if n == 2:
        return 'YES'
    elif n < 0:
        return 'Not supported'
    elif n > 2:
        return is_power(n)
    else:
        return 'NO'

n = int(input())
is_power(n)

# тесты
assert is_power(-5) == 'Not supported', "Should be Not supported"
assert is_power(0) == 'NO', "Should be NO"
assert is_power(1) == 'NO', "Should be NO"
assert is_power(5) == 'NO', "Should be NO"
assert is_power(11) == 'NO', "Should be NO"
assert is_power(8) == 'YES', "Should be YES"
assert is_power(16) == 'YES', "Should be YES"

########################################################
# # 7
def external_sum(a, b):
    def inner_sum(a,b):
        return a + b
    return inner_sum(a, b) + 5

a,b = int(input()), int(input())
external_sum(a, b)

# тесты
assert external_sum(50, 50) == 105, "Should be 105"
assert external_sum(1, 0) == 6, "Should be 6"
assert external_sum(0, 0) == 5, "Should be 5"