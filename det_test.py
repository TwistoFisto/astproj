import math

lvlModifier_Sub = 400
lvlModifier_Div = 1900


lvlModifier_Main = 390
det = int(input("What's your det stat: "))
tenac = int(input("tenacity: "))
spd = int(input("speed: "))
Tenacity = math.floor(100 * (tenac - lvlModifier_Sub) / lvlModifier_Div) / 1000
cVal = math.floor(140 * (det - lvlModifier_Main) / lvlModifier_Div) / 1000
Speed = math.floor(130 * (spd - lvlModifier_Sub) / lvlModifier_Div) / 1000

print(Speed)


print(Tenacity)