import os
import sys

ijssalon = 1
bak = 1
hoorn = 1.25
sorry = "Sorry, dat is geen optie die we aanbieden..."
def smaken():
    global smaak
    for k in range(bol ,0,-1):
        smaak = str(input("Welke smaak wilt u voor bol nummer" + str(k) + " ? A) Aardbei, C) Chocolade, V) Vanille of M) Munt? : ")).lower()
        if smaak =="a":
            smaak = "Aardbei"
        elif smaak =="c":
            smaak = "Chocolade"
        elif smaak =="v":
            smaak = "Vanille"
        elif smaak == "m":
            smaak ="Munt"
        else:
            print (sorry) 

def toppings():
    global topping, toppingsaantal, toppingprijs
    toppingsaantal = 0
    topping = input("Welke topping wilt u? U kunt kiezen uit A) Niks, B) Slagroom, C) Sprinkels of D) Caramel Saus : ").lower()
    if topping == "a":
        topping = "Geen"
        toppingsaantal += 1
        toppingprijs = 0
    elif topping == "b":
        topping = "Slagroom"
        toppingsaantal += 1
        toppingprijs = 0.50
    elif topping == "c":
        topping = "Sprinkels"
        toppingsaantal += 1
        toppingprijs = 0.30*bol
    elif topping == "d" and hoorntje =="a":
        topping = "CaramelSaus"
        toppingsaantal += 1
        toppingprijs = 0.60
    elif topping == "d" and hoorntje =="b":
        topping = "CaramelSaus"
        toppingsaantal += 1
        toppingprijs = 0.90
    else:
        print (sorry) 
        toppings()  

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
        print (sorry)
        ijssalon+0

def zakelijk():
    global literIjs, smaakLiter
    werk = input("Bent u 1) Particulier of 2) Zakelijk? : ")
    if werk == "1":
        begin()
    elif werk == "2":
        literIjs = int(input("Hoeveel liter ijs wilt u? : "))
        for p in range(literIjs,0,-1):
            smaakLiter = str(input("Welke smaak wilt u voor liter nummer " + str(p) + " ? A) Aardbei, C) Chocolade, V) Vanille of M) Munt? : ")).lower()
        zakelijkBon()
    else:
        print (sorry)
        zakelijk()

def zakelijkBon():
    print("")
    print("-------------[Papi Gelato]-------------")
    print("")
    literPrijs = "{:.2f}".format(round(float(literIjs)*9.80 , 2))
    literBTW = "{:.2f}".format(round(float(literIjs)*9.80 / 100 * 9, 2))
    #literBTW = literIjs * 9.80 / 100 * 9
    print("Liter:           ", literIjs,       "x € 9.80 = €",literPrijs)
    print("                               ------ +")
    print("Totaal:                        €",literPrijs)
    print("BTW:                           €",literBTW)

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
    toppingprijsprijs = "{:.2f}".format(round(float(toppingsaantal)*(toppingprijs) , 2))
    totalTopping = float(toppingsaantal) * float(toppingprijs)
    tussenBon = float(total) + float(totalBakje) + float(totalHoorntje) + float(totalTopping)
    print("Bolletjes:       ", bol ,           "x € 1.10 =  €",total)
    print("Horrentje:       ", hoorntjeAantal ,"x € 1.25 =  €",totalHoorntje)
    print("Bakje:           ", bakjeAantal,    "x € 0.75 =  €",totalBakje)
    print("Topping:         ", toppingsaantal, "x €", toppingprijsprijs," =  €", totalTopping )
    print("                                ------ +")
    print("Totaal:                         €",tussenBon)

def begin():
    global bol, deel, hoorntjeAantal, bakjeAantal, hoorntje
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
                    toppings()
                    bestel()
                elif hoorntje == "b":
                    bakjeAantal+= 1
                    deel = "bakje"
                    smaken()
                    toppings()
                    bestel()
                else:
                    print (sorry)
        elif bol >=4 and bol <=8:
            deel = "bakje"
            smaken()
            toppings()
            bestel()
        else:
            print("Sorry, ik snap het niet...")
print("Welkom bij Papi Gelato. ")
zakelijk()