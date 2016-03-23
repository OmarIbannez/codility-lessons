from __future__ import division
import unittest
import math
import timeit


''' Frog position '''
X = 10
''' Minimum destination '''
Y = 85
''' Size of jumps '''
D = 30
''' Total jumps '''
S = 3




def slow_solution(X, Y, D):
    jumps = 0
    for jump in xrange(X, Y, D):
        jumps = jumps + 1
    return jumps

def fast_solution(X, Y, D):
    return int(math.ceil((Y-X) / D))

def faster_solution(X, Y, D):
    if (Y - X) % D == 0:
        return (Y - X) // D
    else:
        return ((Y - X) // D) + 1

def time_test():
    fast_solution2(X, Y, D)

class FrogTest(unittest.TestCase):
    def test_frog_jumps(self):
        self.assertEqual(solution(X, Y, D), S)




if __name__ == '__main__':
    print(timeit.timeit(time_test))
    unittest.main()
