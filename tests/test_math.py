from math_utils import is_prime, fib


def test_primes():
    assert [p for p in range(2, 30) if is_prime(p)] == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_fib():
    assert [fib(n) for n in range(7)] == [0, 1, 1, 2, 3, 5, 8]
