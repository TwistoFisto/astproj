import pandas as pd
import math as math
data = pd.read_csv(r'C:\Users\patel\Downloads\just_frame_cards_-_BasePotencies.csv')
data["Crit"] = data["Crit"].fillna(0).astype(int)
data["DHit"] = data["DHit"].fillna(0).astype(int)
data["Pet"] = data["Pet"].fillna(0).astype(int)
data["Recast"] = data["Recast"].fillna(0)
SAM = data.query("Class == 'SAM'")


lvlModifier_Sub = 400
lvlModifier_Div = 1900
lvlModifier_Main = 390
dh = 1523#int(input("What is your Direct Hit Stat"))
det = 1433#int(input("What is your Determination Stat"))
crit = 2257#int(input("What is your Critical Hit Stat"))
ten = 123#int(input("What is your Tenacity Stat"))
gcd = 2500
spd = 616#int(input("What is your Skill Speed or Spell Speed"))
strength = 2936#int(input("What is your Strength or Intelligence"))
Job = 'SAM'#input("What is your Class")
weaponBaseDamage = 126
lvlAttackModifier = 195
AttackPower = 112

atk = math.floor(lvlAttackModifier * (strength - lvlModifier_Main) / lvlModifier_Main + 100) / 100.0


Dh = math.floor(550 * (dh - lvlModifier_Sub) / lvlModifier_Div) / 1000
Det = math.floor(140 * (det - lvlModifier_Main) / lvlModifier_Div) / 1000
CritD = math.floor(200 * (crit - lvlModifier_Sub) / lvlModifier_Div + 1400) / 1000
CritC = math.floor(200 * (crit - lvlModifier_Sub) / lvlModifier_Div + 50) / 1000
Tenacity = math.floor(100 * (ten - lvlModifier_Sub) / lvlModifier_Div) / 1000
Speed = math.floor(130 * (spd - lvlModifier_Sub) / lvlModifier_Div) / 1000
WeaponDamage = math.floor(lvlModifier_Main * AttackPower / 1000.0 + weaponBaseDamage) / 100.0
baseDamage = math.floor(math.floor(math.floor(100 * atk * WeaponDamage) * (1 + Det)))
avgDamage = math.floor(baseDamage * (1 + (CritD - 1) * CritC) * (1 + Dh * 0.25))
critDamage = math.floor(baseDamage * CritD)

print(baseDamage, avgDamage, critDamage)



