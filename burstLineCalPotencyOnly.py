import pandas as pd
import math

lvlModifier_Sub = 400
lvlModifier_Div = 1900
lvlModifier_Main = 390

print("Please input your stats")
job = "SAM"#input("Class: ")
crit = 2000#int(input("Crit:"))
dhit = 1500#int(input("Direct Hit:"))
speed = 1473 #int(input("Skill Speed/Spellspeed:"))

dataframe = pd.read_csv('justframecards-BasePotencies.csv')
dataframe["Movename"] = dataframe["Movename"].str.lower()

job_moves = dataframe.query("Class == @job")
a = len(job_moves.index)
print(a)
print(job_moves.to_string())

speed = math.floor(130 * (speed - lvlModifier_Sub) / lvlModifier_Div) / 1000
GCD = 2.5-(2.5*speed)
#GCD = (2500-2500*speed)/1000
print(GCD)
player = [job, crit, dhit, speed, GCD]

GCD_Count = 15/GCD
print(GCD_Count)

print("Create a burst line: ")
burstline = []
GCD_Count  = math.floor(GCD_Count)
oGCD_weave_count = 0

#WE'RE GOING TO NEED TO ADD CAST TIMES COLUMN SO WE KNOW IF IT'S: NO WEAVE, SINGLE WEAVE ONLY OR FREE DOUBLE WEAVE
for i in range(GCD_Count):
    print("debug mesg")
    ability_name = input("GCD/oGCD: ")
    ability_name = ability_name.lower()
    
    #Now we search for the move in the class specific segment:
    #ability_from_dataframe = job_moves.query("Movename == @ability_name").loc
    ability_from_dataframe = job_moves.loc[job_moves["Movename"] == ability_name]
    print(ability_from_dataframe)

    #This is supposed to get the potency/type of the move based off the ability name within the class specific segment.
    get_ability_potency = ability_from_dataframe.iloc[0,3]
    get_ability_type = ability_from_dataframe.iloc[0,2]
    print("debug2",get_ability_potency, get_ability_type)
    if get_ability_type == "GCD":
        burstline.append(ability_name)
        pass
    else:
        burstline.append(ability_name)

        ability_name2 = input("GCD/oGCD: ")
        ability_name2 = ability_name2.lower()
        ability_from_dataframe2 = job_moves.loc[job_moves["Movename"] == ability_name2]
        print(ability_from_dataframe2)
        get_ability_potency2 = ability_from_dataframe2.iloc[0,3]
        get_ability_type2 = ability_from_dataframe2.iloc[0,2]
        print("debug2",get_ability_potency2, get_ability_type2)

        if get_ability_type2 == "GCD":
            ++i
            burstline.append(ability_name2)
            pass
        else:
            burstline.append(ability_name2)

            ability_name3 = input("GCD/oGCD: ")
            ability_name3 = ability_name3.lower()
            ability_from_dataframe3 = job_moves.loc[job_moves["Movename"] == ability_name3]
            print(ability_from_dataframe3)
            get_ability_potency3 = ability_from_dataframe3.iloc[0,3]
            get_ability_type3 = ability_from_dataframe3.iloc[0,2]
            print("debug2",get_ability_potency3, get_ability_type3)

            if get_ability_type3 == "GCD":
                ++i
                burstline.append(ability_name3)
                pass
            else:
                burstline.append(ability_name3)
                pass
            
    print("debug1",burstline)


SAM1 = SAM.query("Movename == 'midare setsugekka'")
print(SAM1.to_string())

input = input("Give me a movename: ")

#SAM2 = SAM.query("Movename == input")
SAM2 = SAM.loc[SAM["Movename"] == input]
SAM2_POTENCY_VAL = SAM2.iloc[0,3]
print(SAM2_POTENCY_VAL)


"""
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

"""