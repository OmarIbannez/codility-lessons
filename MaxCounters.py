import unittest
import timeit


A = [3, 4, 4, 6, 1, 4, 4]
N = 5
S = [3, 2, 2, 4, 2]


def solution(N, A):
    ''' Returns value of every counter after all operations '''
    counters = [0] * N
    for x in A:
        if 1 <= x <= N:
            counters[x-1] += 1
        else:
            counters[:] = [max(counters)] * N
    return counters


def time_test():
    ''' Function to test the execution time '''
    solution(N, A)


class CountersTest(unittest.TestCase):
    ''' The output from solution() must be equal to S '''
    def test_counters(self):
        self.assertEqual(solution(N, A), S)


if __name__ == '__main__':
    print(timeit.timeit(time_test))
    unittest.main()
