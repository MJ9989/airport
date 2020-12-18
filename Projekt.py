# -*- coding: utf-8 -*-
"""
Spyder Editor

Dies ist eine temporäre Skriptdatei.
"""

# A2
import time

flugzeugtypen = ["A380","A370","B707"]
luftfahrtgesellschaften = ["Emirates", "Lufthansa", "Turkish Airlines"]
flüge = {}
flugnummerzahl = 100


class Flugzeug(object):

    def __init__(self, flugzeugtyp, luftfahrtgesellschaft,
                 flugnummer, startzeitpunkt=None, landebahn=None,
                 parkposition=None, startbahn=None, status="fliegend"):
        self.startzeitpunkt = startzeitpunkt
        self.landebahn = landebahn
        self.parkposition = parkposition
        self.startbahn = startbahn
        self.flugzeugtyp = flugzeugtyp
        self.luftfahrtgesellschaft = luftfahrtgesellschaft
        self.flugnummer = flugnummer
        self.status = status
    
    

def neuesFlugzeugErfassen(flugzeugtyp, luftfahrtgesellschaft):
    global flugnummerzahl
    global flugzeugtypen
    global luftfahrtgesellschaften
    global flüge
    flugnummer = luftfahrtgesellschaft[0] + luftfahrtgesellschaft[1].upper() + str(flugnummerzahl)
    flugnummerzahl +=1
    if flugzeugtyp not in flugzeugtypen:
        flugzeugtypen.append(flugzeugtyp)
    if luftfahrtgesellschaft not in luftfahrtgesellschaften:
        luftfahrtgesellschaften.append(luftfahrtgesellschaft)
    flüge[flugnummer] = Flugzeug(flugzeugtyp, luftfahrtgesellschaft, flugnummer)


neuesFlugzeugErfassen("A390", "Arab Air")
print(flüge['AR100'].flugnummer)


class Landebahn(object):

    def __init__(self, startzeitpunkt=None, landebahn=None, 
                 parkposition=None, startbahn=None, flugzeugtyp=None, luftfahrtgesellschaft=None): 
        self.startzeitpunkt = startzeitpunkt 
        self.landebahn = landebahn 
        self.parkposition = parkposition 
        self.startbahn = startbahn
        self.flugzeugtyp = flugzeugtyp
        self.luftfahrtgesellschaft = luftfahrtgesellschaft






