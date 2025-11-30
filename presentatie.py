mijn_dict={
    "vis":10,
    "vlees":25,
    "overig":15
}
totaal=50
keys=mijn_dict.keys()
values=mijn_dict.values()

def presenteer(mijn_dict,totaal):
    lengte=25
    for keys,values in mijn_dict.items():
        print(f"{keys} : {values} euro")
    print(lengte*"=")
    print(f"totaal : {totaal} euro")
