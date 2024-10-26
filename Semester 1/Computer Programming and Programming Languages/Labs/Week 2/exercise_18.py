def get_count_and_common_digits_of_numbers(num1, num2):
    count = 0
    common = []
    num1_digits = generate_sorted_list_of_unique_digits(num1)
    num2_digits = generate_sorted_list_of_unique_digits(num2)

    for i in range(0, 10):
        if i in num1_digits and i in num2_digits:
            count = count + 1
            common.append(i)

    return count, common

def generate_sorted_list_of_unique_digits(number):
    digits = []

    while number > 0:
        digits.append(number%10)
        number = number//10

    digits.sort()

    return digits
