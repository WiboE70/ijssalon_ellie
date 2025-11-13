from algemene_functies import mijn_functie_2
print()
def aanbieding_1(smaak,prijs,korting):
    korting = prijs-(prijs*korting)
    return (f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting}  euro.")
print (aanbieding_1("aardbei",4, 0.1))

print()

def inkomsten_totaal(inkomsten,btw):
    totaal = sum (inkomsten)
    bedrag = totaal * btw
    return (f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden.") 
print (inkomsten_totaal([220, 430, 125, 160, 205, 90, 345],0.09))

print()

def laag_en_hoog(mijn_lijst):
    return max(mijn_lijst),min(mijn_lijst)
print (laag_en_hoog([220, 430, 125, 160, 205, 90, 345]))

print()

def gemiddelde(mijn_lijst):
    bedrag=sum(mijn_lijst) / len(mijn_lijst)
    return (f"De gemiddelde inkomsten deze week zijn {bedrag} euro.")
print (gemiddelde([220, 430, 125, 160, 205, 90, 345]))

print()

def meervoudig(invoer_lijst):
        return laag_en_hoog(invoer_lijst)
print (meervoudig([10,5,3,2,1,2,9]))

print()

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    return mijn_functie_2(korte_lijst[0],korte_lijst[1])
print (combinatie([14,5,3,8,2,9]))
