print("Jeg vil nu give dig summen og gennemsnittet af to numre, du indtaster.")
user_input = input("Skriv først det ene nummer: ")
user_input2 = input("Og nu det andet: ")

sum = int(user_input) + int(user_input2)
avg = (int(user_input) + int(user_input2))/2

print(f"Du har indtastet {user_input} og {user_input2}. Summen er {sum}, og gennemsnittet er {avg}.")