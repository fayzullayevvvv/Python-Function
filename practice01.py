def add(a, b):
    result = a + b
    return result

def subtract(a, b):
    result = a - b
    return result

def multiply(a, b):
    result = a * b
    return result

def divide(a, b):
    result = a / b
    return result

def main():
    a = int(input('a: '))
    b = int(input('b: '))

    op = input('Operator (+, -, *, /): ')
    if op == '+':
        result = a + b

    if op == '-':
        result = a - b

    if op == '*':
        result = a * b

    if op == '/':
        result = a / b

    print(result)

main()