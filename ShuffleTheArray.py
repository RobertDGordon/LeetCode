#n is the split
#split the array into two arrays with length of n
#create result array
#loop over both split arrays
#append both elements to result

def shuffle(nums, n):
    x = nums[:n]
    y = nums[n:]
    result = []
    for i in range(0, n):
        result.append(x[i])
        result.append(y[i])
    return result

print(shuffle([2,5,1,3,4,7], 3))