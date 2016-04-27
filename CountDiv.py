import unittest
import timeit


A = 6
B = 11
K = 2
S = 3


def solution(A, B, K):
    ''' Returns the number of integers within the range [A..B] that are divisible by K'''
    a = A//K
    b = B//K
    if A%K == 0: a -= 1
    return b-a


def time_test():
    ''' Function to test the execution time '''
    solution(A, B, K)


class CountdivTest(unittest.TestCase):
    ''' The output from solution() must be equal to S '''
    def test_countdiv(self):
        self.assertEqual(solution(A, B, K), S)


if __name__ == '__main__':
    print(timeit.timeit(time_test))
    unittest.main()
