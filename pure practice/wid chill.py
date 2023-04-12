WC_OFFSET=13.12
WC_FACTOR1=0.6215
WC_FACTOR2=-11.37
WC_FACTOR3=0.3965
WC_EXPONENT=0.16
Temp=float(input("Enter the temp in celsius : " ))
speed=float(input("Enter the speed in kilometers per hour :" , ))

wci=WC_OFFSET+ \
    WC_FACTOR1* WC_OFFSET+\
    WC_FACTOR2 *speed *WC_EXPONENT + \
    WC_FACTOR3 *Temp * speed ** WC_OFFSET
print("the chill index is:  ", round(wci))