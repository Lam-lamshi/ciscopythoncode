print("HI,you are welcome to LAM APP")
user_name=str(input("please input your name? :"))
acc_details=1000
choice=0
mtn=1
glo=2
airtel=3
nmobile=4

choice=int(input ("PLEASE ENTER YOUR NETWORK PROVIDER_____\n"
                  "*********************\n"
                  "ENTER1:mtn\n"
                  "ENTER2:glo\n"
                  "ENTER3:airtel\n"
                  "ENTER4:nmobile\n"
                  "******************* : "
                  ""))
mb_100=1
mb_200=2
mb_2gb=3
mb_10gb=4
if choice ==mtn:
    data_bundle= int(input(""
                           "******************\n"
                           "ENTER 1 :100MB for 50NGN\n"
                           "ENTER 2 : 200mb for 100NGN\n"
                           "ENTER 3 : 2gb for 500NGN\n"
                           "ENTER 4 : 5gb for 1000NGN\n"
                            "ENTER 5 : 10gbm for 10000NGN\n"
                           "*******************\n"
                           ""))
    if acc_details >0 :
        if  data_bundle==mb_100:
            if acc_details>=50:
                print("congratulation you have successfully bought 100mb data bundle for 1 night")
            else :
                print("insufficient fund.please recharge")
        elif data_bundle==mb_200:
            if acc_details>= 100:
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

# purchase for glo
if choice ==glo:
    data_bundle= int(input(""
                           "******************\n"
                           "ENTER 1 :100MB for 50NGN\n"
                           "ENTER 2 : 200mb for 100NGN\n"
                           "ENTER 3 : 2gb for 500NGN\n"
                           "ENTER 4 : 5gb for 1000NGN\n"
                            "ENTER 5 : 10gbm for 10000NGN\n"
                           "*******************\n"
                           ""))
    if acc_details >0 :
        if  data_bundle==mb_100:
            if acc_details>=50:
                print("congratulation you have successfully bought 100mb data bundle for 1 night")
            else :
                print("insufficient fund.please recharge")
        elif data_bundle==mb_200:
            if acc_details>= 100:
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


if choice ==airtel:
    data_bundle= int(input(""
                           "******************\n"
                           "ENTER 1 :100MB for 50NGN\n"
                           "ENTER 2 : 200mb for 100NGN\n"
                           "ENTER 3 : 2gb for 500NGN\n"
                           "ENTER 4 : 5gb for 1000NGN\n"
                            "ENTER 5 : 10gbm for 10000NGN\n"
                           "*******************\n"
                           ""))
    if acc_details >0 :
        if  data_bundle==mb_100:
            if acc_details>=50:
                print("congratulation you have successfully bought 100mb data bundle for 1 night")
            else :
                print("insufficient fund.please recharge")
        elif data_bundle==mb_200:
            if acc_details>= 100:
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


if choice ==nmobile:
    data_bundle= int(input(""
                           "******************\n"
                           "ENTER 1 :100MB for 50NGN\n"
                           "ENTER 2 : 200mb for 100NGN\n"
                           "ENTER 3 : 2gb for 500NGN\n"
                           "ENTER 4 : 5gb for 1000NGN\n"
                            "ENTER 5 : 10gbm for 10000NGN\n"
                           "*******************\n"
                           ""))
    if acc_details >0 :
        if  data_bundle==mb_100:
            if acc_details>=50:
                print("congratulation you have successfully bought 100mb data bundle for 1 night")
            else :
                print("insufficient fund.please recharge")
        elif data_bundle==mb_200:
            if acc_details>= 100:
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


