#create result array
#find max value in array
#loop over array
#check if adding extra candies to current element >= max value
#append result to result array

def kidsWithCandies(candies, extraCandies):
    maximum = max(candies)
    result = []
    for kid in candies:
        if kid + extraCandies >= maximum:
            result.append(True)
        else:
            result.append(False)
    return result

print(kidsWithCandies([4,2,1,1,2], 1))