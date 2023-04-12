side1=int(input("enter the lenght of side 1 :"))
side2=int(input("enter the lenght of side 2 :"))
side3=int(input("enter the lenght of side 3 :"))


if side1==side2 and side2==side3:
    name:str="equilateral"
elif side1==side2 or side2==side3 or side3==side1:
    name: str = "isoceles"
else:
    name: str = "scalene"
print("thats a ",name,"triangle . ")12