def get_all_prime_numbers_with_certain_amount_of_digits_where_prefixes_are_prime_too(n):
    lowest = 10**(n - 1)
    highest = 10**n
    result = []

    for i in range(lowest, highest):
        check = True
        number = i
        while number > 0:
            if not is_prime(number):
                check = False
            number = number // 10
        
        if check == True:
            result.append(i)

    return result


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