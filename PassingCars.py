import unittest
import timeit


A = [0, 1, 0, 1, 1]
S = 5


def solution(A):
    ''' Return the count of passing cars. '''
    west = 0
    passing = 0
    for x in xrange(len(A)-1, -1, -1):
        if A[x] == 0:
            passing += west
            if passing > 1000000000: return -1
        else:
            west += 1
    return passing


def time_test():
    ''' Function to test the execution time '''
    solution(A)


class PassingCarsTest(unittest.TestCase):
    ''' The output from solution() must be equal to S '''
    def test_missing(self):
        self.assertEqual(solution(A), S)


if __name__ == '__main__':
    print(timeit.timeit(time_test))
    unittest.main()
