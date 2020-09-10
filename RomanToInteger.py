#Create Index
#Loop over string
#If C check if next is D or M, add 400 or 900
    #If true, advance index by 1
#If X check if next is L or C, add 40 or 90
    #If true, advance index by 1
#If I check if next is V or X, add 4 or 9
    #Check if index + 1 is in range
    #If true, break
#Add value to result
#Advance index




def romanToInt(s):
    # firsthalf = ""
    # secondhalf = ""
    # marker = False
    result = 0
    # for char in s:
    #     if char == "I" and marker == False:
    #         marker = True
    #     if marker == False:
    #         firsthalf += char
    #     if marker == True:
    #         secondhalf += char
    index = 0
    while index in range(len(s)):
        # print("loop:", s[index], index)
        char = s[index]
        if char == "M":
            result += 1000
        elif char == "D":
            result += 500
        elif char == "C":
            if s[index + 1] == "D":
                result += 400
                index += 1
            elif s[index + 1] == "M":
                result += 900
                index += 1
            else:
                result += 100
        elif char == "L":
            result += 50
        elif char == "X":
            if s[index + 1] == "L":
                result += 40
                index += 1
            elif s[index + 1] == "C":
                result += 90
                index += 1
            else:
                result += 10
        elif char == "V":
            result +=5
        elif char == "I":
            if index + 1 < len(s):
                if s[index + 1] == "V":
                    result += 4
                    break
                elif s[index + 1] == "X":
                    result += 9
                    break
                else:
                    result += 1
            else:
                result += 1
        index += 1
    return(result)

    # print(firsthalf, secondhalf)

print(romanToInt("MCMXCIV"))