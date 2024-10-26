# Read a natural number n. Print the number of 1s from the binary representation of
# n (e.g.: 547 has 4 digits equal to 1 in its binary representation).


def get_count_of_ones_from_binary_representation_of_number(n):
    count = 0 # Initialize counter for the number of 1s

    # Loop until all bits of n have been processed
    while n > 0:
        count = count + n % 2 # Add 1 to count if the last binary digit of n is 1
        n //= 2 # Right shift n by dividing by 2 to check the next bit

    return count # Return the total count of 1s in the binary representation
