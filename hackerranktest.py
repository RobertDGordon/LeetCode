def removeKthLinkedListNode(head, k):
    # set two pointers at the head
    fast = head
    slow = head

    #advance the fast pointer until the Kth position in the SLL
    for i in range(k):
        fast = fast.next
        #if fast pointer reaches end of SLL before K value, kick out of function and return the next value(edge case)
        if fast.next == None:
            return head.next
    
    #advance both pointers at same speed until fast reaches end of SLL
    while fast.next:
        fast = fast.next #advance until end
        slow = slow.next #when fast pointer is at end, slow pointer will be at previous to Kth

    #finally delete the kTh node by setting slow.next to the node after
    slow.next = slow.next.next

    #return beginning of SLL
    return head

    #time complexity: O(n) - looping until n value, n is the length of SLL
    #space complexity: O(1) - using two pointers to track memory addresses(nodes), and no arrays/lists

def balancedBrackets(string):
    #create counters for each bracket type (open and closed)
    #O is open, C is closed
    squareO = 0
    curlyO = 0
    smoothO = 0
    squareC = 0
    curlyC = 0
    smoothC = 0
    ors = 0 #counter for | (or operator), must be even at end

    #loop over each character in string
    for char in string:
        #increment counters
        if char == "[":
            squareO += 1
        if char == "{":
            curlyO += 1
        if char == "(":
            smoothO += 1
        if char == "]":
            squareC += 1
        if char == "}":
            curlyC += 1
        if char == ")":
            smoothC += 1
        if char == "|":
            ors += 1
    
    #check if amount of open brackets is equal to closed brackets and even number of | operators
    if squareO == squareC and curlyO == curlyC and smoothO == smoothC and ors%2 == 0:
        return True
    else:
        return False

    #time complexity: O(n) - looping n times, n for each character in string
    #space complexity: O(1) - using counters to track each type of bracket, no arrays/lists

def threeNumberSum(arr, target):
    #sort array
    arr.sort()
    print("input", arr, target)
    #create array for result
    result = []
    #create set using arr for fast number searching
    numSet = set(arr)
    #create flagged dict
    flagged = {}

    #edge cases:
    if len(arr) < 3:
        return result #if length is less than three, no matches possible, return empty array
    if len(arr) == 3:
        return [arr] #if length is three, no need to calculate, return three numbers in array
    
    if target == 0:
        for index, num in enumerate(arr): #loop over arr, using enumerate to have index count
            for num2 in arr[arr[index]:]: #loop over arr starting at current index of outer loop, set to num2
                #check if outer loop number(positive value) minus inner loop value is in the array(numSet), means the equation has a match
                #also check if num2 has not been added to flagged
                if abs(num) - num2 in numSet and num2 not in flagged.values():
                    third = abs(num) - num2 #third number in equation
                    flagged.update({abs(num): num2}) #flag both numbers, setting outer loop as key, and inner loop as value
                    newArr = [num, num2, third]
                    #print('flagging', third, 'num2', num2)
                    print('found', abs(num), '-', num2, '=', third)
                    result.append(newArr) #add the matched equation to the result as a 2d dimensional array
                return result

    #simple case, loop over each number and calculate
    for num in arr:
        #check if target divided by two minus current number is in numSet
        #also check that current num has already not been flagged
        #target must be divided by two because it will be the third number in the compliment
        if target/2 - num in numSet and num not in flagged.values():
            second_num = target/2 - num #second_number in compliment
            flagged.update({num:int(second_num)}) #add numbers to flagged dict
            result.append([num, int(second_num), int(target/2)]) #add to result
    print("flagged", flagged)
    return result

    #time complexity: O(n2) quadratic time, using loop within a loop, can possibly improve by taking second loop out of first 
    #space complexity: 0(n), linear space that increases depending on the size of the array, uses set/dict to check values, and returns 2d list

def threeNumberSum2(arr, target):
    tuples = []
    available = {}
    arr.sort()

    for i in range(len(arr)):
        available[arr[i]] = i

    for i in range(len(arr) - 2):
        for j in range(i + 1,len(arr) - 1):
            need = target - arr[i] - arr[j]
            if need in available and available[need] > j:
                tuples.append([arr[i],arr[j],need])

    return tuples

    #add more comments