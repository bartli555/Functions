###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    number = abs(number)
    number_as_string = str(number)
    sum_of_digits = 0
    for i in number_as_string:
        sum_of_digits += int(i)
        
    return sum_of_digits

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')