height = input("Enter your height in m: ")
new_height = float(height)
weight = input("Enter your weight in kg: ")
new_weight = int(weight)

# BMI = weight / height**2
BMI = int(new_weight / new_height ** 2)

print(BMI)