
age = int(input("Enter your age: "))
if 18 <= age <= 64:
    weight_lbs = float(input("Enter your weight in pounds:"))
    height_in = float(input("Enter your height in inches:"))
    bmi = weight_lbs / (height_in * height_in)
    print("BMI:", bmi)
    if bmi < 19:
        print("You are underweight")
    elif bmi > 24:
        print("You are overweight")
    else:
        print("You are right were you should be")
else:
    print("BMI is not valid for your age group")
