import os
import sys

ijssalon = 1
bak = 1
hoorn = 1.25
def smaken():
    global smaak
    for k in range(bol ,0,-1):
        smaak = str(input("Welke smaak wilt u voor " + str(k) + " ? A) Aardbei, C) Chocolade, V) Vanille of M) Munt? : ")).lower()
        if smaak =="a":
            smaak = "Aardbei"
        elif smaak =="c":
            smaak = "Chocolade"
        elif smaak =="v":
            smaak = "Vanille"
        elif smaak == "m":
            smaak ="munt"
        else:
            print("Sorry dat snap ik niet")
        

def bestel():
    global bestel
    bestellen = input("Hier is uw "+ deel+ " met " + str(bol)+ " bolletje(s). Wilt u nog meer bestellen? (Y/N) : ").lower()
    if bestellen == "y":
        return begin()
    elif bestellen == "n":
        bonnetje()
        print("Bedankt en tot ziens.")
        sys.exit()     
    else:
        print("Sorry, dat snap ik niet...")
        ijssalon+0

def bonnetje():
    global bon
    #prijsBak = (bakjeAantal * 0.75)
    #prijsHoorn = (hoorntjeAantal * 1.25)
    print("")
    print("-------------[Papi Gelato]-------------")
    print("")
    #print("Bolletjes   ",bol," x €1,10 = €",prijsBol)
    total = "{:.2f}".format(round(float(bol)*1.1 , 2))
    totalBakje = "{:.2f}".format(round(float(bakjeAantal)*0.75 , 2))
    totalHoorntje = "{:.2f}".format(round(float(hoorntjeAantal)*1.25 , 2))
    totaalBon = total + totalBakje + totalHoorntje
    print("Bolletjes:       ", bol ,           "x € 1.10 =  €",total)
    print("Horrentje:       ", hoorntjeAantal ,"x € 1.25 =  €",totalHoorntje)
    print("Bakje:           ", bakjeAantal,    "x € 0.75 =  €",totalBakje)
    print("                                ------ +")
    print("Totaal:                         €",totaalBon)

def begin():
    global bol, deel, hoorntjeAantal, bakjeAantal
    hoorntjeAantal = 0
    bakjeAantal = 0
    while ijssalon == 1:
        bol = int(input("Hoeveel bolletjes ijs wilt u? : "))
        while bol >8:
            print("Sorry, zulke grote bakken hebben we niet")
            bol = int(input("Hoeveel bolletjes ijs wilt u? : "))
        if bol >=1 and bol <=3:
            while bak == 1:
                hoorntje = str(input("Wilt u deze " + str(bol) + " bolletje(s) in A) een hoorntje of B) een bakje? : ")).lower()
                if hoorntje == "a":
                    hoorntjeAantal += 1
                    deel = "hoorntje"
                    smaken()
                    bestel()
                elif hoorntje == "b":
                    bakjeAantal+= 1
                    deel = "bakje"
                    smaken()
                    bestel()
                else:
                    print("Sorry, dat snap ik niet")
        elif bol >=4 and bol <=8:
            deel = "bakje"
            smaken()
            bestel()
        else:
            print("Sorry, ik snap het niet...")
print("Welkom bij Papi Gelato. ")
begin()