# module to run the tests for Damivis's snake problem
from utils import SnakeSolver

# define test inputs:
test1 = {'board': [4,3],
         'snake': [[2,2],[3,2],[3,1],[3,0],[2,0],[1,0],[0,0]],
         'depth': 3,
         'expect_result': 7}

test2 = {'board': [2,3],
         'snake': [[0,2],[0,1],[0,0],[1,0],[1,1],[1,2]],
         'depth': 10,
         'expect_result': 1}

test3 = {'board': [10,10],
         'snake': [[5,5],[5,4],[4,4],[4,5]],
         'depth': 4,
         'expect_result': 81}

tests = [test1, test2, test3] # remove from list to choose a subset of tests

# run the tests:
i=1
for test in tests:

    # initialize board and snake
    snake = SnakeSolver(test['board'], test['snake'])

    result = snake.numberOfAvailableDifferentPaths(test['depth'])

    # print inputs and result
    print('\nTest{}:'.format(i))
    print('\tBoard: ', test['board'])
    print('\tSnake: ', test['snake'])
    print('\tDepth: ', test['depth'])
    print('Expected result: ', test['expect_result'])
    if result == test['expect_result']:
        print('Test PASSED with result: ', result)
    else:
        print('Test FAILED with result: ', result)

    i+=1