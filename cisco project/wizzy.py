# this is my customer service
user_name=(input("pls input your name:"))
print(user_name,"You are welcome to my customer service","i am a robot \n and i am here to resolve your problem providing you ask the required questions\n,please remember i am a robot")
A=str,float("the money transferred ")
B=str,float("The money transferred was not recieved ")
C=str,float("the website is giving me some issues ")
D=str,float("The money placed on the goods are too high ")


while True:
        choice = input("Enter choice(1/2/3/4): ")
        first_check = str(input("is your complaint  listed above "))
        if first_check == "no":
                print("please try reinstalling the app in order to fix the problem ")
        else:
                print("i am a robot")


    # check if choice is one of the four options
        if choice in ('1', '2', '3', '4'):



        if A=="yes"  :
                print("Sorry the problem will be fixed it is the fault of our network")
                 print("maybe you should try closing the app and opening again ")
        elif B=="yes":
                print(" that will be rectified right now ")
        elif C=="yes":
                 print("print the website is still under construction right now soo\ncheck back next week it will be fixed by then")
        elif D=="yes":
                print ("We are sorry about that but that is the fixed price for those goods because of their standards ")



