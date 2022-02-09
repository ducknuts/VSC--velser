print("Test om du skal have lys på cyklen: ")


tid = 0
print("Test om lysene skal tændes: ")

def biking_bool():
    biking = input("Cykler du? Ja/Nej ").lower()
    if biking == "ja":
        return True
    if biking == "nej":
        return False
biking_bool()

if biking_bool == True:
    tid = int(input("Skriv nærmeste hele tidsslæt (kun timer): "))


def LightsOn(biking_bool, tid):
    if biking_bool == True:
        if tid < 8 or tid > 18:
            print("Du skal have lys på (True)")
    else: print("Det er lyst, ingen lyskrav.")

LightsOn(biking_bool, tid)
