def c_to_f(celsius):
    return celsius * 9 / 5 + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

c = float(input("Celsius: "))
print("Fahrenheit:", c_to_f(c))

f = float(input("Fahrenheit: "))
print("Celsius:", f_to_c(f))
