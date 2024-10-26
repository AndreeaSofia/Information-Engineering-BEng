def smallest_number_using_digits_of_number(n):
    list_of_digits = []

    while n > 0 :
        list_of_digits.append(n%10)
        n = n//10

    list_of_digits.sort()

    minim_number = 0
    ignore = -99

    for i in range(0, len(list_of_digits)):
        if list_of_digits[i] != 0:
            minim_number = list_of_digits[i]
            ignore = i
            break

    for i in range(0, len(list_of_digits)):
        if i != ignore:
            minim_number = minim_number * 10 + list_of_digits[i]

    return minim_number


def smallest_number_using_digits_of_number_string_operation(num):
    # Convert the number to a string and get its digits
    digits = list(str(num))
    
    # Sort the digits
    digits.sort()
    
    # If the smallest digit is '0', find the first non-zero digit
    if digits[0] == '0':
        # Find the first non-zero digit
        for i in range(1, len(digits)):
            if digits[i] != '0':
                # Swap it with the first digit (0)
                digits[0], digits[i] = digits[i], digits[0]
                break
    
    # Join the digits back into a string and convert to integer
    smallest_number = ''.join(digits)
    
    return smallest_number