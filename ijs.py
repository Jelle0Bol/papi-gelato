from time import sleep
import os
import sys

ijssalon = 1
stap2 = 1
stap3 = 1
stap4 = 1
aantalaantal = 1

def aantalbolletjes():
    global aantalb
    while aantalaantal > bol:
        hoeveel = str(input("Welke smaak wilt u voor bolletje",aantalaantal,"? : "))
        aantalaantal + 1


def smaken():
    global smaak
    smaak = str(input("Welke smaak wilt u voor bolletje nummer 1?. U kunt kiezen uit A) Aardbei, C) Chocolade, M) Munt en V) Vanilla : ")).lower()
    if smaak == "a":
        smaak= "Aardbei"
    elif smaak == "c":
        smaak = "Chocolade"
    elif smaak == "m":
        smaak= "Munt"
    elif smaak == "v":
        smaak= "Vanilla"
    else:
        print("Sorry, dat hebben we niet")
    

print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")
sleep(2.5)
while ijssalon == 1:
    bol = int(input("Hoeveel bolletjes ijs wilt u? : "))
    while bol >8:
        print("Welke smaak wilt u voor bolletje",bol,"? : ")
        print("Sorry, zulke grote bakken hebben we niet")
        bol = int(input("Hoeveel bolletjes ijs wilt u? : "))
    if bol >=1 and bol <=3:
        while stap2 == 1:
            hoorntje = str(input("Wilt u deze " + str(bol) + " bolletjes in A) een hoorntje of B) een bakje? : ")).lower()
            if hoorntje == "a":
                while stap3 == 1:
                        meer = str(input("Hier is uw hoorntje met " + str(bol) + " bolletjes. Wilt u nog meer bestellen? Y/N : ")).lower()
                        if meer == "y":
                            while 1:
                                os.system("python ijs.py")
                                exit()
                        elif meer == "n": 
                            print("Bedankt en tot ziens!")
                            sleep(2.0)
                            sys.exit()
            elif hoorntje == "b":
                while stap4 ==1:
                    nogmeer = str(input("Hier is uw bakje met " +str(bol) + " bolletjes. Wilt u nog meer bestellen? Y/N : ")).lower()
                    if nogmeer =="y":
                        while 1:
                            os.system("python ijs.py")
                            exit()
                    elif nogmeer =="n":
                        print("Bedankt en tot ziens!")
                        sleep(2.0)
                        sys.exit()
                print("Stap3")
            else:
                print("Sorry, dat snap ik niet")
    elif bol >=4 and bol <=8:
        supermeer = str(input("Hier is uw bakje met " +str(bol)+" bolletjes. Wilt u nog meer bestellen? Y/N : " )).lower()
        if supermeer =="y":
            while 1:
                os.system("python ijs.py")
                exit()
        elif supermeer =="n":
            print("Bedankt en tot ziens!")
            sleep(2.0)
            sys.exit()
    else:
        print("Sorry, ik snap het niet...")
