# Print all numbers with maximum 2 digits of form xy with the property that the last digit of (xy)^2 is y.
# (e.g.: 5^2=25 or 10^2=100 or 76^2=5776).


def find_numbers_xy():
    for x in range(0, 10):  # x is the first digit
        for y in range(0, 10):  # y is the second digit
            xy = x * 10 + y  # Form the two-digit number xy
            square = xy ** 2  # Calculate the square of xy
            if square % 10 == y:  # Check if the last digit of the squared number equals y
                print(str(xy) + " : " + str(square))


# Example:
find_numbers_xy() # This will print the numbers which fit the specified criteria in the function
