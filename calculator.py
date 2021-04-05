# Get info from users
# TODO user input validation
# TODO convert string to number
userInput = input('What is the number: ')
print ('Your number is:', userInput) # TODO remove for production
userNumber = float(userInput) #

# Perform the conversion

# Convert in to mm 25.4 mm per in
# userAnswer = userNumber * 25.4

# Convert from mm to in
userAnswer = userNumber / 25.4

# Print out the answer
print ('The answer is: ', userAnswer)