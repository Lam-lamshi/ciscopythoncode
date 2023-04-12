# program to solve almighty formula
import cmath
from random import choice
print( "Hi,Welcome to my  calculator for quadractic equation ")
user_name=(str(input("please input your name:  ")))
A=int(input("_insert_the_the_value_of_the_first_value_A:"))
B=int(input("_insert_the_value_of_the_second_term_B:"))
C=int(input("_insert_the_value_of_the_third_term_C:"))
d=(B*B)-(4*A*C)
sol1 = (-B-cmath.sqrt(d))/(2*A)
sol2 = (-B+cmath.sqrt(d))/(2*A)
print('The solution are {0} and {1}'.format(sol1,sol2))
# this is my  calculator
print( "Hi",user_name,"Welcome to my calculator:")
def add(x,y):
    return x+y
def multiply(x,y):
    return x*y
def subtract(x,y):
    return x-y
def divide(x,y):
    return x/y
print("select operation:")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

while True:
    choice= input("Enter choice(1/2/3/4) : ")
    if choice in("1", "2", "3", "4"):
        num1=float(input("enter the first number: "))
        num2=float(input("enter the second number:"))

    if choice == "1":
             print(num1,"+",  num2, "=",add(num1 , num2 ))

    elif choice == "2":
             print(num1,"-",num2,"=",subtract(num1 , num2))

    elif choice == "3":
             print(num1 ,"*" ,  num2 ,"=", multiply(num1,num2))

    elif choice == "4":
              print(num1,"/",num2,"=", divide(num1,num2))
        #check if user want another calculation
        #break the while loop if the answer is no

    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
        break

    else:
                print("Invalid Input")



#a program to calculate the nth term of an ap
print( "Hi",user_name,"Welcome to my nth term calculator:")
a=int(input("please insert the first term:"))
n=int(input("please input the number of term of the AP:"))
d=int(input("please input the common difference of the AP:"))
Tn=a+(n-1)*d
print(Tn)

# a program to calculate gp
print( "Hi",user_name,"Welcome to my G.p  calculator:")
a=int(input("please insert the first term:"))
r=int(input("please insert the common ratio of the gp:"))
n=int(input("please input the the no of terms:"))
Tn=a*r^(n-1)
print(Tn)


#program to solve the sum of an AP
print( "Hi",user_name,"Welcome to my sum of a AP calculator:")
a=float(input("please insert the first term:"))
n=float(input("please input the number of term of the AP:"))
d=float(input("please input the common difference of the AP:"))
Sn= n * ( ( 2*a + (n-1) * d)/2)
print(Sn)


#program to calculate the sum of a GP
print( "Hi,Welcome to my Sum of a Gp calculator:")
user_name=(str(input("please input your name : ")))
a=float(input("please input the first term:"))
r=float(input("please input the common ratio:"))
Sum_to_infinity=(1-r)/a
print(Sum_to_infinity)

# the formula to calculate the value of kelvin
print( "Hi,Welcome to my temperature calculator:")
user_name=(str(input("please input your name : ")))
T=273
K=int(input("input the value of the kelvin: "))
C=K+T
Y="This is the value of your celcuis"
print(Y,C)
#this is to calculate the value if your farenheit
U=int(input("please input the value of your celcuis:"))
F=9/5*(C+35)
D= " This is the value of your farenheit"
print (D,F)
#this is to generate matric number generator
input("please input your name ")
