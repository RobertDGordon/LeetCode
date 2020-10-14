#create count variable
#loop over array
#loop over array starting at +1
#check if outer elem == inner elem AND outer < inner

def numIdenticalPairs(nums):
    count = 0
    for outer in range(0, len(nums)):
        for inner in range(1, len(nums)):
            if nums[outer] == nums[inner] and outer < inner:
                count += 1
    return count

print(numIdenticalPairs([1,2,3,1,1,3]))