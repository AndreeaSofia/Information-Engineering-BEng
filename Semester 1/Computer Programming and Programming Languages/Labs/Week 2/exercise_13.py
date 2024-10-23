# Read a natural number n. Form another number from its digits found at odd positions (from left to right).
# (e.g.: for 1234 input, output is 13).


def number_from_odd_positions(n):
    digits = str(n)  # Convert the number to a string to process from left to right
    result = ""  # This will store the digits from/at odd positions

    # Loop through the digits and pick the ones at odd positions (1st, 3rd, 5th, etc.)
    for i in range(len(digits)):
        if (i + 1) % 2 != 0:  # Check if the position (i+1) is odd
            result += digits[i]  # Add the digit at the current odd position

    return int(result)  # Convert the result string back to an integer


# Example:
n = 12345
print(number_from_odd_positions(n))  # Output: 135

