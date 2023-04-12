##
#
# reading the input from the user
nsides =int(input("Enter the number of sides of the shape you want : "))

name=""

if nsides==3:
   name:str="triangle "
elif nsides==4:
    name:str= "  quadrilateral"
elif nsides==5:
    name:str= " pentagon "
elif nsides==6:
    name:str=" hexagon"
elif nsides==7:
    name:str= " heptagon "
elif nsides==8:
     name:str=" octagon "
elif nsides ==9:
    name:str="nonagon "
elif nsides ==10:
    name:str=" decagon "



if name=="":
    print("the nsides is not supported by this app.")
else :
    print("That's a ", name)

