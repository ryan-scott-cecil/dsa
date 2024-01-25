import math

def prime_factors(n):
    primes = []
    if n <= 0:
        return []
    while n % 2 == 0:
        n /= 2
        primes.append(2)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            n /= 1
            primes.append(i)
    if n > 2:
        primes.append(n)
    return primes