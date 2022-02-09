decimal = int(input("Indtast et decimaltil, som jeg konverterer til binær: "))
i = 0
binær = []

while decimal != 0:
    rest = decimal % 2
    binær.insert(i, rest)
    i = i + 1
    decimal = int(decimal/2)

print(*binær[::-1])