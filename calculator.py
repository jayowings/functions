# Get info from users
# TODO user input validation for menu and numvber
# TODO convert string to number
#conversion facts
def MMToIn(Inputt):
    return Inputt / 25.4
def InToMM(Inputt):
    return Inputt * 25.4
def InToFt(Inputt):
    return Inputt /12

# Perform the conversion
def printResults(userConversionInput, userInputx):
    if userConversionInput == '1':
        userAnswer = InToMM(userNumber)
        conversionUnit = ("in")
        ConvertedUnit = ('mm')
    if userConversionInput == '2':
            userAnswer = MMToIn(userNumber)
            conversionUnit = ('mm ')
            ConvertedUnit = ('in')
    if userConversionInput == '3':
            userAnswer = InToFt(userNumber)
            conversionUnit = ('in')
            ConvertedUnit = ('ft')
    print ("The answer is", userInputx, conversionUnit, "=", userAnswer, ConvertedUnit + ".")

while True:
    userConversionInput = input ('What type of conversion? \n\t 1 - inches to mm \n\t 2 - mm to inches \n\t 3 - inches to feet \n\t Q to Quit \n')
    if userConversionInput == "Q":
        break
    userInput = input('What is the number: ')
    print ('Your number is:', userInput) # TODO remove for production
    userNumber = float(userInput) #
    
    # Print out the answer
    printResults(userConversionInput, userInput)