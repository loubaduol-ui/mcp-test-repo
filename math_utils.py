def is_prime(n: int) -> bool:
    if n < 2:
        return False
    return all(n % i for i in range(2, int(n ** 0.5) + 1))


def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
