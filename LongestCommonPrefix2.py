#compare first word in array to next word
#loop over both words at same time
    #add matching letters to result
    #if letters at current position do not match, stop loop, advance to next words
    #append result to result array
#return longest result from result array

def longestCommonPrefix(strs):
    if len(strs) == 0 or "" in strs:
        return ""
    elif len(strs) == 1: #leetcode is annoying
        return strs[0]
    result = []
    for index in range(len(strs) - 1):
        word = strs[index]
        nextword = strs[index + 1]
        # print('words', word, nextword)
        #switch words based on length
        if len(word) > len(nextword):
            word, nextword = nextword, word
            # print('switched', word, nextword)
        subresult = ''
        for ndex in range(len(word)):
            if word[ndex] == nextword[ndex]:
                # print('match:', word[ndex], '==', nextword[ndex])
                subresult += word[ndex]
        result.append(subresult)
    # print(result)
    if len(result) > 0:
        return(min(result))


strs = ['flight', 'flower', 'flow']

# print('return', longestCommonPrefix(strs))

def longestCommonPrefixFast(strs):
    strs.sort()
    result = ""
    for x, y in zip(strs[0], strs[-1]):
        print(x, y)
        if x == y: 
            result += x
        else: break
    return result

print(longestCommonPrefixFast(strs))