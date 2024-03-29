from random import triangular
import pandas as pd
import math

#another prototype, this is proving that we can take an "array" of dmg GCDs/oGCDs and convert them to various potencies, from base, to trait modified to 
#including various self buffs and then have that be distingushed on a per GCD/oGCD basis. (This part hasn't been implemented yet)

#One of the main edge cases which is annoying me are GCDs and oGCDs that is outside of a specific buff while being under card buff, a good example would be an early NIN card where you catch a GCD before Trick 
#has even been applied, or better yet, early card NIN where you catch Phantom Kama under Mug's buff but not Trick Attack. This prototype will have to iterate for GCD, oGCD, autoattacks and pet actions if it's 
#under their own stat steroid. Under a commandline interface, this is extremely slow as you'll have to ask the user to input a true or false statement for every single iteration of dmg in a burst profile.
#I'll need something that will create a buff timeline, and a rotation timeline, and then check if a dmg instance is outside of said buff or not, then lastly calculate final potency + true dmg values.
    #tl;dr I need something thatwill automatically update values synonomously as the user place stuff within and outside of their buff.
lvlModifier_Sub = 400
lvlModifier_Div = 1900
lvlModifier_Main = 390

print("Please input your stats")
job = "SAM"#input("Class: ")
crit = 2000#int(input("Crit:"))
dhit = 1500#int(input("Direct Hit:"))
speed = 508 #int(input("Skill Speed/Spellspeed:"))
#1473
movenamelist = pd.read_csv('justframecards-BasePotencies.csv')
movenamelist["Movename"] = movenamelist["Movename"].str.lower()

traitBuffList = pd.read_csv('justframecards-TraitsAndBuffs.csv')
traitBuffList['Buff'] = traitBuffList['Buff'].str.rstrip('%').astype('float') / 100.0
print(traitBuffList.to_string())

job_moves = movenamelist.query("Class == @job")
a = len(job_moves.index)
print(a)
print(job_moves.to_string())

jobmodpd = pd.read_csv('JobModifiers.csv')
jobget = jobmodpd.query("Class == @job")
jobmod = jobget.iloc[0,1]
print(jobmod)
jobmod = float(jobmod)

jobtype = jobget.iloc[0,2]

#using jobtype to determine what trait modifiers to use, healers are classified as casters
#and then use trait modifiers to calculate both modified potencies + true damage values.
if jobtype == "CASTER":
    trait_modifier = 1.3
elif jobtype == "PHYR":
    trait_modifier = 1.2
elif jobtype == "TANK":
    trait_modifier = 0.8
else:
    trait_modifier = 1.0

#Getting baseline potency including buffs - also my python wasn't updated so we're nesting fucking if statements yandere dev moment KEKW
#it'll need to draw out buff type and also duration so we'll know what to attach to the modified GCD or not.
if job == "SAM":
    SAMBuffList = traitBuffList.query("Class == @job")
    #not the best solution, find another.
    Jinpu = [SAMBuffList.query("Name == 'Jinpu'").iloc[0,2],SAMBuffList.query("Name == 'Jinpu'").iloc[0,3]]
    print("Jinpu", Jinpu)
    Shifu = [SAMBuffList.query("Name == 'Shifu'").iloc[0,2],SAMBuffList.query("Name == 'Shifu'").iloc[0,3]]
    buffs = [Jinpu, Shifu]
    print(buffs)
    pass

elif job == "NIN":
    NINBuffList = traitBuffList.query("Class == @job")
    Huton = NINBuffList.query("Name == 'Huton'").iloc[0,2]
    Trick_Attack = NINBuffList.query("Name == 'Trick Attack'").iloc[0,2]
    Mug = NINBuffList.query("Name == 'Mug'").iloc[0,2]
    buffs = [Huton, Trick_Attack, Mug]
    pass

elif job == "DRG":
    DRGBuffList = traitBuffList.query("Class == @job")
    Battle_Litany = DRGBuffList.query("Name == 'Battle Litany'").iloc[0,2]
    Dragonsight_Self = DRGBuffList.query("Name == 'Dragonsight Self'").iloc[0,2]
    Disembowl = DRGBuffList.query("Name == 'Disembowl'").iloc[0,2]
    Lance_Charge = DRGBuffList.query("Name == 'Lance Charge'").iloc[0,2]
    buffs = [Battle_Litany, Dragonsight_Self, Disembowl,Lance_Charge]
    pass

elif job == "MNK":
    MNKBuffList = traitBuffList.query("Class == @job")
    Disciplined_Fists = MNKBuffList.query("Name == 'Disciplined Fists'").iloc[0,2]
    Greased_Lightning = MNKBuffList.query("Name == 'Greased Lightning'").iloc[0,2]
    Riddle_of_Fire = MNKBuffList.query("Name == 'Riddle of Fire'").iloc[0,2]
    Riddle_of_Wind = MNKBuffList.query("Name == 'Riddle of Wind'").iloc[0,2]
    Brotherhood = MNKBuffList.query("Name == 'Brotherhood'").iloc[0,2]
    buffs = [Disciplined_Fists, Greased_Lightning, Riddle_of_Fire,Riddle_of_Wind, Brotherhood]
    pass

elif job == "RPR":
    RPRBuffList = traitBuffList.query("Class == @job")
    Shadow_of_Death = RPRBuffList.query("Name == 'Shadow of death'").iloc[0,2]
    Arcane_Circle = RPRBuffList.query("Name == 'Arcane Circle'").iloc[0,2]
    buffs = [Shadow_of_Death,Arcane_Circle]
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
    buffs = [Raging_Strikes,Battle_Voice,Mages_Ballad,Wanderers_Minuet,Armys_Paeon,Radiant_Finale]
    pass

#not needed?
elif job == "MCH":
    MCHBuff = traitBuffList.query("Class == 'ALL PHY RANGED'").iloc[0,2]
    pass

elif job == "DNC":
    DNCBuffList = traitBuffList.query("Class == @job | Class == 'ALL PHY RANGED'")
    Increased_Action_DMG2 = DNCBuffList.query("Name == 'Increased Action DMG'").iloc[0,2]
    Dance_Partner = DNCBuffList.query("Name == 'Dance Partner'").iloc[0,2]
    Technical_Finish = DNCBuffList.query("Name == 'Technical Finish'").iloc[0,2]
    Devilment = DNCBuffList.query("Name == 'Devilment'").iloc[0,2]
    buffs = [Dance_Partner,Technical_Finish,Devilment]    
    pass

elif job == "BLM":
    BLMBuffList = traitBuffList.query("Class == @job | Class == 'ALL CASTERS + HEALERS'")
    Casterbuff = BLMBuffList.query("Name == Maim and Mend").iloc[0,2]
    Enochian = BLMBuffList.query("Name == 'Enochian'").iloc[0,2]
    Fire_Aspect = BLMBuffList.query("Name == 'Aspect of Fire 3'").iloc[0,2]
    Leylines = BLMBuffList.query("Name == 'Leylines'").iloc[0,2]
    buffs = [Enochian,Fire_Aspect,Leylines]
    pass

elif job == "SMN":
    SMNBuffList = traitBuffList.query("Class == @job | Class = 'ALL CASTERS + HEALERS'")
    Casterbuff = SMNBuffList.query("Name == 'Maim and Mend'").iloc[0,2]
    Searing_Light = SMNBuffList.query("Name == 'Searing Light'").iloc[0,2]
    pass

elif job == "RDM":
    RDMBuffList = traitBuffList.query("Class == @job | Class = 'ALL CASTERS + HEALERS'")
    Embolden = RDMBuffList.query("Name == 'Embolden'").iloc[0,2]
    Manafication = RDMBuffList.query("Name == 'Manafication'").iloc[0,2]
    pass

elif job == "WAR":
    WARBuffList = traitBuffList.query("Class = @job | Class = 'ALL TANKS'")
    Tank_Mastery = WARBuffList.query("Name == 'Tank Mastery'").iloc[0,2]
    Storms_Eye = WARBuffList.query("Name == 'Storms Eye'").iloc[0,2]
    pass

elif job == "PLD":
    PLDBuffList = traitBuffList.query("Class == @job | Class = 'ALL TANKS'")
    Tank_Mastery = PLDBuffList.query("Name == 'Tank Mastery'").iloc[0,2]
    Fight_or_Flight = PLDBuffList.query("Name == 'Fight or Flight'")
    pass

elif job == "DRK":
    DRKBuffList = traitBuffList.query("Class == @job | Class = 'ALL TANKS'")
    Tank_Mastery = DRKBuffList.query("Name == 'Tank Mastery'").iloc[0,2]
    Darkside = DRKBuffList.query("Name == 'Darkside'").iloc[0,2]
    pass

elif job == "GNB":
    GNBBuffList = traitBuffList.query("Class == @job | Class = 'ALL TANKS'")
    Tank_Mastery = GNBBuffList.query("Name == 'Tank Mastery'").iloc[0,2]
    No_Mercy = GNBBuffList.query("Name == 'No Mercy'").iloc[0,2]
    pass

elif job == "SGE":
    SGEBuff = traitBuffList.query("Class == 'Tank Mastery'").iloc[0,2]
    pass

elif job == "SCH":
    SCHBuffList = traitBuffList.query("Class == @job | Class == 'ALL CASTERS + HEALERS'")
    Casterbuff = SCHBuffList.query("Name == 'Maim and Mend'").iloc[0,2]
    Chain_Stratagem = SCHBuffList.query("Name == 'Chain Stratagem'").iloc[0,2]
    pass

elif job == "AST":
    ASTBuffList = traitBuffList.query("Class == @job | Class == 'ALL CASTERS + HEALERS'")
    Casterbuff = ASTBuffList.query("Name == 'Maim and Mend'").iloc[0,2]
    Divination = ASTBuffList.query("Name == 'Divination'").iloc[0,2]
    Astrodyne_Mind = ASTBuffList.query("Name == 'Astrodyne: Mind'").iloc[0,2]
    Astrodyne_Body = ASTBuffList.query("Name == 'Astrodyne: Body'").iloc[0,2]
    pass


#It'll need a checker for it the class in question has any haste modifiers like MNK greese lightning, SAM's shifu, etc...
#it'll then need to do a separate calculation to account for that
speed = math.floor(130 * (speed - lvlModifier_Sub) / lvlModifier_Div) / 1000
GCD = 2.5-(2.5*speed)
#GCD = (2500-2500*speed)/1000
print("GCD recast:", GCD)

#for i in 
#    ability_from_dataframe = job_moves.loc[job_moves["Movename"] == ability_name]
Modified_GCD_speed = GCD-(GCD - (GCD*0.87))
print("Modified GCD Speed:",Modified_GCD_speed)

player = [job, crit, dhit, speed, GCD]

GCD_Count = 15/GCD
print("GCD Count:",GCD_Count)

print("Create a burst line: ")
burstline = []
burstline_base_potency = []
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
        burstline_base_potency.append(float(get_ability_potency))

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
            burstline_base_potency.append(float(get_ability_potency2))
            pass
        else:
            burstline.append(ability_name2)
            burstline_base_potency.append(float(get_ability_potency2))

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
                burstline_base_potency.append(float(get_ability_potency3))
                pass
            else:
                burstline.append(ability_name3)
                burstline_base_potency.append(float(get_ability_potency3))
                pass
            
    print("debug1",burstline)
    print("debug", burstline_base_potency)





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
#using burstline as a basis to get values from the class' moveset.
#modified potencies will act as a new container for the moveset's potencies.
#truedmg list does the same thing as modified potencies, but instead of potencies it computes true baseline dmg values.
total_base_potency = sum(burstline_base_potency)
print(total_base_potency)

trait_modified_potencies = total_base_potency * trait_modifier
print(trait_modified_potencies)

trait_modified_potenciesArray = []
for i in burstline_base_potency:
    trait_modified_potenciesArray.append(i * trait_modifier)

print(trait_modified_potenciesArray)

buff_modified_potencies = []
true_dmg = []
#This for loop is gonna iterate per dmg instance. It'll need information whether or not the GCD or ability was buffed. For example We can take NIN
#as an example - it need to check if the GCD or ability was used under Trick + Mug, or just trick, etc... and adversely Trick Attack itself is always base value so it'll need to account for that.
for i in trait_modified_potenciesArray:
    print("Trait:", )
    pass

#actually 2nd idea, I can just ask at what GCD does their buff start in the burst profile.
slot = int(input("at what GCD does your buff goes out"))
slot = slot - 1

for i in trait_modified_potenciesArray:
    
    if i == slot:

        pass
    pass

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