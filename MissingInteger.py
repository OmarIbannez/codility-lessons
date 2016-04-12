import unittest
import timeit


A = [1, 2, 3, 4, 6, 7, 8, 9, 10]
S = 5


def solution(A):
    ''' returns the minimal positive integer (greater than 0) that does not occur in A '''
    size = len(A) + 1
    seen = [False] * size
    for x in A:
        if x > 0 and x < size:
            seen[x-1] = True
    return seen.index(False) + 1


def time_test():
    ''' Function to test the execution time '''
    solution(A)


class MissingIntTest(unittest.TestCase):
    ''' The output from solution() must be equal to S '''
    def test_missing(self):
        self.assertEqual(solution(A), S)


if __name__ == '__main__':
    print(timeit.timeit(time_test))
    unittest.main()
