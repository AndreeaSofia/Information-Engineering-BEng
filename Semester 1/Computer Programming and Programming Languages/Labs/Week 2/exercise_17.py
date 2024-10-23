# A number n is special if there is a natural number m such that n=m+S(m), where S(m) is the sum of digits of m.
# Verify if a given number is special. (e.g.: 1235 is special because 1235=1225+10).


def sum_of_digits(n):
    total = 0  # This will store the sum of the digits of n
    while n > 0:
        total += n % 10  # Add the last digit of n to total
        n //= 10  # Remove the last digit from n
    return total  # Return the sum of digits


def is_special(n):
    for m in range(1, n):  # Check all numbers m from 1 to n-1
        if n == m + sum_of_digits(m):  # If n equals m + sum of digits of m
            return True  # n is special
    return False  # If no such m exists, n is not special


# Example:
n = 1235
print(is_special(n))  # Output: True (because 1235 = 1225 + 10)
