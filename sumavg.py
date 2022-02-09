def subave(number):
    ialt = 0
    for x in range(number + 1):
        ialt += x
    return print(f"Der er i alt {ialt} fra 1 til {number}. Gennemsnittet af alle de tal er: {ialt/number}.")

subave(int(input("Indtast et nummer og jeg giver dig summen og gennemsnittet af 1 til dit nummer: ")))
