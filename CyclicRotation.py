import collections
import unittest
import timeit


''' Input list '''
A = [3, 8, 9, 7, 6]
''' Times the values will rotate '''
K = 3
''' List rotated K times '''
S = [9, 7, 6, 3, 8]


def solution(A, K):
    ''' Rotate list A K times '''
    d = collections.deque(A)
    d.rotate(K)
    return list(d)


def time_test():
    ''' Function to test the execution time '''
    solution(A, K)


class CyclicRotationTest(unittest.TestCase):
    ''' The expected return list from solution() must be equal to S '''
    def test_cyclic_rotation(self):
        self.assertEqual(solution(A, K), S)


if __name__ == "__main__":
   print(timeit.timeit(time_test))
   unittest.main()
