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
