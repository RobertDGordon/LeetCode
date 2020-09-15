#Loop through each string, add each input to hash table?
#

def longestCommonPrefix(strs):
    strs.sort()
    prefix = ""
    for i in range(len(strs)):
        first = strs[i][0]
        print(first)
        for index, ch in enumerate(strs[i]):
            # print(index, ch)
            pass

    return prefix

strs=["flower","flow","flight"]

longestCommonPrefix(strs)