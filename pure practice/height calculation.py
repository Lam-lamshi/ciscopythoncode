ft_per_in=12
in_per_cm=2.54
user_name=str(input("Enter your name : "))
feet=int(input("Enter your height in feet : "))
inches=int(input("Enter your height in inches : "))
cm=(feet*ft_per_in+inches)*in_per_cm
print("your height in centimeters is : ",cm)