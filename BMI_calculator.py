
print("Welcome to BMI calculator!")
w = input("Enter your weight(kg): ")
h = input("Enter your height(m): ")

bmi = float(w) / (float(h)**2)
bmi = round(bmi,1)                  #rounds the bmi value

if bmi <= 18.5:
    print(f"Your BMI is {bmi} - Underweight")
elif bmi > 18.5 and bmi <= 25:                  # 18.5 < bmi < 25:   (also works)
    print(f"Your BMI is {bmi} - Normal")
elif bmi >= 25 and bmi > 30:
    print(f"Your BMI is {bmi} - Overweight")
else:
    print(f"Your BMI is {bmi} -Obese")