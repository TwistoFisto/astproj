#Astrodyne?
from random import triangular
import pandas as pd
import math

#currently a prototype file, it'll need to be organised into functions, afterwards so it works with the main file.


#these variables can be shifted so it's user inputed.
#gcdspeed = 2.41
gcdspeed = 2.5
#gcdspeed = float(input("GCD speed: "))
gcdspeed_hasted = gcdspeed-(gcdspeed/10)
SecondSlot = False
trait_modifier = 1.3 #maim and mend modifier


dh = 1012
det = 1752
crit = 2257
ten = 123
gcd = 2500
spd = 803
strength = 2936 #mainstat

lvlModifier_Sub = 400   
lvlModifier_Div = 1900
lvlModifier_Main = 390
weaponBaseDamage = 126
lvlAttackModifier = 195
AttackPower = 115 #from jobmodifiers for AST (it's the job's main stat)

movenamelist = pd.read_csv('justframecards-BasePotencies.csv')
movenamelist["Movename"] = movenamelist["Movename"].str.lower()

job_moves = movenamelist.query("Class == 'AST'")
a = len(job_moves.index)
print(a)
print(job_moves.to_string())
malefic = job_moves.loc[job_moves["Movename"] == "fall malefic"]
combust = job_moves.loc[job_moves["Movename"] == "combust 3"]
lord_of_crowns = job_moves.loc[job_moves["Movename"] == "lord of crowns"]
earthly_star = job_moves.loc[job_moves["Movename"] == "earthly star"]
print(malefic)

#gets base malefic potency and calculates modified potency under maim and mend
malefic_base = malefic.iloc[0,3]
combust_base = combust.iloc[0,3]
lordOfCrowns_base = lord_of_crowns.iloc[0,3]
earthlyStar_base = earthly_star.iloc[0,3]

print(float(malefic_base))
malefic_base = float((malefic_base))
modified_malefic = float(malefic_base) * trait_modifier
print(modified_malefic)

#Getting values of other AST dps abilities:
combust_base = float(combust_base)
modified_combust = combust_base * trait_modifier

lordOfCrowns_base = float(lordOfCrowns_base)
modified_lordOfCrown = lordOfCrowns_base * trait_modifier

#idk precisely how earthly star dmg is calculated so I'm using a simple dmg final modifier for potency.
#As for actual dmg it's very scuffed from what I've looked at it... the 0.9 is the general damage reduction for AST's earthly star.
earthlyStar_base = float(earthlyStar_base)
modified_earthlyStar = (earthlyStar_base * 0.9) * trait_modifier

print()
print("Earthly Star modified potency:",modified_earthlyStar)
print()

#After getting the base malefic potency, we'll need to calculate the average potency of malefic, this accounts for player stats so mind, crit, det, dhit, etc... (done?)


#f(atk) - this is just calculating the function of attack power. Strength here is the mainstat,
#it should be renamed to mind due to the context being mostly AST. But they're the same thing in function, just named differently,
#especially how all characters at BiS lvl have the same main stat :)
atk = math.floor(lvlAttackModifier * (strength - lvlModifier_Main) / lvlModifier_Main + 100) / 100.0


Dh = math.floor(550 * (dh - lvlModifier_Sub) / lvlModifier_Div) / 1000
Det = math.floor(140 * (det - lvlModifier_Main) / lvlModifier_Div) / 1000
CritD = math.floor(200 * (crit - lvlModifier_Sub) / lvlModifier_Div + 1400) / 1000
CritC = math.floor(200 * (crit - lvlModifier_Sub) / lvlModifier_Div + 50) / 1000
WeaponDamage = math.floor(lvlModifier_Main * AttackPower / 1000.0 + weaponBaseDamage) / 100.0
baseDamage = math.floor(math.floor(math.floor(100 * atk * WeaponDamage) * (1 + Det))) * trait_modifier
#I'm not sure where the trait modifier goes, according to character panel refined the trait modifier goes at the base dmg. However I think this is wrong?



#approximate dmg for every 100 potency.
avgDamage = math.floor(baseDamage * (1 + (CritD - 1) * CritC) * (1 + Dh * 0.25))


#This calculates your GCD speed under Astrodyne haste buff.
gcdspeed_hasted_display = str(round(gcdspeed_hasted,2))
print(gcdspeed_hasted_display)


#This calculates how many GCDs we'll catch under Astrodyne buff, but because this ability can be woven on 1st or 2nd slot of a GCD cycle
#it'll affect how many GCDs we'll get under the buff, depending on the SPS stat of the AST.
"""if SecondSlot == True:
    GCD_Count = (15/gcdspeed_hasted) + 1
    GCD_Count = math.floor(GCD_Count)
    print("GCDs: ",GCD_Count)

else:
    GCD_Count = (15/gcdspeed_hasted)
    GCD_Count = math.floor(GCD_Count)
    print("GCDs: ",GCD_Count)
"""
#There's a slight problem with this setup, while it does find how many GCDs you can fit under Astrodyne, it's a little bit "too accurate"
#So 2.38 GCD speed can theoretically fit 8 GCDs, but the big catch is that the timing required on the 2nd weave is tighter than my ass to consistenctly get.
#So at most, 2.34 is roughly the human limit for 8 GCDs consistently. 2.35 is doable, but a little bit inconsistent.
#So I might add another condition where even SceondSlot == True, is needs to be == to 2.34s or lower. But that mean all 2nd weaves above 2.34s won't be accounted for?
#So maybe I turn the current SecondSlot == True as an elif statement to catch those cases, while the initial If statement checks for 2.34 + 2nd slot.

#This calculates both states of possible astrodyne weaves.
GCD_Count_2ndSlot = (15/gcdspeed_hasted) + 1
GCD_Count_2ndSlot = math.floor(GCD_Count_2ndSlot)
print("GCDs:",GCD_Count_2ndSlot)

GCD_Count_Early = (15/gcdspeed_hasted)
GCD_Count_Early = math.floor(GCD_Count_Early)
print("GCDs:",GCD_Count_Early)

#From here we should try figure out if we actually gain anything from 2nd weaving our astrodyne in the first place.
if GCD_Count_2ndSlot == GCD_Count_Early:
    print("Neutral no gain.")

elif GCD_Count_2ndSlot > GCD_Count_Early:
    leadbool = True
    lead = GCD_Count_2ndSlot - GCD_Count_Early

    print("2nd weave nets you:", lead, "GCD")

#Debug
#print(type(malefic_base), type(lead))

#dmg gained from having a lead malefic
leadTrueDamage = ((avgDamage/100) * float(malefic_base)) * float(lead)
leadBasePotency = float(malefic_base) * lead
leadModifiedPotency = modified_malefic * lead

#dmg gained from lead malefic on top of 5% astrodyne buff.
astrodyneleadTrueDmg = leadTrueDamage * 0.05
astrodyneleadBasePotency = leadBasePotency * 0.05
astrodyneleadModifiedPotency = leadModifiedPotency * 0.05

print("Base Potency lead =", leadBasePotency)
print("Modified Potency Lead =",leadModifiedPotency)
print("Average Malefic Damage Lead =", leadTrueDamage)
print("Lead gained with astrodyne dmg up [Base, Modified, TrueVal]:", astrodyneleadBasePotency, astrodyneleadModifiedPotency, astrodyneleadTrueDmg)


#Figuring out 5% dmg increase from astrodyne on a set of malefics (should change this so it includes the highest possible burst from AST, this is now accounting for double lord and earthly star)
print()
print("malefic contribution to astrodyne:",float(malefic_base) * 0.05)
BuffedGCDTotalTrueDamageE = (((avgDamage/100) * float(malefic_base)) * GCD_Count_Early) * 0.05
BuffedGCDTotalBasePotencyE = (float(malefic_base) * GCD_Count_Early) * 0.05
BuffedGcdTotalModifiedPotencyE = (modified_malefic * GCD_Count_Early) * 0.05

BuffedGCDTotalTrueDamageL = (((avgDamage/100) * float(malefic_base)) * GCD_Count_2ndSlot) * 0.05
BuffedGCDTotalBasePotencyL = (float(malefic_base) * GCD_Count_2ndSlot) * 0.05
BuffedGcdTotalModifiedPotencyL = (modified_malefic * GCD_Count_2ndSlot) * 0.05

print("Astrodyne dmg buff contribution Early Weave")
print("Base Potency increase =", BuffedGCDTotalBasePotencyE)
print("Modified Potency increase =",BuffedGcdTotalModifiedPotencyE)
print("Average Damage increase =", BuffedGCDTotalTrueDamageE)

print()
print("Late weave:")
print("Base Potency increase =", BuffedGCDTotalBasePotencyL)
print("Modified Potency increase =",BuffedGcdTotalModifiedPotencyL)
print("Average Damage increase =", BuffedGCDTotalTrueDamageL)



#This part is an extension of the one just before, but altered for calculating total gain including double lord + earthly star
TotalBuffedGCDTotalTrueDamageE = (((((avgDamage/100) * float(malefic_base)) * GCD_Count_Early)) + ((avgDamage/100) * (lordOfCrowns_base * 2)) + ((avgDamage/100) * earthlyStar_base * 0.9)) * 0.05
TotalBuffedGCDTotalBasePotencyE = ((float(malefic_base) * GCD_Count_Early) + (lordOfCrowns_base) + (earthlyStar_base)) * 0.05
TotalBuffedGcdTotalModifiedPotencyE = ((modified_malefic * GCD_Count_Early) + (modified_lordOfCrown * 2) + (modified_earthlyStar))* 0.05


TotalBuffedGCDTotalTrueDamageL = (((((avgDamage/100) * float(malefic_base)) * GCD_Count_2ndSlot)) + ((avgDamage/100) * (lordOfCrowns_base * 2)) + ((avgDamage/100) * earthlyStar_base * 0.9)) * 0.05
TotalBuffedGCDTotalBasePotencyL = ((float(malefic_base) * GCD_Count_2ndSlot) + (lordOfCrowns_base) + (earthlyStar_base)) * 0.05
TotalBuffedGcdTotalModifiedPotencyL = ((modified_malefic * GCD_Count_2ndSlot) + (modified_lordOfCrown * 2) + (modified_earthlyStar))* 0.05

print()
print("Total Astrodyne dmg buff contribution Early Weave")
print("Base Potency increase =", TotalBuffedGCDTotalBasePotencyE)
print("Modified Potency increase =",TotalBuffedGcdTotalModifiedPotencyE)
print("Average Damage increase =", TotalBuffedGCDTotalTrueDamageE)

print()
print("Late weave:")
print("Base Potency increase =", TotalBuffedGCDTotalBasePotencyL)
print("Modified Potency increase =",TotalBuffedGcdTotalModifiedPotencyL)
print("Average Damage increase =", TotalBuffedGCDTotalTrueDamageL)



"""
idk what this is
GCD_Count2 = (15/gcdspeed) + 0.5
print(GCD_Count2)
"""



#
#cutaway = gcdspeed - gcdspeed_hasted
#print(cutaway)