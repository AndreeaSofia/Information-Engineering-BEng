# Read integer numbers until number 0 is read. Print the number of pairs n1 and n2 of
# numbers read consecutively with the property that the number of digits 5 from n1 is 
# strictly higher than the number of digits 5 from n2. (e.g. If the numbers read are
# 182, 457, 341, 497, 5597, 1335, 15, 38, 5, 0 then the result is 3, as the pairs 457-341,
# 5597-1335, 15-38 satisfy the required property).


# Function to count pairs of consecutive numbers with a specific digit condition
def get_pairs():
    pairs_count = 0 # Initialize counter for valid pairs
    previous = None # Variable to store the previous number in sequence

    # Loop to continually read input until '0' is entered
    while True:
        current = input("Enter a Number (0 to Stop): ") # Read the current number as input

        if current == 0:  # Stop reading numbers if '0' is entered
            break 

        # Check if there's a previous number to compare with the current one
        if previous is not None: 
            # Check if the previous number has more '5's than the current number
            if number_of_digits_5(previous) > number_of_digits_5(current): 
                pairs_count = pairs_count + 1 # Increment the count of valid pairs

        previous = current # Update 'previous' to the current number for the next iteration

    return pairs_count # Return the total count of valid pairs


# Function to count the number of '5's in a given number
def number_of_digits_5(number):
    count = 0 # Initialize counter for '5' digits

    # Loop to check each digit of the number
    while number > 0 :
        if number % 10 == 5: # Check if the last digit is '5'
            count = count + 1 # Increment the count if the digit is '5'
        number = number // 10  # Remove the last digit by integer division

    return count
