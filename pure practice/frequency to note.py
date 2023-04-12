C4_FREQ=261.63
D4_FREQ=293.66
E4_FREQ=329.63
F4_FREQ=349.23
G4_FREQ=392.00
A4_FREQ=440.00
B4_FREQ=493.88
Limit=1

print(" The number of listed frequency needed for input are : "
       "*********** \n"
       "C4 \n"
       "D4 \n"
       "E4 \n"
       "F4 \n"
       "G4 \n"
       "A4 \n"
       "B4 \n"
       "***********\n")

note=" "

freq=float(input("Enter the frequency : "))


if freq >= C4_FREQ - Limit and freq <= C4_FREQ + Limit :
    note:float="C4"
elif freq >= D4_FREQ - Limit and freq<= D4_FREQ + Limit :
    note:float="D4"
elif freq >= E4_FREQ - Limit and freq <= E4_FREQ + Limit :
    note:float="E4"
elif freq >= F4_FREQ - Limit and freq <= F4_FREQ + Limit :
    note:float="F4"
elif freq >= G4_FREQ - Limit and freq <= G4_FREQ + Limit :
    note:float="G4"
elif freq >= A4_FREQ - Limit and freq <= G4_FREQ + Limit :
    note:float="A4"
elif freq >= B4_FREQ- Limit and freq <= B4_FREQ + Limit :
    note:float="B4"
else :
    note =""

if note =="":
    print("there is no note that match that frequency ")
else:
    print("That frequency is", note)

