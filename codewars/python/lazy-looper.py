"""
Solution to "Lazy Looper" problem on Codewars (Kata 5).
https://www.codewars.com/kata/51fc3beb41ecc97ee20000c3
"""

from collections.abc import Callable

def make_looper(string: str) -> Callable:
    c = [0]  # non-local counter accessible to inner function
    def _():
        while True:
            s = string[c[0]]
            c[0] += 1
            if c[0] == len(string):
                c[0] = 0

            return s

    return _


if __name__ == "__main__":
    abc = make_looper('abc')
    abc()  # should return 'a' on this first call
    abc()  # should return 'b' on this second call
    abc()  # should return 'c' on this third call
    abc()  # should return 'a' again on this fourth call
