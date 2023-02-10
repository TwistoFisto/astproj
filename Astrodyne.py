#Astrodyne?
from random import triangular
import pandas as pd
import math


#these variables can be shifted so it's user inputed.
#gcdspeed = 2.41
gcdspeed = 2.34
#gcdspeed = float(input("GCD speed: "))
gcdspeed_hasted = gcdspeed-(gcdspeed/10)
SecondSlot = True

movenamelist = pd.read_csv('justframecards-BasePotencies.csv')
movenamelist["Movename"] = movenamelist["Movename"].str.lower()

job_moves = movenamelist.query("Class == 'AST'")
a = len(job_moves.index)
print(a)
print(job_moves.to_string())


gcdspeed_hasted_display = str(round(gcdspeed_hasted,2))

print(gcdspeed_hasted_display)

#for if it's woven on 2nd slot or not.
if SecondSlot == True:

    GCD_Count = (15/gcdspeed_hasted) + 1
    GCD_Count = math.floor(GCD_Count)
    print("GCDs: ",GCD_Count)

else:
    GCD_Count = (15/gcdspeed_hasted)
    GCD_Count = math.floor(GCD_Count)
    print(GCD_Count)

#eh
if GCD_Count == 8:
    extra_malefic = 250


#astrodyne_gain







"""
idk what this is
GCD_Count2 = (15/gcdspeed) + 0.5
print(GCD_Count2)
"""



#
#cutaway = gcdspeed - gcdspeed_hasted
#print(cutaway)