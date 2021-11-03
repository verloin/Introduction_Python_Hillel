import random

#######################################################
# 1
file_name = input()

def create_and_write(file_name):

    with open(f"{file_name}.txt", 'w') as file:
        strings = []

        for _ in range(100):
            random_list = random.sample(range(0, 100), 10)
            random_string = " ".join(map(str, random_list)) + '\n'
            strings.append(random_string)
        file.writelines(strings)

create_and_write(file_name)

with open(f"{file_name}.txt", 'r') as for_test:
    my_list = for_test.readlines()
    assert len(my_list) != 0,  'The list should not be empty'
    assert len(my_list) == 100, 'The length of list should be 100'
    assert len(my_list[0][:-2].split(' ')) == 10, 'The length of first string should be 10'

#######################################################
# 2

def add_in_file(file_name):
    with open(f"{file_name}.txt", 'r+') as file:
        strings = []

        for element in file:
            middle_list = [int(i)**2 for i in element.split()]
            string = ' '.join(str(el) for el in middle_list) + '\n'
            strings.append(string)
        file.writelines(strings)

add_in_file(file_name)

with open('test.txt', 'r') as for_test:
    my_list = for_test.readlines()
    assert len(my_list) != 0,  'The list should not be empty'
    assert len(my_list) == 200, 'The length of list should be 100'
    assert len(my_list[-1][:-1].split(' ')) == 10, 'The length of last string should be 10'
