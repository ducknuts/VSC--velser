agehash = { 'Peter K' : 34, 
            'Peter P' : 29, 
            'Lars' : 41, 
}

for name, age in agehash.items():
    print(f'{name} is {age} years old.')

agehash['Peter K'] = 35
agehash['Andrew'] = 44
print( '-' * 50)

for name in agehash.keys():
    print(f'{name} is {agehash[name]} years old')

aldre = agehash.values()
print(f"Summen af personernes alder er {sum(aldre)}.")