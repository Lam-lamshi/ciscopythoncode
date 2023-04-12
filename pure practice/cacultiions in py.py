print("You are welcome to our Dating app")
user_name=input("Enter your name: ")
wiz=int(input("Enter your age in order to get your age limit for dating:"))
#to calculate the age limit
def allowed_dating_age(my_age):
    girls_age= my_age/2 + 7
    return girls_age
wisdom_limit = allowed_dating_age(wiz)
print(user_name,f"can date girls,{wisdom_limit},or older")



