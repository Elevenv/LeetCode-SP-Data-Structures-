# https://leetcode.com/problems/linked-list-cycle/?envType=study-plan&id=data-structure-i


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # AddressList = []
        # while head:
        #     if head not in AddressList:
        #         AddressList.append(head)
        #         head = head.next
        #     else:
        #         return True
        # return False
        
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
