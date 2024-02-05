print("HI, WELCOME TO BMI CALCULATOR")
name=input("Enter your name = ")
weight = float(input("Enter your weight in pounds = "))
height = float(input("Enter your height in inches = "))
bmi = weight* 703/ (height * height)
print(bmi)
if(bmi>0):
    if(bmi <= 18.5):
        print(name+",you are Underweight")
    elif( bmi >= 18.5 and bmi < 25):
        print(name+", you are Normal")
    elif(bmi >= 25 and bmi < 30):
        print(name+",you are Overweight")
    elif(bmi >= 30):
        print(name+", you are Obese")
    else:
        print(name+",you are severly obese")
else:
    print("enter an valid input")
