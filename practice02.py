def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    print('{} yoshdasiz'.format(age))

    if age >= 18:
        print('Siz balog\'atga yetgansiz')
    else:
        print('Siz balog\'atga yetmagansiz')

calculate_age(2025, 2009)