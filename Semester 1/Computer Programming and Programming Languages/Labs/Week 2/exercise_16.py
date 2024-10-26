def get_numbers_with_unit_smaller_than_tens():
    count = 0 

    while True:
        number = int(input("Read a number of minimum 2 digits (0 to Stop): "))

        if number == 0:
            break

        if number >= 10 and number <= 99:
            if number%10 < (number//10)%10:
                count = count + 1

    return count