import unittest
import timeit

A = [4, 2, 2, 5, 1, 5, 8]
S = 1


def solution(A):
    list_size = len(A)
    min_index = 0
    min_avg = 9999999

    for x in xrange(list_size-1):
        slice_avg = (A[x] + A[x+1]) / 2.0
        if slice_avg < min_avg:
            min_index = x
            min_avg = slice_avg

        if x < list_size-2:
            slice_avg = (A[x] + A[x+1] + A[x+2]) / 3.0
            if slice_avg < min_avg:
                min_index = x
                min_avg = slice_avg

    return min_index


def time_test():
    ''' Function to test the execution time '''
    solution(A)


class MinAvgTwoSliceTest(unittest.TestCase):
    ''' The output from solution() must be equal to S '''
    def test_min_avg(self):
        self.assertEqual(solution(A), S)


if __name__ == '__main__':
    print(timeit.timeit(time_test))
    unittest.main()
