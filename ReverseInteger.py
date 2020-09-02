def reverse(self, x: int) -> int:
    rev = str(x)    
    neg = False
    if rev[0] == '-':
        neg = True
        rev = rev[1:]
    rev = int(rev[::-1])
    if rev < -2**31:
        return 0
    if rev > 2**31 - 1:
        return 0
    if neg == True:
        rev = rev * -1
    return rev