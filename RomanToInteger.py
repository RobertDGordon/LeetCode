#Loop over string with enumerate
#If C check if next is D or M, subtract by add 400 or 900
#If X check if next is L or C, add 40 or 90
#If I check if next is V or X, add 4 or 9
#Add value to result




def romanToInt(s):
    # firsthalf = ""
    # secondhalf = ""
    # marker = False
    result = int
    # for char in s:
    #     if char == "I" and marker == False:
    #         marker = True
    #     if marker == False:
    #         firsthalf += char
    #     if marker == True:
    #         secondhalf += char
    for char, index in enumerate(s):
        if char == "M":
            result += 1000
        if char == "D":
            result += 500
        if char == "C":
            result += 100
        if char == "L":
            result += 50
        if char == "X":
            result +=10
    # print(firsthalf, secondhalf)

romanToInt("LVIII")