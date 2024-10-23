# Compute the control digit of an integer by summing up its digits, then summing up the digits of the sum,
# so on, until a sum of only one digit is obtained. (e.g.: The control digit of integer number 1971 is 9).


def control_digit(n):
    while n >= 10: # Continue while the number has more than one digit
        sum_digits = 0 # Reset the sum of digits for this iteration
        while n > 0:
            sum_digits += n % 10  # Add the last digit to sum_digits
            n //= 10  # Remove the last digit from n
        n = sum_digits  # Update n to the sum of its digits
    return n  # Return the final single-digit number


# Example:
an = 1971
print(control_digit(an))  # Output: 9
