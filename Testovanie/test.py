from unit import *
from tests_case import *


def test_upper_space():
    print('TEST UPPER SPACE')
    counter = 0
    for i in t_upper_space.keys():
        try:
            assert upper_space(i) == t_upper_space[i]
        except AssertionError:
            print('Test failed!')
            continue
        print('Test passed!')
        counter += 1

    print(
        f'\nTest for upper space : {counter}/{len(t_upper_space.keys())}\n'+'-'*90)
    pass


def test_highest_rank():
    print('TEST HIGHEST RANK')
    counter = 0
    for i in t_highest_rank.keys():
        try:
            assert highest_rank(t_highest_rank[i]) == i
        except AssertionError:
            print('Test failed!')
            continue
        print('Test passed!')
        counter += 1

    print(
        f'\nTest for highest rank : {counter}/{len(t_highest_rank.keys())}\n'+'-'*90)
    pass
