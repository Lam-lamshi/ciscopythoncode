price_of_bread=3.49
discount_on_bread=0.69

num_of_loaves=int(input("Enter the number of loaves ypu want : "))
regular_price=num_of_loaves*price_of_bread
discount =discount_on_bread*regular_price
total=regular_price-discount

print("the regular price is %5.2f" %regular_price)
print("the discount price is %5.2f" %discount)
print("the total price will be %5.2f" % total)

