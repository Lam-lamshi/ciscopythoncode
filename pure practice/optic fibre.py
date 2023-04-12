#  a programme to calculate the value of light passing through a glass
#speed of light in a vacuum
import math
c = (3*(10**8))
# speed of light in glass
b= (1.88*(10**8))
#what do you want to calculate
print("Led= speed light in a vaccum ")
print("Light=speed of light in a glass")
# list of things there ar to calculate
Led = "speed of light in a vacuum "
Light = " speed of light in glass"
n = int(input("enter the number of things you want to calculate:"))
numbers_of_times = []

# n=c/v
for x in range(n):
   SPD = input("what do you want to calculate : ")
   R_I = input("enter the value of the refractive index:")
   numbers_of_times.append(R_I)
   numbers_of_times.append(SPD)
   H = c*R_I
   G = b*R_I

def SPD():
   if SPD == Led:
      if SPD == Light:
         print("the value of spped in glass is ", H)
   print("the value of the speed in a vacuum is ", G)

SPD()


