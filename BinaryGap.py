import timeit
import unittest


""" Integer """
N = 1041
""" Longest sequence of zeros """
S = 5


def solution_one_liner(n):
    """Return the longest sequence of zeros in binary representation of N"""
    return len(max("{0:b}".format(n).split("1")))


def solution(n):
    binary = bin(n)[2:]
    max_zeros = 0
    zeros = 0
    for bit in binary:
        if int(bit) == 0:
            zeros += 1
        if int(bit) == 1:
            max_zeros = max(max_zeros, zeros)
            zeros = 0
    return max_zeros


def time_test():
    """Function to test the execution time"""
    solution(N)


class BinaryGapTest(unittest.TestCase):
    """The expected return integer from solution() must be equal to S"""

    def test_binary_gap(self):
        self.assertEqual(solution(N), S)


if __name__ == "__main__":
    print(timeit.timeit(time_test))
    unittest.main()
