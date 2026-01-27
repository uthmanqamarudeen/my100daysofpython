print("Welcome to Dr Glam's mini story zone!")
name = input("What's Dr Glam's name?, just a name of his! \n").strip().lower()
if name == "uthman" or name == "qamarudeen" or name == "adesina":
    print("Correct! Unto the next ✌️")
    glam = input("He's being called Glam, what's the name powering this unique abridged nickname of his? \n").strip().lower()
    if glam == "glamour":
        print("Correct! Unto the next ✌️")
        whose_legacy = input("Whose legacy is the name 'Glamour' trying to upheld? \n").strip().lower()
        if whose_legacy == "father" or whose_legacy == "daddy" or whose_legacy == "papa" or whose_legacy == "dad":
            print("Correct! Unto the next ✌️")
            legacy = input("What's dad's legacy? \n Carpentry, Photography, Shoemaking, Entrepreneur? \n").strip().lower()
            if legacy == "photography":
                print("Correct! Unto the next ✌️")
                profession = input("Apart from his legacy as a photographer, what was his main profession from the above options? \n").lower()
                if profession == "entrepreneur":
                    print("That's great! It's a win, and you've succesfully completed this mini story challenge\nI guess you're close to Dr Glam!? 😎")
                else:
                    print("That was so close, probably you might have won it.\nYou've come so far up to this, try again, you might be luckier!")
            elif legacy == "entrepreneur":
                  print("You're close, he was also an entrepreneur, but that's not the exact thing upholding \"glamour's\" legacy! \nTry again!")  
            else:
                print("You're incorrect! Game's over")  
        else: 
           print("You're incorrect! Game's over") 
    else:
        print("You're incorrect! Game's over")
else: 
    print("You're incorrect! Game's over")
   