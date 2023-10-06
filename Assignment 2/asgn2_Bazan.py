#Ramiro Bazan
title="* * Check Education Level* *\n"
print(title)
#function start
def education():
    #Ask for name
    name=input("What is your name: ")
    #Using a number because it is easier to visualize
    level = 5
    while level == 5:
        #ask for Education
        educationLevel=input("Highest Education level? (Enter: HS, BS, MS, or PhD )")
        #repeat messages/text
        message= "Hello " + name + " your education level is a " + educationLevel
        levelMessage= "You have an " + educationLevel + "\n"
        error = educationLevel +" is not a known education level, try again \n"
       #Nested if/else used example 2.16
        if educationLevel == "HS":
            print(levelMessage)
            print(message)
            level=4
        else:
            if educationLevel == "BS":
                print(levelMessage)
                print(message)
                level=4
            else:
                if educationLevel == "MS":
                    print(levelMessage)
                    print(message)
                    level=4
                else:
                    if educationLevel == "PhD":
                        print(levelMessage)
                        print(message)
                        level=4
                    else:
                        print(error)
#call function
education()
print("END OF PROGRAM")
