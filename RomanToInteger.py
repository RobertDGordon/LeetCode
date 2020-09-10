# Loop over string until it reaches I
# Seperate at I
# Create marker, set true at I
# Calculate first half (pre I) of the string
# Calculate second hald (post I)
# Add together and return



def romanToInt(s):
    firsthalf = ""
    secondhalf = ""
    marker = False
    for char in s:
        if char == "I" and marker == False:
            marker = True
        if marker == False:
            firsthalf += char
        if marker == True:
            secondhalf += char
    print(firsthalf, secondhalf)

romanToInt("MCMIV")