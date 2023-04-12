from math import sqrt
gravity = 9.8
d=float(input("Height  from which the object fell from "))
vf = sqrt(2 * gravity * d)
print("the free fall of the object is %.3f " % vf)
