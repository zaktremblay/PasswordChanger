import random

def createRandomPassword():

    inclusions = []

    includeUpperCharacters=inclusions.append(bool(input("upper characters?")))
    includeLowerCharacters=inclusions.append(bool(input("lower characters?")))
    includeIntegers=inclusions.append(bool(input("integers?")))
    includeSymbols=inclusions.append(bool(input("symbols?")))

    def getRandomLowerCharacter():
        lowerCaseAlphabet="abcdefghijklmnopqrstuvwxyz"
        return(random.choice(lowerCaseAlphabet))

    def getRandomUpperCharacter():
        upperCaseAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return(random.choice(upperCaseAlphabet))

    def getRandomInteger():
        return(random.randint(0,9))

    def getRandomSymbol():
        symbols="!@#$%?&*"
        return(random.choice(symbols))

    characterCreation=[getRandomLowerCharacter,getRandomUpperCharacter,getRandomInteger,getRandomSymbol]

    numberOfCharacters=int(input("how many characters:"))
    password=""

    #numberOfDifferentCharacters=sum(inclusions)

    #for inclusion in inclusions:
        #if inclusion:
            #numberOfDifferentCharacters+=1

    for iteration in range(numberOfCharacters):
        choiceOfNewCharacter=[]
        

        for iteration, inclusion in enumerate(inclusions):
            choiceOfNewCharacter.append(characterCreation[iteration]())
                
        """
        for iteration, inclusion in enumerate(inclusions):
            for differentCharacter in range(numberOfDifferentCharacters):
                if password[-differentCharacter] 

        """

        newCharacter=random.choice(choiceOfNewCharacter)
        
        password=password+str(newCharacter)
    print(password)

    #def containsLower():
