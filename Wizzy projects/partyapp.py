print("hi i am the party bot")
user_name = str(input("please input your name:"))
user_age = float(input("please input your age:"))
if user_age <= 15 :
    print("Hi", user_name,"your section is in the regulars")
elif user_age >= 15 and user_age <= 20:
    print("hi",user_name,"you belong to the vip section")
elif user_age>= 20:
    print ("HI",user_name,"You belong to the vvip section")
else:
    print("Hi",user_name,"incorrect or age  not entered")

    #program to calculate the cgpa of a student
user_name = str(input("please input your name:"))
user_age = float(input("please input your age:"))
cgpa=float(input("enter your cgpa:"))
if 4.5<= cgpa <=5.0:
        print("congratulation you have first class")
elif 3.5<=cgpa<=4.4:
        print("you have second class")
elif 2.29<=cgpa<=3.49:
        print("you have third class")
elif 1.0<=cgpa<=1.49:
        print ("you do not have the credibility to graduate ")
else:
     print ("you have no record")

