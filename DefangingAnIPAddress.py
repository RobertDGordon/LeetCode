#create empty string
#loop over string
#if element is ".", append to empty string "[.]"
#else append element

def defangIPaddr(address):
    result = ""
    for elem in address:
        if elem == ".":
            result += "[.]"
        else:
            result += elem
    return result

print(defangIPaddr("10.10.1.1"))