from random import triangular
import pandas as pd
import math

lvlModifier_Sub = 400
lvlModifier_Div = 1900
lvlModifier_Main = 390

print("Please input your stats")
job = "BRD"#input("Class: ")
crit = 2000#int(input("Crit:"))
dhit = 1500#int(input("Direct Hit:"))
speed = 1473 #int(input("Skill Speed/Spellspeed:"))

movenamelist = pd.read_csv('justframecards-BasePotencies.csv')
movenamelist["Movename"] = movenamelist["Movename"].str.lower()

traitBuffList = pd.read_csv('justframecards-TraitsAndBuffs.csv')
traitBuffList['Buff'] = traitBuffList['Buff'].str.rstrip('%').astype('float') / 100.0
print(traitBuffList.to_string())

job_moves = movenamelist.query("Class == @job")
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

"""
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
            
    print("debug1",burstline)"""


#Getting baseline potency including buffs - also my python wasn't updated so we're nesting fucking if statements yippee:

if job == "SAM":
    SAMBuffList = traitBuffList.query("Class == @job")
    Jinpu = SAMBuffList.query("Name == 'Jinpu'").iloc[0,2]
    print("Jinpu", Jinpu)
    Shifu = SAMBuffList.query("Name == 'Shifu'").iloc[0,2]  
    pass

elif job == "NIN":
    NINBuffList = traitBuffList.query("Class == @job")
    Huton = NINBuffList.query("Name == 'Huton'").iloc[0,2]
    Trick_Attack = NINBuffList.query("Name == 'Trick Attack'").iloc[0,2]
    Mug = NINBuffList.query("Name == 'Mug'").iloc[0,2]
    pass

elif job == "DRG":
    DRGBuffList = traitBuffList.query("Class == @job")
    Battle_Litany = DRGBuffList.query("Name == 'Battle Litany'").iloc[0,2]
    Dragonsight_Self = DRGBuffList.query("Name == 'Dragonsight Self'").iloc[0,2]
    Disembowl = DRGBuffList.query("Name == 'Disembowl'").iloc[0,2]
    Lance_Charge = DRGBuffList.query("Name == 'Lance Charge'").iloc[0,2]
    pass

elif job == "MNK":
    MNKBuffList = traitBuffList.query("Class == @job")
    Disciplined_Fists = MNKBuffList.query("Name == 'Disciplined Fists'").iloc[0,2]
    Greased_Lightning = MNKBuffList.query("Name == 'Greased Lightning'").iloc[0,2]
    Riddle_of_Fire = MNKBuffList.query("Name == 'Riddle of Fire'").iloc[0,2]
    Riddle_of_Wind = MNKBuffList.query("Name == 'Riddle of Wind'").iloc[0,2]
    Brotherhood = MNKBuffList.query("Name == 'Brotherhood'").iloc[0,2]
    pass

elif job == "RPR":
    RPRBuffList = traitBuffList.query("Class == @job")
    Shadow_of_Death = RPRBuffList.query("Name == 'Shadow of death'").iloc[0,2]
    Arcane_Circle = RPRBuffList.query("Name == 'Arcane Circle'").iloc[0,2]
    pass

elif job == "BRD":
    BRDBuffList = traitBuffList.query("Class == @job | Class == 'ALL PHY RANGED'")
    #print(BRDBuffList.to_string())
    Increased_Action_DMG = BRDBuffList.query("Name == 'Increased Action DMG'").iloc[0,2]
    Raging_Strikes = BRDBuffList.query("Name == 'Raging Strikes'").iloc[0,2]
    Battle_Voice = BRDBuffList.query("Name == 'Battle Voice'").iloc[0,2]
    Mages_Ballad = BRDBuffList.query("Name == 'Mages Ballad'").iloc[0,2]
    Wanderers_Minuet = BRDBuffList.query("Name == 'Wanderers Minuet'").iloc[0,2]
    Armys_Paeon = BRDBuffList.query("Name == 'Armys Paeon'").iloc[0,2]
    Radiant_Finale = BRDBuffList.query("Name == 'Radiant Finale'").iloc[0,2]
    BRDBuffArray = [Increased_Action_DMG,Raging_Strikes,Battle_Voice,Mages_Ballad,Wanderers_Minuet,Armys_Paeon,Radiant_Finale]
    print(BRDBuffArray)
    pass

elif job == "MCH":
    MCHBuff = traitBuffList.query("Class == 'ALL PHY RANGED'")
    pass

elif job == "DNC":
    DNCBuffList = traitBuffList.query("Class == @job | Class == 'ALL PHY RANGED'")
    Increased_Action_DMG2 = DNCBuffList.query("Name == 'Increased Action DMG'").iloc[0,2]
    Dance_Partner = DNCBuffList.query("Name == 'Dance Partner'").iloc[0,2]
    Technical_Finish = DNCBuffList.query("Name == 'Technical Finish'").iloc[0,2]
    Devilment = DNCBuffList.query("Name == 'Devilment'").iloc[0,2]
    pass

elif job == "BLM":
    pass
elif job == "SMN":
    pass
elif job == "RDM":
    pass
elif job == "WAR":
    pass
elif job == "PLD":
    pass
elif job == "DRK":
    pass
elif job == "GNB":
    pass
elif job == "SGE":
    pass
elif job == "SCH":
    pass
elif job == "AST":
    pass

"""
match job:
    case "SAM":
        buffs = job_moves = traitBuffList.query("Class == @job")
    case "NIN":
    case "DRG":
    case "MNK":
    case "RPR":
    case "BRD":                
    case "MCH":
    case "DNC":
    case "BLM":
    case "SMN":
    case "RDM":
    case "WAR":
    case "PLD":
    case "DRK":
    case "GNB":     
"""
"""    

SAM1 = SAM.query("Movename == 'midare setsugekka'")
print(SAM1.to_string())

input = input("Give me a movename: ")

#SAM2 = SAM.query("Movename == input")
SAM2 = SAM.loc[SAM["Movename"] == input]
SAM2_POTENCY_VAL = SAM2.iloc[0,3]
print(SAM2_POTENCY_VAL)
"""


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