# Get info from users
# TODO user input validation for menu and numvber
# TODO convert string to number
# Menu system 1-inches to mm 2-mm to inches
userConversionInput = input ('What type of conversion? \n\t 1 - inches to mm; \n\t 2 - mm to inches \n')
userInput = input('What is the number: ')
print ('Your number is:', userInput) # TODO remove for production
userNumber = float(userInput) #

def calculate(userNumber, conversionType):
    if conversionType == '1':
                userAnswer = userNumber * 25.4
    if conversionType == '2':
                userAnswer = userNumber / 25.4
    return userAnswer

def printResults(userConversionInput, userInput, calcValue):
    if userConversionInput == '1':
        conversionUnit = ("in")
        ConvertedUnit = ('mm')
    if userConversionInput == '2':
        conversionUnit = ('mm ')
        ConvertedUnit = ('in')
        
    print ("The answer is", userInput, conversionUnit, "=", calcValue, ConvertedUnit + ".")

# Perform the conversion

calcValue = calculate(userNumber, userConversionInput)
# Print out the answer

printResults(userConversionInput, userInput, calcValue)