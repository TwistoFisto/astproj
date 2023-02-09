import pandas as pd
import math
"""
crit = int(input("What's your crit stat: "))
dhit = int(input("What's your dhit stat: "))
det = int(input("What's your det stat: "))
tena = int(input("What's your tenacity: "))
speed = int(input("What's your Skillspeed stat: "))"""
jinpu = 1.13

lvlModifier_Sub = 400
lvlModifier_Div = 1900
lvlModifier_Main = 390

crit = 2446
dhit = 1459
det = 1571
tena = 495
speed = 520

dhit = math.floor(550 * (dhit - lvlModifier_Sub) / lvlModifier_Div) / 1000
critD = math.floor(200 * (crit - lvlModifier_Sub) / lvlModifier_Div + 1400) / 1000
critC = math.floor(200 * (crit - lvlModifier_Sub) / lvlModifier_Div + 50) / 1000
det = math.floor(140 * (det - lvlModifier_Main) / lvlModifier_Div) / 1000
det = det+1
print(critD)
print(det)
#Tank only
tena = math.floor(100 * (tena - lvlModifier_Sub) / lvlModifier_Div) / 1000

#stats = [critC,critD, dhit, det, tena, speed]

"""
DEPRECATED
dataframe2 = pd.read_csv('stats.csv')
print(dataframe2.to_string())
"""

#charDataframe = pd.DataFrame([stats], columns=["CRIT","DHIT","DET","SKS"])
#print(charDataframe)
#print(charDataframe.to_string())

dataframe = pd.read_csv('justframecards-BasePotencies.csv')
#df = pd.
dataframe["Movename"] = dataframe["Movename"].str.lower()
#f(WD) = ⌊ ( LevelModLv, MAIN · JobModJob, Attribute / 1000 ) + WD ⌋
#f(AUTO) = ⌊ ( ⌊ LevelModLv, Main · JobModJob, Attribute / 1000 ) + WD ⌋ · ( Weapon Delay / 3 ) ⌋




SAM = dataframe.query("Class == 'SAM'")
a = len(SAM.index)
print(a)
print(SAM.to_string())

modified_potencies = pd.DataFrame([], columns=["modified_potency"])
modified_potency = 0
float(modified_potency)

i = 0
for i in range(a):
    base_potency = SAM.loc[i][3]
    print(base_potency)
    if SAM.loc[i][5] == True:
        #print("YES")
        modified_potency = float(base_potency) * jinpu * det * critD
        #print(modified_potency)
        #print("YES2")
        if SAM.loc[i][6] == True:
            modified_potency = modified_potency * 1.25

        modified_potencies = modified_potencies.append(pd.Series(modified_potency, index=modified_potencies.columns, name=SAM.loc[i][1]))
    else:
        if SAM.loc[i][6] == True:
            #print("yess")
            modified_potency = float(base_potency) * jinpu * det * 1.25
            modified_potencies = modified_potencies.append(pd.Series(modified_potency, index=modified_potencies.columns, name=SAM.loc[i][1]))
        else:
            modified_potency = float(base_potency) * jinpu * det
            modified_potencies = modified_potencies.append(pd.Series(modified_potency, index=modified_potencies.columns, name=SAM.loc[i][1]))

    #modified_potencies = pd.concat(modified_potency)
    #SAM.concat(modified_potency, axis = 1)

print(modified_potencies.to_string())

#SAM.concat(modified_potencies)

# Using 'Address' as the column name
# and equating it to the list
#df['Address'] = address



SAM1 = SAM.query("Movename == 'midare setsugekka'")
print(SAM1.to_string())

input = input("Give me a movename: ")

#SAM2 = SAM.query("Movename == input")
SAM2 = SAM.loc[SAM["Movename"] == input]
SAM2_POTENCY_VAL = SAM2.iloc[0,3]
print(SAM2_POTENCY_VAL)


print(SAM2.to_string())