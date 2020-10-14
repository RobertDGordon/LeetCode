#compare first word in array to next word
#loop over both words at same time
    #add matching letters to result
    #if letters at current position do not match, stop loop, advance to next words
    #append result to result array
#return longest result from result array

def longestCommonPrefix(strs):
    result = []
    for index in range(len(strs) - 1):
        word = strs[index]
        nextword = strs[index + 1]
        print('words', word, nextword)
        #switch words based on length
        if len(word) > len(nextword):
            word, nextword = nextword, word
            print('switched', word, nextword)
        subresult = ''
        for ndex in range(len(word)):
            if word[ndex] == nextword[ndex]:
                print('match:', word[ndex], '==', nextword[ndex])
                subresult += word[ndex]
            else:
                break
        result.append(subresult)
    print(min(result))

strs = ["flower","flow","flight", "fluxed", "flagrant", "flood"]

longestCommonPrefix(strs)