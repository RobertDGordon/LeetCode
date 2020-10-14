#loop over string
#increment count if open
#decriment count if closed
#check if count is greater than nest
    #set nest = count
#return nest

def maxDepth(s):
    count = 0
    nest = 0
    for char in s:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
        if count > nest:
            nest = count
    return nest

s = "()(()())"

print(maxDepth(s))