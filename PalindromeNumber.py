# def isPalindrome(x: int) -> bool:
#     rev = str(x)
#     rev = rev[::-1]
#     if str(x) == rev:
#         return True
#     else:
#         return False

def isPalindrome(x: int) -> bool:
    rev = 0
    init_n = x
    if( x < 0):
        return False
    while x != 0:
            print('\nrev:', rev,'* 10 =', rev * 10)
            print('x:', x,'% 10 =', x % 10)
            rev = (rev*10) +  x % 10
            print('// x:', x / 10)
            x = x // 10
            print('final rev:', rev, ' x:', x)

    if(rev == init_n):
                return True
    return False

isPalindrome(1234)

x = 1234
rev = 0
