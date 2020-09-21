#return true if all brackets are closed, in the correct order
#return false if uneven number, or out of order
#edge cases?
#test cases?

#Loop over string
#Break loop if closed bracket is found before open
#If open bracket is found, add to specific bracket counter type
    #If other type of open bracket is found, set flag to true
    #If closed bracket of original type is found while flag is true, break
    #If closed bracket of second type is found while flag is true, set flag to false and continue
#If closed bracket is found, add to specific closed bracket counter
#check that open brackets are equal to closed brackets, return true, else false

def isValid(s):
    smoothO = 0
    smoothC = 0
    curlyO = 0
    curlyC = 0
    squareO = 0
    squareC = 0
    flag = False
    flagtype = ""