# Get info from users
# TODO user input validation for menu and numvber
# TODO convert string to number
# Menu system 1-inches to mm 2-mm to inches
userConversionInput = input ('What type of conversion? \n\t 1 - inches to mm; \n\t 2 - mm to inches \n')
userInput = input('What is the number: ')
print ('Your number is:', userInput) # TODO remove for production
userNumber = float(userInput) #

def printResults(userConversionInput, userInputx):
    if userConversionInput == '1':
        userAnswer = userNumber * 25.4
        conversionUnit = ("in")
        ConvertedUnit = ('mm')
    if userConversionInput == '2':
        userAnswer = userNumber / 25.4
        conversionUnit = ('mm ')
        ConvertedUnit = ('in')
    print ("The answer is", userInputx, conversionUnit, "=", userAnswer, ConvertedUnit + ".")

# Perform the conversion

# Print out the answer

printResults(userConversionInput, userInput)