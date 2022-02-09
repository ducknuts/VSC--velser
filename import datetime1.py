import datetime

print("Test om du skal have lys på cyklen: ")

def cykel_eller_ej():
    biking = input("Cykler du? Ja/Nej ").lower()
    if biking == "ja":
        return True
    else:
        return False

now = datetime.datetime.now()

def LightsOn():
    if cykel_eller_ej() == True:
        if now.hour < 8 and now.hour > 18:
            print("Det er tidligere end 8 eller senere end 18.Det er mørkt, tag lys på.")
        else: print("Klokken er mellem 8 og 18. Du behøver ikke have lys på på dette tidspunkt. ")
    if cykel_eller_ej == False:
        print("Du cykler ikke, don't bother. ")
LightsOn()