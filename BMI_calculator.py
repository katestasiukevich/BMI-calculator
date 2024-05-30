height, weight = int(input('Height (cm): ')), int(input('Weight (kg): '))
bmi = weight / (height / 100) ** 2
print(f'BMI: {int(bmi)}')
print("10" + "=" * (int(bmi) - 11) + "|" + "=" * (50 - (int(bmi) + 1)) + "50") # шкала имт от 10 до 50