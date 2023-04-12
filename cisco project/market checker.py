#to do list
#she likes to save the money
#what will be her compound interest for five years
def received(a, b):
    print(a, "+", b,"=","₦",(a + b ))
what=int(input("Enter the number  of things you have to buy : "))
money=[]
names = []
sum=0

n = what
acc_on=int(input("Enter the estimated  amount of money budgeted :₦ "))
# collect the items bought
for x in range(n):
    name = input("Enter the name of the item : ")
    amount=float(input("Enter the amount of the item  :₦"))
    names.append(name)
    money.append(amount)
for i in money:
    sum+= i
for y in range (len(money)):
    print(names[y],":","₦",money[y])
# the calculation of the average of the expences
total:str=sum+n
print("the total amount of your money is ₦ %.3f"%total)
minus=acc_on-total
if total > acc_on:
    print(" and the amount of expenses is over the budgeted amount of money and \nat this  rate there will be no amount left to save   ")
else:
    print("the remaining amount of money is ₦ %.3f" %minus)


dis_received=str(input("enter the discount if any(Enter  the amount )\n(And if not Enter none) :₦ "))
mon_received=str(input("enter the amount of money received from anyone if any(enter the amount)\n (And if not Enter none) :₦ "))

if dis_received== str("none") and mon_received==str("yeah"):
        print(mon_received+total)

elif dis_received== str("yeah") and mon_received==str("none"):
        print(dis_received+total)
else:
        print(received(dis_received,mon_received))

