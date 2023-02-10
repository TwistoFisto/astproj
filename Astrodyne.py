#Astrodyne?
import math


gcdspeed = 2.41
gcdspeed_hasted = gcdspeed-(gcdspeed/10)

gcdspeed_hasted_display = str(round(gcdspeed_hasted,2))

print(gcdspeed_hasted_display)

GCD_Count = 15/gcdspeed_hasted
print(GCD_Count)

GCD_Count2 = 15/gcdspeed
print(GCD_Count2)
#
#cutaway = gcdspeed - gcdspeed_hasted
#print(cutaway)