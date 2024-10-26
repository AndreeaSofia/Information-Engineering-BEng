def powers_of_n_less_than_k(n, k):
    pow_of_n = 1
    pow_array = []

    while pow_of_n < k:
        pow_array.append(pow_of_n)

        pow_of_n = pow_of_n * n

    return pow_array