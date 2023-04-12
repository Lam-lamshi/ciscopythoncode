print( "Hi,Welcome to my calculator ")
user_name=(str(input("please input your name  ")))
n = int(input("Please Enter any Number: "))
print("The List of Natural Numbers from 1", "to", n)
for i in range(1, n + 1): print (i, end = ' ')

# the formula to calculate the value of kelvin
T=273
K=int(input("input the value of the kelvin: "))
C=K+T
G="HI",user_name,"this is the value of your celcuis: "
print(G,C)
# check if user wants another calculation
# break the while loop if answer is no
next_calculation = input("Let's do next calculation? (yes/no): ")
if next_calculation == "no":
     "break"

else:
    print(C)
F=9/5*(C+35)
D= "Hi",user_name, "This is the value of your farenheit:"
print (D,F)
