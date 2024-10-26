# Generate all prime numbers having n digits with the property that all its prefixes
# are also prime (e.g. For n=2, the first number is 23, as 2, 23 are primes).


# Generate all prime numbers with 'n' digits where all prefixes are also prime
def get_prime_numbers_with_all_prime_prefixes(n):
    lowest = 10**(n - 1) # The smallest n-digit number
    highest = 10**n # The smallest number with (n+1) digits, sets the upper bound
    result = [] # List to store valid prime numbers

    # Loop through all n-digit numbers
    for i in range(lowest, highest):
        check = True # Flag to indicate if all prefixes of 'i' are prime
        number = i
        # Check each prefix of the number by progressively removing the last digit
        while number > 0:
            if not is_prime(number): # If any prefix is not prime
                check = False # Set check to False if a non-prime prefix is found
            number = number // 10 # Remove the last digit to check the next prefix

        # If all prefixes are prime, add the number to the result list
        if check == True:
            result.append(i)

    return result # Return the list of numbers that meet the criteria


# Helper function to check if a number is prime
def is_prime(n):
    if n <= 1: # Numbers less than or equal to 1 are not prime
        return False
    if n == 2 or n == 3: # 2 and 3 are prime numbers
        return True
    if n % 2 == 0: # Exclude even numbers greater than 2
        return False
    i = 3
    # Check for factors from 3 up to the square root of n
    while i * i <= n:
        if n % i == 0: # If a factor is found, n is not prime
            return False
        i = i + 2 # Only check odd numbers
    return True # If no factors found, n is prime
