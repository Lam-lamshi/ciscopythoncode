user_name=float(input(" pls enter your name "))
print(" Hi", user_name,"You are welcomed to lam`s atm machine")
print("please input your card")
user_acc=float(input(""))
acc_details=1000
choice=0
current=1
savings=2
checking=3

choice=int(input ("PLEASE ENTER YOUR acouunt type_____\n"
                  "*********************\n"
                  "ENTER1:current\n"
                  "ENTER2:savings\n"
                  "ENTER3:checking\n"
                  "******************* : "
                  ""))
Ng_500=1
Ng_1000=2
Ng_1500=3
Ng_2000=4
Ng_2500=6
Ng_3000=7
Ng_3500=8
Ng_4000=9
Ng_4500=10
Ng_5000=11
Ng_5500=12
Ng_6000=13
Ng_6500=14
Ng_7000=15
Ng_7500=16
Ng_8000=17
Ng_8500=18
Ng_9000=19
Ng_9500=20
Ng_10000=21
Ng_10500=22
Ng_11000=23
Ng_11500=24
Ng_12000=25
Ng_12500=26


if choice ==current:
    data_bundle= int(input(""
                           "******************\n"
                           "ENTER 1 :Ng_500 for 50NGN\n"
                           "ENTER 2 : Ng_1000 for 100NGN\n"
                           "ENTER 3 : Ng_1500 for 500NGN\n"
                           "ENTER 4 : Ng_2000 for 1000NGN\n"
                            "ENTER 5 : Ng_2500 for 10000NGN\n"
                           "ENTER 6 :Ng_3000  for "
                           "*******************\n"
                           ""))
    if acc_details >0 :
        if  data_bundle==Ng_500:
            if acc_details>=50:
                print("congratulation you have successfully bought 100mb data bundle for 1 night")
            else :
                print("insufficient fund.please recharge")
        elif data_bundle==mb_200:
            if acc_details>= 100
                print(user_name,"congratulation you have 200mb for 7 days")
            else :
                print(user_name,"insufficient fund, please recharge")

        elif data_bundle==mb_2gb:
            if acc_details>=500:
                print(user_name,"you have successfully purchased 2gb for 3weeks ")
            else :
                print(user_name,"insufficient fund , please recharge")

        elif data_bundle==mb_5gb:
            if acc_details>=1000:
                print(user_name,"you have successfully purchased 5gb for 1 month ")
            else :
                print(user_name,"insufficient fund , please recharge")

        elif data_bundle == mb_10gb:
            if acc_details >= 10000:
                print(user_name, "you have successfully purchased 10gb for 1 month ")
            else:
                print(user_name, "insufficient fund , please recharge")

