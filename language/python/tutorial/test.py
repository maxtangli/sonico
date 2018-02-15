import unittest

def fib(n):
    if n==0: return 0
    elif n==1: return 1
    else: return fib(n-1) + fib(n-2)

class TestFib(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib(4), 3)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(6), 8)

if __name__ == '__main__':
    unittest.main()

"""
day 4 unittest, vim run 10min
thoughts
- nothing new, just code something to be familiar.
"""
