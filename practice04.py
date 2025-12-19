def get_grade(ball):
    if ball >= 90:
        return "A"
    elif ball >= 80:
        return "B"
    elif ball >= 70:
        return "C"
    else:
        return "F"
    
print(get_grade(67))