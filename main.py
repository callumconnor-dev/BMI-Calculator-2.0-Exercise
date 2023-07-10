height = (float(input("Please enter your height in m: ")))
weight = (float(input("Please enter your weight in kg: ")))

bmi = round(weight / (height ** 2))

if bmi >= 35:
  bmiStatus = "are clinically obese"
elif bmi >= 30:
  bmiStatus = "are obese"
elif bmi >= 25:
  bmiStatus = "are slightly overweight"
elif bmi >= 18.5:
  bmiStatus = "have a normal weight"
else: 
  bmiStatus = "are underweight"

print(f"Your BMI is {bmi}, you {bmiStatus}.")