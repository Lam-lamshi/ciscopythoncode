#collect the name of the ten student
weight=[]
names=[]
sum=0
n=2
#collect the weight of the ten students
for x in range(n):
    name = input("Enter your name ")
    w=float(input("Enter the weight kg  : "))
    weight.append(w)
    names.append(name)
for i in weight :
    sum+= i
for y in names:
    print(y,":",i)
avg=sum/n
print(avg)
for y in range (len(weight)):
    print(names[y],":",weight[y])


price_of_bread=3.49
discount_on_bread=0.69

num_of_loaves=int(input("Enter the number of loaves ypu want : "))
regular_price=num_of_loaves*price_of_bread
discount =discount_on_bread*regular_price
total=regular_price-discount

print("the regular price is %5.2f" %regular_price)
print("the discount price is %5.2f" %discount)
print("the total price will be %5.2f" % total)


