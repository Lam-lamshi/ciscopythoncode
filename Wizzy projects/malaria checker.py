print("Hi, i am your malaria checker ")
user_name = str(input("please input your name:"))
user_age = float(input("please input your age:"))
med_1=(float,str('Cough Medicine,\nStay Hydrated,\nSip Warm Tea, \nTake a Hot Bath or Shower.'))
med_2=(float,str('you can try Layering clothes or getting to a warm place'))
med_3=(float,str('you have to Rest and drink plenty of fluids'))
med_4=(float,str('ibuprofen (Advil, Motrin IB, others) , aspirin.'))
med_5=(float,str('drink plenty of fluid and ave a good rest'))
med_6=(float,str('Eat ginger\nPeppermint aromatherapy\nAcupuncture or acupressure\nLemon. ...'))
med_7=(float,str('take paracetamol and have enough rest'))
med_8=(float,str('Drinking gradually larger amounts of clear liquids\nAvoiding solid food until the vomiting episode has passed'
                  '\nRestingTemporarily discontinuing all oral medications, which can irritate the stomach and make vomiting worse'))
med_9=(float,str('try resting the area of the body where you are experiencing aches and pains'))
med_10=(float,str('Drink plenty of clear fluids such as water,\nReduce your intake of coffee, tea and alcohol as these can make the pain worse'))
med_11=(float,str('Breathe through pursed lips,\nBreathe slowly into a paper bag or cupped hands\n'
                  'Attempt to breathe into your belly (diaphragm) rather than your chest\n'
                  'Hold your breath for 10 to 15 seconds at a time.'))
disease_checker= float,str(input( "i am here to check if you have malaria\n please press ENTER"))
print("1.cough")
print("2.chills")
print("3.fever")
print("4.high temperature")
print("5.General feeling of discomfort")
print("6.Nausea ")
print("7.Headache.")
print("8.vomiting.")
print("9. Muscle or joint pain")
print("10. Abdominal pain")
print ("11.Rapid breathing")
print("if you have any of the following symptoms that means you have a sign of malaria")

while True:

    first_check = str(input("do you have malaria"))
    if first_check == "no":
        print("kindly exit the app")
        break
    else:
        print(" will you like to take any of the advice listed below or\nVisit a doctor .")
    choice = int(input("Enter the available symptoms \n from the listed ones above \n****************\n(1/2/3/4/5/6/7/8/9/10/11) \n******************* : "))
if "choice"  in('1' ,'2','3','4','5','6','7','8','9','10','11'):

    if choice == '1':
            print(med_1)

    elif choice == '2':

           print(med_2)

    elif choice == '3':

            print(med_3)
    elif choice == '4':
            print(med_4)

    elif choice == '5':
             print(med_5)

    elif choice == '6':
            print(med_6)

    elif choice == '7':
            print(med_7)

    elif choice =='8':
            print(med_8)

    elif  choice == '9':
            print(med_9)

    elif choice == '10':
            print(med_10)

    elif  choice == '11':
          print(med_11)
    else:
        print("you will have see a doctor")
    next_check = input("Do you want to take another review ? (yes/no): ")

    if next_check == "no":
        print(user_name,"I hope you got your results. ")

        break

    else:
             print(user_name,"Thank you for your patronage.")