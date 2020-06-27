
age = int(input("Enter your age: "))
if 18 <= age <= 64:
    weight_kg = float(input("Enter your weight in kg:"))
    height_m = float(input("Enter your height in meters:"))
    bmi = weight_kg / (height_m * height_m)
    print("BMI:", bmi)
    if bmi < 19:
        print("You are underweight")
    elif bmi > 24:
        print("You are overweight")
    else:
        print("You are right were you should be")
else:
    print("BMI is not valid for your age group")
