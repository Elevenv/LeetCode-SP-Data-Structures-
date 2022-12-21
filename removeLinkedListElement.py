# https://leetcode.com/problems/remove-linked-list-elements/?envType=study-plan&id=data-structure-i


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        dummy = prev = ListNode(next = head)
        curr = head

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr

            curr = curr.next

        return dummy.next

        # dummy = ll = ListNode(0)
        # while temp:
        #     if temp.val != val:
        #         ll.next = ListNode(temp.val)
        #         ll = ll.next
        #     temp = temp.next
        
        # return dummy.next