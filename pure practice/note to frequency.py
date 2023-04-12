C4_FREQ=261.63
D4_FREQ=293.66
E4_FREQ=329.63
F4_FREQ=349.23
G4_FREQ=392.00
A4_FREQ=440.00
B4_FREQ=493.88

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

name=input ("Enter two frequency note like C4 : ")
note=name[0]
octave=int(int (name[1]))
freq = ""


if note =="C":
    freq:float=C4_FREQ
elif note =="D":
    freq:float=D4_FREQ
elif note == "E":
    freq:float=E4_FREQ
elif note == "F":
    freq:float=F4_FREQ
elif note == "G":
    freq:float= G4_FREQ
elif note=="A":
    freq:float=A4_FREQ
elif note =="B":
    freq: float =B4_FREQ

frequency = freq/ 2 ** (4- octave)
if freq=="":
    print("the freq is not listed ;  ")
else:
    print("this frequency of ", name,"is",freq)
