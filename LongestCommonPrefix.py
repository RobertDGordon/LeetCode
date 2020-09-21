#Loop through each string, add each input to hash table?
#

def longestCommonPrefix(strs):
    if len(strs) < 1:
        return ""
    strs.sort()
    strs.sort(key = lambda x:len(x))
    # print(strs)
    prefix = ""
    first = strs[0][0]
    for current_string in range(len(strs)-1):
        if strs[current_string][0] == strs[current_string + 1][0]:
            # print("match:", strs[current_string][0])
            prefix = strs[current_string][0]
            for second_index in range(len(strs[current_string])-1):
                # print("\nnext_char:", strs[current_string][second_index + 1])
                next_char = strs[current_string][second_index + 1]
                if next_char == strs[current_string + 1][second_index + 1]:
                    # print("second letter match:", strs[current_string + 1][second_index + 1])
                    prefix += strs[current_string + 1][second_index + 1]
                else:
                    break
        else:
            current_string += 1

    return prefix

strs=["flower","racecar","flow","flight","fireys"]

print(longestCommonPrefix(strs))