print("welcome to python pizza delivery !")
size=input("What size of pizza do you want ? S,M,L :")
add_pepperoni=input("Do you want pepperoni ? y/n :")
extra_cheese=input("do you want extra cheese ?  : ")

bill=0
if size == "S":
    bill = 15
    if  add_pepperoni  == "y":
        bill += 2
        if extra_cheese == "y":
            bill += 1
            print(f"your total bill  would be {bill} ")
        else:
            print(f"your total bill would be {bill}")
    else:
        bill=15
        print(f"your total  bill would be {bill}")
elif size =="M":
    bill=20
    if  add_pepperoni  =="y":
        bill +=3
        if extra_cheese == "y":
            bill += 1
            print(f"your total bill  would be {bill} ")
        else:
            print(f"your total bill would be {bill}")
    else:
        bill=20
        print(f"your total  bill would be {bill}")
elif size =="L":
    bill=25
    if  add_pepperoni  =="y":
        bill +=3
        if extra_cheese == "y":
            bill += 1
            print(f"your total bill  would be {bill} ")
        else:
            print(f"your total bill would be {bill}")
    else:
        bill=25
        print(f"your total  bill would be {bill}")
