#each character in the string is a value
#parse the jewels string into a dict
#loop over stones string and increment counter on match

def numJewelsInStones(J, S):
    count = 0
    jewels = []
    for jewel in J:
        jewels.append(jewel)
    for stone in S:
        if stone in jewels:
            count += 1
    return count

J = "abced"
S = "abd"
print(numJewelsInStones(J, S))