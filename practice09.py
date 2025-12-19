def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if balance > amount:
        return balance - amount
    else:
        return 'Balansda yetarli mablag\' mavjud emas'

def check_balance(balance):
    return balance
