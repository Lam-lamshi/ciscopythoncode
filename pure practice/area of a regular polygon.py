from math import tan,pi
s=int(input("Enter the lenght of each number of sides  : "))
n=int(input("Enter the number of sides : "))
area=(n * s ** 2) /  (4 * tan( pi / n))
print("The area of the regular polygon %.2f" % area)