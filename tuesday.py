def twoSum(nums, target):
    numset = {}
    for index, number in enumerate(nums):
        compliment = target - number
        # print(index, number)
        if compliment in numset:
            return [numset[compliment], index]
        numset[number] = index
    return []

# nums = [2, 7, 11, 15]
# target = 9

nums = [3, 3]
target = 6

print(twoSum(nums, target))