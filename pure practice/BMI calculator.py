height =float(input("Enter your height in m : "))
weight = float(input("Enter your weight in kg :"))
BMI= round(weight/(height ** 2))
if BMI<18.5 :
    print(f"your bmi is {BMI},you are under weighted ")
elif  BMI< 25 :
    print(f"your bmi is {BMI},you have a normal weigth ")
elif  BMI<=30:
    print(f"your bmi is {BMI},you are overweight ")
elif BMI<=35:
    print(f"your bmi is {BMI}, you are obese ")
else :
    print(f"your bmi is {BMI},You are clinically obese ")

