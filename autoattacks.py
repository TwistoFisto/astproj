import math
#import pandas as pd

#testvalues
WeaponDelay =3.36
WeaponDamage = 126
aap= 141.12


#source reddit:
AutoAttackPotency = WeaponDelay/3.00*WeaponDamage
print(AutoAttackPotency)
#this autoattack value correlates to the stat of the abyssos war axe rounded up. Which would be 141.12 (got 141.11999999999999)


#So over the course of 1 server tick (3s) all autos will deal upwards of 100p
#PPS is calculated as PPS = Potency/Time
#To find the PPS of 1s for war we do 100/3 which should give us 33.3 recurring?



#However according to Opener Burst Cal by Marielle Kaidafaux on Adamanoise from the Fey Temperance Discord has these values for wAR:
"""
Auto potency: 100.8
Auto Delay: 3.36
Base Auto PPS: 30.00
"""
lvlModifier_Main = 390
attackpower = 105
wd = 126
weaponDelay = 3.36
strength = 2910
lvlAttackModifier = 195
#f(AUTO) = ⌊ ( ⌊ LevelModLv, Main · JobModJob, Attribute / 1000 ) + WD ⌋ · ( Weapon Delay / 3 ) ⌋
autos = ((390*105)/1000)+126*(3.36/3)
print(autos)


#*105
Potency = 110
atk = math.floor(lvlAttackModifier * (strength - lvlModifier_Main) / lvlModifier_Main + 100) / 100.0
#D1 = Potency*atk/100
#D2 = D1*autos/100
#print(D2)




