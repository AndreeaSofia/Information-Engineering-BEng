# Determine the value of the element at the index k in the array 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, ... without
# reading or effectively creating the array. (e.g.: k = 35, output is 8).

def value_at_index(k):
    n = 1  # Start with the number 1
    total_positions = 0  # Track how many positions we've filled

    while total_positions < k:
        total_positions += n  # Add 'n' positions for the current number
        if total_positions >= k:  # If we've reached or exceeded position k
            return n  # Return the number n
        n += 1  # Move to the next number


# Example:
k = 35
print(value_at_index(k))  # Output: 8
