water_heat_capacity=4.186
electricity_price=8.6
J_to_KWH=2.777e-7

volume = int(input("Enter the amount of volumes in millimeters : "))
d_temp= int (input (" Enter the increase in temperature : "))
q=volume*d_temp*water_heat_capacity

print("that will require %d joules of energy  "  %q )
KWH=q*J_to_KWH
cost=KWH*electricity_price
print("that much energy will require %.2f cents" %cost )
