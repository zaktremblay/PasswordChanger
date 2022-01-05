import random

def createRandomPassword(numberOfCharacters,includeLowerCharacters,includeUpperCharacters,includeIntegers,includeSymbols):
    
    lowerCaseAlphabet="abcdefghijklmnopqrstuvwxyz"
    upperCaseAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols="!@#$%?&*"
    inclusions = [includeLowerCharacters,includeUpperCharacters,includeIntegers,includeSymbols]
    numberOfDifferentCharacters=sum(inclusions)

    if numberOfCharacters>=numberOfDifferentCharacters:

        def getRandomLowerCharacter():
            return(random.choice(lowerCaseAlphabet))

        def getRandomUpperCharacter():
            return(random.choice(upperCaseAlphabet))

        def getRandomInteger():
            return(random.randint(0,9))

        def getRandomSymbol():
            return(random.choice(symbols))

        def containsLowerCharacter(currentPassword):
            return(any(character for character in currentPassword if character.islower()))
        
        def containsUpperCharacter(currentPassword):
            return(any(character for character in currentPassword if character.isupper()))

        def containsInteger(currentPassword):
            return(any(character for character in currentPassword if character.isdigit()))

        def containsSymbol(currentPassword):
            check = False
            for character in currentPassword:
                for symbol in symbols:
                    if character==symbol:
                        check=True
            return(check)

        password=""

        characterCreation=[getRandomLowerCharacter,getRandomUpperCharacter,getRandomInteger,getRandomSymbol]
        characterChecks=[containsLowerCharacter,containsUpperCharacter,containsInteger,containsSymbol]


        for iteration in range(numberOfCharacters):
            choiceOfNewCharacter=[]

            if ((numberOfCharacters-iteration)-numberOfDifferentCharacters)<0:
                for iteration, inclusion in enumerate(inclusions):
                    print(characterChecks[iteration](password))
                    if inclusion and not characterChecks[iteration](password):
                        choiceOfNewCharacter.append(characterCreation[iteration]())
                if not choiceOfNewCharacter:
                    for iteration, inclusion in enumerate(inclusions):
                        if inclusion:
                            choiceOfNewCharacter.append(characterCreation[iteration]())
            else:
                for iteration, inclusion in enumerate(inclusions):
                    if inclusion:
                        choiceOfNewCharacter.append(characterCreation[iteration]())

            print(choiceOfNewCharacter)
            print(password)
            newCharacter=random.choice(choiceOfNewCharacter)
            
            password=password+str(newCharacter)
        print(password)

    else:
        return(None)
        
createRandomPassword(5,bool(True),bool(True),bool(True),bool(True))
