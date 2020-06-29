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