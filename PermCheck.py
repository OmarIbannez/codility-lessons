import timeit
import unittest


''' Input list '''
A = [4, 1, 3]
''' output '''
S = 0


def solution(A):
    ''' returns 1 if A is a permutation and 0 if it is not '''
    if set(A) == set(xrange(1, len(A)+1)):
        return 1
    return 0


def time_test():
    ''' Function to test the execution time '''
    solution(A)


class PermCheckTest(unittest.TestCase):
    ''' The output from solution() must be equal to S '''
    def test_perm(self):
        self.assertEqual(solution(A), S)


if __name__ == '__main__':
    print(timeit.timeit(time_test))
    unittest.main()
