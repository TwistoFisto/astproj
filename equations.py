import math
from operator import contains
import pandas as pd


#This file is a basis for all our future calculations, it'll all be in it's own function so other pys can call upon when needed.

#global variables - same across the board
lvlModifier_Sub = 400   
lvlModifier_Div = 1900
lvlModifier_Main = 390
weaponBaseDamage = 126
lvlAttackModifier = 195

#apparently tanks have -50 on the lvlattackmodifier
def dh(dhit):
    Dh = math.floor(550 * (dhit - lvlModifier_Sub) / lvlModifier_Div) / 1000
    return Dh

def det(det):
    Det = math.floor(140 * (det - lvlModifier_Main) / lvlModifier_Div) / 1000
    return Det

def atk(lvlAttackModifier, mainstat, lvlModifier_Main):
    Atk = math.floor(lvlAttackModifier * (mainstat - lvlModifier_Main) / lvlModifier_Main + 100) / 100.0
    return Atk

def tenc(tenc):
    Ten = 100 * ((tenc - lvlModifier_Sub) / lvlModifier_Div) / 1000
    return Ten


#This function calculates the averageDMG of a player per 100 potency
def averageDMG(mainstatS, critS, detS, dhitS, speedS, tenacityS, job):
    print("debug, averageDMG function")

    #Getting job modifier stats
    jobmodpd = pd.read_csv('JobModifiers.csv')
    job = jobmodpd.query("Class == @job")
    jobmod = job.iloc[0,1]
    print(jobmod)
    jobmod = float(jobmod)

    jobtype = job.iloc[0,2]

    if jobtype == "CASTER":
        trait_modifier = 1.3
    elif jobtype == "PHYR":
        trait_modifier = 1.2
    elif jobtype == "TANK":
        trait_modifier = 0.8
    else:
        trait_modifier = 1.0
    
    atk = math.floor(lvlAttackModifier * (mainstatS - lvlModifier_Main) / lvlModifier_Main + 100) / 100.0
    Dh = math.floor(550 * (dhitS - lvlModifier_Sub) / lvlModifier_Div) / 1000
    Det = math.floor(140 * (detS - lvlModifier_Main) / lvlModifier_Div) / 1000
    CritD = math.floor(200 * (critS - lvlModifier_Sub) / lvlModifier_Div + 1400) / 1000
    CritC = math.floor(200 * (critS - lvlModifier_Sub) / lvlModifier_Div + 50) / 1000
    WeaponDamage = math.floor(lvlModifier_Main * jobmod / 1000.0 + weaponBaseDamage) / 100.0
    baseDamage = math.floor(math.floor(math.floor(100 * atk * WeaponDamage) * (1 + Det))) * trait_modifier
    #I'm not sure where the trait modifier goes, according to character panel refined the trait modifier goes at the base dmg. However I think this is wrong maybe?

    #approximate dmg for every 100 potency.
    avgDamage = math.floor(baseDamage * (1 + (CritD - 1) * CritC) * (1 + Dh * 0.25))
    return avgDamage

#Delay / 3.00 * 90 = AA potency of all melees + dnc
#Delay / 3.00 * 80 = AA potency of brd + mch
#f(AUTO) = ⌊ ( ⌊ Level Lv, MAIN × Job Job, Attribute / 1000 ) + WD ⌋ × ( Weapon Delay / 3 ) ⌋
#this function is suppose to figure out how much dmg your autos deal generally speaking
def autoattacks(job,mainstat):
    print("debug - autoattacks funct")
    jobmodpd = pd.read_csv('JobModifiers.csv')
    job = jobmodpd.query("Class == @job")
    jobWeapDelay = job.iloc[0,3]
    jobmod = job.iloc[0,1]
    print(jobmod)
    jobmod = float(jobmod)
    print(jobWeapDelay)
    jobWeapDelay = float(jobWeapDelay)
    jobtype = job.iloc[0,2]

    #and then divide that shit by 100 idk what the fuck i'm doing here.
    autoattacks = ((lvlModifier_Main * jobmod/1000) + weaponBaseDamage) * (jobWeapDelay/3)
    atkA = atk(lvlAttackModifier, mainstat, lvlModifier_Main)
   # d1 = 90 * atkA

    if jobtype == "TANK" or jobtype == "MELEE" or job == "DNC":
        AABasepotency = (jobWeapDelay/3) * 90
        #print(math.ceil(AABasepotency))
        AABasepotency = round(AABasepotency,1)
        print(AABasepotency)
        return AABasepotency
    
    elif jobtype == "PHYR":
        AABasepotency = (jobWeapDelay/3) * 80
        AABasepotency = round(AABasepotency,1)
        print(AABasepotency)
        return AABasepotency
    else:
        return

#test funct
result = averageDMG(2936, 2257, 1752,1012,803,123,"AST")
print(result)
#autoattacks("WAR")
"""strength = 2936
dh = 1012
det = 1752
crit = 2257
ten = 123
gcd = 2500
spd = 803
""" 
"""
    if job == "BLM" or job == "RDM" or job == "SMN" or job == "WHM" or job == "SCH" or job == "AST" or job == "SGE":
        trait_modifier = 1.3
    elif job == "BRD" or job == "DNC" or job == "MCH":
        trait_modifier = 1.2
    elif job == "WAR" or job == "PLD" or job == "DRK" or job == "GNB":
        trait_modifier = 0.8
    else:
        trait_modifier = 1
"""   