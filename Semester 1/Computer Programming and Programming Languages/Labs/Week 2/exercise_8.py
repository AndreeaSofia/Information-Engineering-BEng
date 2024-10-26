def nearest_prime_to_number(n):
    if is_prime(n):
        return n

    lower = n - 1
    upper = n + 1

    while True:
        if lower >= 2 and is_prime(lower):
            return lower
        if is_prime(upper):
            return upper
        lower -= 1
        upper += 1


def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 2
    return True