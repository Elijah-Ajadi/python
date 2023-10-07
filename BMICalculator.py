# this is a BMI calculator

h = int(input("Enter your height: "))
w = int(input("Enter your weight: "))


BodyMassIndex = w / (h^2)

if BodyMassIndex <= 18.5:
    print(f"your BMI {BodyMassIndex} is Underweight!")
    
elif BodyMassIndex <= 24:
    print(f"your BMI {BodyMassIndex} is Normal weight")
    
elif BodyMassIndex <= 28:
    print(f"your BMI of {BodyMassIndex} is Overweight")
    
elif BodyMassIndex > 28:
    print(f"You are Obese! Your BMI is {BodyMassIndex}")
