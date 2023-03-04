# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = weight/height**2

def diagnosis(BMI):
    if BMI < 18.5:
        return "are underweight"
    if BMI < 25.0:
        return "have a normal weight"
    if BMI < 30.0:
        return "are slightly overweight"
    if BMI < 35.0:
        return "are obese"
    if BMI >= 35.0:
        return "are clinically obese"

print(f"""%s ÷ %s^2 = %s
Your BMI is %s, you are %s.""" % (weight, height, BMI, round(BMI), diagnosis(BMI)))
