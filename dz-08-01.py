

########################################################
# 3
def sum_digit(n):
    if n > 0:
        return n % 10 + sum_digit(n // 10)
    elif n < 0:
        return 'Not supported'
    else:
        return 0

print(sum_digit(123))

# тесты
print('sum_digit(-5) -', 'Not supported' == sum_digit(-5))
print('sum_digit(0) -', 0 == sum_digit(0))
print('sum_digit(1) -', 1 == sum_digit(1))
print('sum_digit(5) -', 5 == sum_digit(5))
print('sum_digit(11332) -', 10 == sum_digit(11332))

########################################################
# 4
def fibonachi(n):
    if n in (1, 2):
        return 1
    elif n < 0:
        return 'Not supported'
    elif n == 0:
        return 0
    else:
        return fibonachi(n-2) + fibonachi(n-1)

print(fibonachi(11))

# тесты
print('fibonachi(-5) -', 'Not supported' == fibonachi(-5))
print('fibonachi(0) -', 0 == fibonachi(0))
print('fibonachi(1) -', 1 == fibonachi(1))
print('fibonachi(5) -', 5 == fibonachi(5))
print('fibonachi(11) -', 89 == fibonachi(11))


########################################################
# 5
def multiply(lst):
    if len(lst) > 1:
        return lst[-1] * multiply(lst[:-1])
    else:
        return lst[0]

print(multiply([1,-2,3]))

# # тесты
print('multiply([1,-2,3]) -', -6 == multiply([1,-2,3]))
print('multiply([0]) -', 0 == multiply([0]))
print('multiply([1]) -', 1 == multiply([1]))
print('multiply([1,2,3]) -', 6 == multiply([1,2,3]))
print('multiply(1,3,0) -', 0 == multiply([1,3,0]))

########################################################
# 6
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

print(is_power(16))

# тесты
print('is_power(-5) -', 'Not supported' == is_power(-5))
print('is_power(0) -', 'NO' == is_power(0))
print('is_power(1) -', 'NO' == is_power(1))
print('is_power(5) -', 'NO' == is_power(5))
print('is_power(11) -', 'NO' == is_power(11))
print('is_power(8) -', 'YES' == is_power(8))
print('is_power(16) -', 'YES' == is_power(16))