import unittest
import timeit


''' Consecutive integers '''
A = [1, 2, 9, 8, 6, 4, 5, 7, 3, 10, 15, 11, 13, 14]
''' Missing int '''
S = 12


def solution(A):
    ''' Return the missing int '''
    a_len = len(A)
    complete = (a_len + 1) * (a_len + 2) // 2
    incomplete = sum(A)
    return complete - incomplete


def test():
    ''' Function to test the execution time '''
    solution(A)


class MissingElementTest(unittest.TestCase):

    def test_missing(self):
        ''' The expected return integer from solution() must be equal to S '''
        self.assertEqual(solution(A), S)


if __name__ == '__main__':
    print(timeit.timeit(test))
    unittest.main()
