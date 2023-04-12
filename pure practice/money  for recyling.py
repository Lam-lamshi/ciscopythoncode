less_money=0.10
more_money=0.25
less=float(input("how many containers 1l or less do you have"))
more=float(input("how many  container 1l or more  do you have "))
refund=less+less_money*more+more_money
print("your total refund will be $ %.2f"%refund)
