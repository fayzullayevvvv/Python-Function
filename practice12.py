def calculate_bmi(weight: float, height: float) -> float:
    height = height / 100
    return weight / (height ** 2)

def bmi_status(bmi: float) -> str:
    if bmi < 18.5:
        return "Ozgin"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Ortiqcha vazn"
    else:
        return "Semiz"


bmi = calculate_bmi(60, 180)
status = bmi_status(bmi)

print(f"BMI: {bmi:.2f}")
print(f"Holat: {status}")