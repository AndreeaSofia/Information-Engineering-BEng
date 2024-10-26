#get pairs of numbers where the first number's number of digits 5 is strictly higher
#than the number of digits 5 from the second number
def get_pairs():
    pairs_count = 0
    previous = None

    while True:
        current = input("Enter a Number (0 to Stop): ")

        if current == 0:
            break 

        if previous is not None:
            if number_of_digits_5(previous) > number_of_digits_5(current):
                pairs_count = pairs_count + 1

        previous = current

    return pairs_count


def number_of_digits_5(number):
    count = 0

    while number > 0 :
        if number % 10 == 5:
            count = count + 1
        number = number // 10

    return count
