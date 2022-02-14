def my_input() -> int:   
    while True:    
        try:
            result = int(input("Indtast et nummer eller cancel (CTRL + C): "))  
        except ValueError:
            print("Indtast venligst et helt tal. ")
        except KeyboardInterrupt:
            print("\n Bruger har annulleret. ")
            return None
        else:
            return result

i = my_input()
if i is not None:
    print("User input %d" % i)