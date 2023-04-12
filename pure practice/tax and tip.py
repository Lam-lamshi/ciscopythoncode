
user_name=str(input("Enter you name : "))
tip_rate =0.05
tax_rate=0.18
amt_of_meal=float(input("Enter the amount of meal you have eaten in dollars : $"))
tax=tax_rate*amt_of_meal
tip=tip_rate*amt_of_meal
total=tax+amt_of_meal+tip
print(user_name,"the tax is  %.2f, the tip is %.2f, the total is $ %.2f" % \
      (tax,tip,total))