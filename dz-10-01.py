import random

#######################################################
# 1
def create_and_write():

    with open('test.txt', 'w') as file:
        for _ in range(100):
            for _ in range(10):
                num = (random.randint(0, 100))
                file.write(str(num) + ' ')
            file.write('\n')
    
    with open('test.txt', 'r') as for_test:
        my_list = for_test.readlines()

        assert len(my_list) != 0,  'The list should not be empty'
        assert len(my_list) == 100, 'The length of list should be 100'
        assert len(my_list[0][:-2].split(' ')) == 10, 'The length of first string should be 10'

create_and_write()


#######################################################
# 2

def pow_and_rewritten():
    with open('test.txt', 'r+') as file:
        my_list = file.readlines()

        for i in my_list:
            string = i.split(' ')
            for k in (string[:-1]):
                number = int(k)**2
                file.write(str(number) + ' ')
            file.write('\n')

    with open('test.txt', 'r') as for_test:
        my_list = for_test.readlines()

        assert len(my_list) != 0,  'The list should not be empty'
        assert len(my_list) == 200, 'The length of list should be 100'
        assert len(my_list[-1][:-2].split(' ')) == 10, 'The length of last string should be 10'
            
pow_and_rewritten()

