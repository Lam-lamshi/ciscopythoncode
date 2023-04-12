cents_per_Tonnie=200
cents_per_lonnie=100
cents_per_quarter=25
cents_per_dime=10
cents_per_Nickel=5
cents=float(input("Enter the amount of your change :"))
print("",cents// cents_per_Tonnie,"Tonnie")
cents= cents % cents_per_Tonnie
print("",cents// cents_per_lonnie,"lonnie" )
cents=cents% cents_per_lonnie
print("", cents // cents_per_quarter,"quarter")
cents=cents %  cents_per_quarter
print("",cents // cents_per_dime,"dime")
cents= cents % cents_per_dime
print("",cents // cents_per_Nickel,"Nickel" )
cents= cents % cents_per_Nickel
print("",cents," pennies")