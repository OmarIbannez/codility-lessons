import unittest
import timeit


''' Input list '''
A = [3, 1, 2, 4, 3]
''' Minimal difference '''
S = 1


def solution(A):
    ''' returns the minimal difference that can be achieved '''
    minimal = 0
    right_part = sum(A)
    left_part = 0
    for x in xrange(len(A)-1):
        left_part += A[x]
        right_part -= A[x]
        difference = abs(left_part - right_part)
        if minimal == 0 or difference < minimal:
            minimal = difference
    return minimal


def time_test():
    ''' Function to test the execution time '''
    solution(A)


class TapeEquilibriumTest(unittest.TestCase):
    ''' The expected return integer from solution() must be equal to S '''
    def test_equilibrium(self):
        self.assertEqual(solution(A), S)


if __name__ == '__main__':
    print(timeit.timeit(time_test))
    unittest.main()
