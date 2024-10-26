# Determine if two natural numbers have the following property: the same
# digits are necessary to write them in base 10 (e.g.: 2113 and 31221 have
# this property, whereas 12521 and 11551 do not).


def check_if_numbers_have_same_digits_in_base_two(num1, num2):
    str_num1 = str(num1) # Convert the first number to a string
    str_num2 = str(num2) # Convert the second number to a string
    
    count1 = {} # Dictionary to count the occurrences of each digit in num1
    count2 = {} # Dictionary to count the occurrences of each digit in num2

    # Count the frequency of each digit in the first number
    for digit in str_num1:
        count1[digit] = count1.get(digit, 0) + 1

    # Count the frequency of each digit in the second number
    for digit in str_num2:
        count2[digit] = count2.get(digit, 0) + 1

    # Return True if both numbers have the same digits with the same frequency
    return count1 == count2
