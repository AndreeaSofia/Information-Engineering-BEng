def get_count_of_ones_from_binery_representation_of_number(n):
    count = 0
    while n > 0:
        count = count + n % 2
        n //= 2

    return count