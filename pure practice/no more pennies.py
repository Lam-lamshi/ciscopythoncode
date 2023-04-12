pennies_per_nickels=5
nickels=0.05

total=0.00
line =input("Enter the price of the item (blank to quit ): ")
while line != "":
    total=total + float(line)
    line=input("Enter the price of the item (blank to quit ):")
    print("the amount that is payable is %.02f"%total)
rounding_indicators=total*100 % pennies_per_nickels
if rounding_indicators<pennies_per_nickels/2 :
    cash_total=total-rounding_indicators /100
else:
    cash_total=total+nickels-rounding_indicators/100
print("the amount payable is %.02f"%cash_total)
