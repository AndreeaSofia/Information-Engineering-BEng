def get_numbers_of_n_digits_equal_to_k_multiplied_by_digits_product(n, k):
    lower_limit = 10**(n - 1)
    upper_limit = 10**n

    valid_numbers = []

    for num in range(lower_limit, upper_limit):
        product = 1
        temp = num
        while temp > 0:
            product = product * (temp%10)
            temp = temp//10

        if k*product == num:
            valid_numbers.append(num)

    return valid_numbers