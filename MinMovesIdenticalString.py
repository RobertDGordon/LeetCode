# You are given a string S consisting of N letters 'a' and/or 'b'.
# In one move, you can swap one letter for the other ('a' for 'b' or 'b' for 'a')
#
# Write a function solution that, given such a string S
# returns the minimum number of moves required to obtain a string
# containing no instances of three identical consecutive letters.
#
# Examples:
# 1. Given S = "baaaaa", the function should return 1
#  The string without three identical consecutive letters which can be obtained in one move is "baabaa".
#
# 2. Given S = "baaabbaabbba", the function should return 2.
#  There are four valid strings obtainable in two moves: for example, "bbaabbaabbaa".
#
# 3. Given S = "baabab", the function should return 0.
#
# Write an efficient algorithm for the following assumptions:
# N is an interger within the range [0..200,000]
# string S consists only of the characters "a" and/or "b"

# [baaaaa]
# [baabaa]
# [baaabbaabbba]
# [bbaabbaabbaa]

# loop through string
# check each char
    # if a increment a count
        #reset b count (checking for consecutive a's)
    # if b increment b count
        #reset a count (checking for consecutive b's)
    # if a or b = 3
        # increment moves count
        # reset counters

def minMove(s):
    a = 0
    b = 0
    moves = 0
    for c in s:
        if c == 'a':
            a += 1
            b = 0
        elif c == 'b':
            a = 0
            b += 1
        if a == 3 or b == 3:
            moves += 1
            a = 0
            b = 0
    return moves

s = 'baabab'

assert minMove('baaaaa') == 1
assert minMove('baaabbaabbba') == 2
assert minMove('baabab') == 0
assert minMove('aaabb') == 1
assert minMove('baabb') == 0
assert minMove('baaab') == 1
assert minMove('baaaab') == 1
assert minMove('baaaaab') == 1
assert minMove('baaaaaab') == 2