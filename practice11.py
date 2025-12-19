def calculate_tax(salary: float) -> float:
    if salary > 5_000_000:
        tax = 0.20
    else:
        tax = 0.13

    return salary * tax

def calculate_net_salary(salary: float) -> float:
    tax = calculate_tax(salary)
    return salary - tax

salary = float(input("Maoshingiz: "))

tax = calculate_tax(salary)
net_salary = calculate_net_salary(salary)

print(tax)
print(net_salary)