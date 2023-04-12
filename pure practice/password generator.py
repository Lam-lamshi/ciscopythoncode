import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="[]{}()*;/,._-"


all=lower + upper +numbers+symbols
length=8
password="".join(random.sample(all,length))
word=str(input (" enter any number to get list of wifi connection  "))

while word !=0:
    for q in range(1,password):
        print("")
        word+=1
    word=str(input("enter any number to get list of wifi connection "))

print(password)