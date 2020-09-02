def isPalindrome(x: int) -> bool:
    rev = str(x)
    rev = rev[::-1]
    if str(x) == rev:
        return True
    else:
        return False
    
isPalindrome(-1210)