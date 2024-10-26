def greatest_power_of_2_smaller_or_equal_to_number(n):
    p = 0
    power = 1

    while True:
        if power > n:
            return p - 1

        p = p + 1
        power = power * 2
