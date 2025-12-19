def is_even(num):
    return True if num % 2 == 0 else False

def print_even_message(num):
    if is_even(num):
        print('Juft son')
    else:
        print('Toq son')

number = int(input('Num: '))
print_even_message(number)