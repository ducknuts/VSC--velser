new_list = []

print("Indtast 10 tal:")
for x in range (10):
        userinput = int(input())
        new_list.append(userinput)

print(f"Summen af numrene er: {sum(new_list)}")
print(f"Det mindste tal er: {min(new_list)}")
print(f"Det største tal er: {max(new_list)}")
print(f"Gennemsnittet er: {sum(new_list)/10}")

