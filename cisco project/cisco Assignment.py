import math
b =int(input("enter_the_value_of_the_base"))
h=int(input("enter_the_value_of_the_height"))
area=(b*h)/2
print(area)

#volume of a sphere
pie=3.142
r=int(input("enter_the_value_of_the_raduis"))
volume=(4*pie*r*r*r)/3
print(volume)

#area of an equilateral triangle
a=int(input("enter_the_value_of_the_lenght"))
_area_equi =math.sqrt(3)/4*a*a
print(_area_equi)

#volume of a cubiod
a=int(input("enter_the_value_of_the_lenght"))
volume_of_cubiod=a*a*a
print(volume_of_cubiod)

#mechanical_advantage
Fo=int(input("enter_the_value_of_the_output"))
Fi=int(input("enter_the_value_of_the_input"))
MA=Fo/Fi
print(MA)

#electric_potential
q=int(input("enter_the_value_of_the_charge_particle"))
r=int(input("enter_the_value_of_the_raduis_of_the_charge"))
k=24
columb_constant=(k*q)/r
print(columb_constant)

#gravitational force
M1=int(input("enter_the_value_of_the_first_mass"))
M2=int(input("enter_the_value_of_the_second_mass"))
R=int(input("enter_the_value_of_the_raduis"))
G=6.6743*(10^11)
F=(G*M1*M2)/7*7

#half life
K=0.693
λ=int(input("enter_the_value_of_the_Lambda"))
Half_life=K/λ
print(Half_life)

#electric_force
k=34
q1=int(input("enter_the_value_of_the_first_columb_particle"))
q2=int(input("enter_the_value_of_the_second_columb_particle"))
r=int(input("enter_the_value_of_the_raduis"))
EF=k*(q1*q2)/r*r
print(EF)




