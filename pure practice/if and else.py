height =int(input("Enter your height : "))
bill=0
if height >= 120 :
    print("You can ride the roller coster ! ")
    age=int(input("Enter your age "))
    if age< 12:
        bill=5
        print("child tickets are $5.")
    elif age<=18:
        bill=7
        print("youth tickets are  $7.")
    elif age>=45 and age <= 55:
        print("Everything is going to be ok.Have a free ride on us. ")
    else:
        bill=12
        print("adult tickets are  $12.")
    picture=input("do you want photos on your ride : ")
    if picture == "yes" :
        bill +=3
    print(f"your final bill is ${bill}")

else :
    print("sorry you are not up to the height range !.")
