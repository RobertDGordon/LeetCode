#Loop through each string, add each input to hash table?
#

def longestCommonPrefix(strs):
    strs.sort()
    strs.sort(reverse=True, key = lambda x:len(x))
    print(strs)
    prefix = ""
    first = strs[0][0]
    for current_string in range(len(strs)-1):
        if strs[current_string][0] == strs[current_string + 1][0]:
            print("match:", strs[current_string][0])
        for index, char in enumerate(strs[current_string]):
            # print(index, ch)
            pass

    return prefix

strs=["flower","racecar","flow","flight","fireys"]

longestCommonPrefix(strs)