import timeit
import unittest


''' Leaf position '''
X = 5
''' River '''
A = [1, 3, 1, 4, 2, 3, 5, 4]
''' In second 6, a leaf falls into position 5 '''
S = 6


def solution(X, A):
    ''' Return earliest time when leaves appear in every position across the river. '''
    leaves = [0] * X
    clear = X
    for x in xrange(0, len(A)):
        if leaves[A[x]-1] == 0:
            leaves[A[x]-1] = 1
            clear -= 1
        if clear == 0:
            return x
    return -1


def time_test():
    ''' Function to test the execution time '''
    solution(X, A)


class FrogRiverTest(unittest.TestCase):
    ''' The expected return integer from solution() must be equal to S '''
    def test_frog(self):
        self.assertEqual(solution(X, A), S)


if __name__ == '__main__':
    print(timeit.timeit(time_test))
    unittest.main()
