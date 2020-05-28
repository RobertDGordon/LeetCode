# newlist = ListNode
# Loop through list1:
#     if list1.head <= list2.head:
#         add list1 node at beginning
#         then add list2 node
#         point list1 next to added list2 node
#     elif list1 > list2:
#         add list2 node at beginning
#         then add list1 node
#         point list2 next to added list1 node`
#     advance nodes

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class Solution:
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    newList = ListNode
    list1 = l1
    list2 = l2
    while list1 is not None:
        if list1.val <= list2.val:
            newNode = ListNode(list1.val)
            newNode.next = ListNode(list2.val)
            newList.next = newNode
        # elif list1.val > list2.val:
        #     newNode = ListNode(list2.val)
        #     newNode.next = ListNode(list1.val)
        list1 = list1.next
        list2 = list2.next
    return newList.next

l1 = ListNode(1)
new_node = ListNode(2)
l1.next = new_node
new_node.next = ListNode(4)

l2 = ListNode(1)
new_node = ListNode(3)
l2.next = new_node
new_node.next = ListNode(4)

# nodePrint = l2
# while nodePrint is not None:
#     print(nodePrint.val)
#     nodePrint = nodePrint.next

new_print = mergeTwoLists(l1, l2)
nodePrint = new_print
while nodePrint is not None:
    print(nodePrint.val)
    nodePrint = nodePrint.next