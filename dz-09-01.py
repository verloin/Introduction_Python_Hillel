import random

#######################################################
# 1
def buble_sort(nums):
    t = nums.copy()
    for n in range(0, len(t)):
        for i in range(len(t)):
            if t[i] > t[n]:
                t[i], t[n] = t[n], t[i]
    return t

nums = [(random.randint(0, 100)) for _ in range(15)]
my_sorted = buble_sort(nums)

print(my_sorted)

assert my_sorted == sorted(nums), "failure"
assert my_sorted[0] <= my_sorted[-1], "failure, my_sorted[0] > my_sorted[-1]"

#######################################################
# 2
start_list = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]

final_list = list(map(lambda l: (l[0], l[-1] * l[-2] + 10) if (l[-1] * l[-2] < 100) else (l[0], l[-1] * l[-2]), start_list))

print(final_list)

#######################################################
# 3
start_list = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]

plus_list = [
    [24387, ' на русском', 2, 4.59],
    [18762, 'The C Programming Language (2nd Edition)', 12, 78.80],
    [87236, "C Programming Absolute Beginner's Guide", 1, 23.55],
    [58132, 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14', 9, 42.89]
]

start_list.extend(plus_list)
print(start_list)

#######################################################
# 4
start_list = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99],
    [24387, ' на русском', 2, 4.59],
    [18762, 'The C Programming Language (2nd Edition)', 12, 78.80],
    [87236, "C Programming Absolute Beginner's Guide", 1, 23.55],
    [58132, 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14', 9, 42.89]
]

print(sorted(start_list, key=lambda x:x[-1]))

#######################################################
# 5
start_list = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99],
    [24387, ' на русском', 2, 4.59],
    [18762, 'The C Programming Language (2nd Edition)', 12, 78.80],
    [87236, "C Programming Absolute Beginner's Guide", 1, 23.55],
    [58132, 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14', 9, 42.89]
]

final_list = list(filter(lambda x : x[-2] > 5, start_list))

print(final_list)