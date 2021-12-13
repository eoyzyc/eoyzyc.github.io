import random
import time
##element = ['hydrogen','helium','lithium','beryllium','boron','carbon','nitrogen','oxygen','flourine','neon','sodium','magnesium',]
##RAM = ['1','4','7','9','11','12','14','16','19','20','23','24']
Element = {'hydrogen':1,'helium':4,'lithium':7,'beryllium':9,'boron':11,'carbon':12,'nitrogen':14,'oxygen':16,'flourine':19,'neon':20,'sodium':23,'magnesium':24,'alluminium':27,'silicon':28,'phosphorus':31,'sulfur':32,'chlorine':35.5,'argon':40}
keyList = list(Element)
values = Element.values()
valuesList = list(values)
avogadroC = 6*10**23
##==========starting, type of question choice==========##
print("This is a mole concept tester")
flag = True
while True: 
    print("What kind of question do you want to answer?")
    print("""      a) Calculate moles, given number of particles and elementa
        b) calculate number of particles, given numebr of moles
        c) calculate moles, given the element and mass of substance
        d) calcualte mass, given moles and element""")
    choice = input("choose ==> a,b,c,d: ")
    ##==========option a==========##  
    if choice == 'a':
        print("you have chose 'a' ")
        print("Calculate moles, given number of particles.")
        aNOP = random.randint(100,999)/100
        aTheElement = random.randint(0,11)
        aElement = keyList[aTheElement]
        print("The question: Calculate the number of moles there are in " + str(aNOP) + "x10^24 " + str(aElement) + " atoms.")
        aAns = (aNOP*10**24)/avogadroC
        aAnsRound = round(aAns, 2)
        Flag = True
        while True:
            aAnsCheck = input("What is your answer corrected to 2 dp?: ")
            if aAnsCheck == str(aAnsRound):
                print("Congragulation u got it correct!")
                break
            else: 
                print("Sorry you got it wrong...")
    ##==========option b==========#
    elif choice == 'b':
        print("you have chose 'b' ")
        print("calculate number of particles, given numeber of moles.")
        bMoles = random.randint(100,1500)/100
        bTheElement = random.randint(0,11)
        bElement = keyList[bTheElement]
        print("The question: How many atoms are there in " + str(bMoles) + " moles of " + str(bElement) + ".")
        bAns = bMoles*avogadroC/(10**24)
        bAnsRound = round(bAns, 2)
        Flag = True
        while True:
            bAnsCheck = input("What is your answer corrected to 2dp(__x10^24)?: ")
            if bAnsCheck == str(bAnsRound):
                print("Congragulation u got it correct!")
                break
            else: 
                print("Sorry you got it wrong...")
    ##==========option c==========##
    elif choice == 'c':
        print("you have chose 'c' ")
        print("calculate moles, given the element and mass of substance.")
        cWeight = random.randint(1, 99999)/100
        cTheElement = random.randint(0,11)
        cElement = keyList[cTheElement]
        cRAM = valuesList[cTheElement]
        print("The question: How many moles are there in " + str(cWeight) + "g of " + str(cElement) + "? ")
        cAns = cWeight/cRAM
        cAnsRound = round(cAns, 2)
        Flag = True
        while True:  
            cAnsCheck = input("What is your answer corrected to 2dp?: ")
            if cAnsCheck == str(cAnsRound):
                print("Congragulation u got it correct!")
                break
            else: 
                print("Sorry you got it wrong...")
    ##==========option d==========##
    elif choice == 'd':
        print("you have chose 'd' ")
        print("calcualte mass, given moles and element.")
        dMoles = random.randint(100,1500)/100
        dTheElement = random.randint(0,11)
        dElement = keyList[dTheElement]
        dWeight = random.randint(1, 99999)/100
        print("The question: How heavy is " + str(dWeight) + "g of " + str(dElement) + "?")
        dAns = dMoles*dWeight
        dAnsRound = round(dAns, 2)
        Flag = True
        while True:    
            dAnsCheck = input("What is your answer corrected to 2dp?: ")
            if dAnsCheck == str(dAnsRound):
                print("Congragulation u got it correct!")
                break
            else: 
                print("Sorry you got it wrong...")
    Flag = True
    while True:
        tryAgain = input("Do you want to try again? (y/n)")
        if tryAgain == 'y':
            print("Next question")
            break
        elif tryAgain == 'n':
            print("Goodbye")
            time.sleep(2)
            exit()
    
