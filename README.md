# AstCardProj

Work in progress project.

The purpose of this project is to showcase how much damage you can potentially gain from perfect card play decision. This is different from the AstCardCal as we want to account for 2 minute sequencing, Astrodyne vs perfect card role draws and Potential redraws. It'll will however take aspects of AstCardCal, XIVanalysis and Opener Burst Cal, but  having an expanded library of burst lines for every class and means to showcase what decision will cost you potency, etc...
AST is a class of marginals - low gains, low losses. Mistakes don't seem that impressive until you start totalling your losses. Gains don't seem significant until you start to consistently tech your cards for every single play.

**Todo:**
1. Expand scope to include all relevent class (No WHM, BLU, etc...).
2. Autoattacks
3. Be able to calculate a burst line's low point, high roll and average potencies and true dmg values (WIP)

From this point we'll need to use FFLOGs data to feed it information for it to process the following functions:
1. 2 Minute sequencing - we want to figure how the best sequence to card people and the chance of drawing that specific sequence; as well as showcasing other similar sequence incase of RNG.
2. Astrodyne vs perfect card role draw - a case if 6% on optimal card target vs 6% secondary target + 5% self under Div
3. Potential Redraws - it should be able to figure out if a redraw would have been the play or not, regardless of the outcome, it should forecast what you stand to gain or lose.

