from random import randint

def check_guess(secret, guess):
    return secret == guess

def print_result(is_correct):
    if is_correct:
        print("To'gri topdingiz.")
    else:
        print("Xato")

secret_number = randint(1, 20)
user = int(input('Num: '))

result = check_guess(secret_number, user)
print_result(result)