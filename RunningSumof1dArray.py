#create empty array
#loop over nums array
#append empty element + current nums element

def runningSum(nums):
    result = [0]
    for num in nums:
        result.append(result[-1] + num)
    return result[1:]

print(runningSum([1,2,3,4]))