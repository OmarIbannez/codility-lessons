import unittest
import timeit


''' Input list '''
A = [9, 3, 9, 3, 9, 7, 9]
''' Odd integer '''
S = 7


def solution(A):
    ''' Bitwise xor over the list of integers '''
    odd_int = 0
    for x in A: odd_int ^= x
    return odd_int


def time_test():
    ''' Function to test the execution time '''
    solution(A)


class OddIntegerTest(unittest.TestCase):
    ''' The expected return integer from solution() must be equal to S '''
    def test_odd_int(self):
        self.assertEqual(solution(A), S)


if __name__ == '__main__':
    print(timeit.timeit(time_test))
    unittest.main()
