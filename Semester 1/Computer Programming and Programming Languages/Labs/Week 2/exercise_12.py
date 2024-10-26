def check_if_numbers_have_same_digits_in_base_two(num1, num2):
    str_num1 = str(num1)
    str_num2 = str(num2)
    
    count1 = {}
    count2 = {}
    
    for digit in str_num1:
        count1[digit] = count1.get(digit, 0) + 1
        
    for digit in str_num2:
        count2[digit] = count2.get(digit, 0) + 1
    
    return count1 == count2