"""
Chapter 1:
    - Euclid's Algorithm
"""


def gcd(m, n):
    """Euclid's algorithm for finding the greatest common divisor (GCD) of two
    positive integers _m_ and _n_.
    """
    while True:
        r = m % n
        if r == 0:
            break
        m = n
        n = r
    return n


def gcd_recursive(m, n):
    """Recursive implementation of Euclid's algorithm"""
    r = m % n
    if r == 0:
        return n
    return gcd_recursive(m=n, n=r)
