import unittest
import timeit


''' Frog position '''
X = 10
''' Minimum destination '''
Y = 85
''' Size of jumps '''
D = 30
''' Total jumps '''
S = 3


def solution(X, Y, D):
    ''' Jumps from X to Y '''
    if (Y - X) % D == 0:
        return (Y - X) // D
    else:
        return ((Y - X) // D) + 1


def time_test():
    ''' Function to test the execution time '''
    solution(X, Y, D)


class FrogTest(unittest.TestCase):
    '''' The expected return integer from solution() must be equal to S '''
    def test_frog_jumps(self):
        self.assertEqual(solution(X, Y, D), S)


if __name__ == '__main__':
    print(timeit.timeit(time_test))
    unittest.main()
