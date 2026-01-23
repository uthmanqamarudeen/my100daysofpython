year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        #if year % 400 == 0:
         #   print("This is a leap year")
        #else:
         #   print("This is not a leap year")
         print("This is a leap year")
    elif year % 400 == 0:
        print("This is a leap year")
    else:
        print("This year is a leap year")
else:
    print("This year is not a leap year")
    