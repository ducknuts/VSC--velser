from datetime import datetime


fødselsår = input("Hvornår blev du født? ")
årstal = datetime.today().year
print(årstal - int(fødselsår))