def deposit(balance, amount):
    if amount > 0:
        return balance + amount
    return balance

def withdraw(balance, amount):
    if balance >= amount:
        return balance - amount
    else:
        return 'Balansda yetarli mablag\' mavjud emas'

def check_balance(balance):
    return f'Sizning balansingiz: {balance:,.2f} so\'m'