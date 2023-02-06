import math

lvlModifier_Sub = 400
lvlModifier_Div = 1900
dh = 1547

dh = int(input("What's your dhit stat: "))
crit = int(input("crit: "))

cVal = math.floor(550 * (dh - lvlModifier_Sub) / lvlModifier_Div) / 1000

CritD = math.floor(200 * (crit - lvlModifier_Sub) / lvlModifier_Div + 1400) / 1000
CritC = math.floor(200 * (crit - lvlModifier_Sub) / lvlModifier_Div + 50) / 1000

print(CritD, CritC)