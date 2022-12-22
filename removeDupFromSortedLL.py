# https://leetcode.com/problems/remove-duplicates-from-sorted-list/?envType=study-plan&id=data-structure-i


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # temp = head
        # l = []
        # while temp:
        #     if temp.val not in l:
        #         l.append(temp.val)
        #     temp = temp.next

        # dummy = ll = ListNode(0)

        # for i in l:
        #     ll.next = ListNode(i)
        #     ll = ll.next
        
        # return dummy.next

# OR

        # temp = head
        # while temp:
        #     temp2 = temp
        #     while temp2:
        #         if temp.val == temp2.val:
        #             temp.next = temp2.next
        #         temp2 = temp2.next
        #     temp = temp.next
        
        # return head

# OR

        curr = head

        while curr:
            while curr.next and curr.next.val == curr.val:
                curr.next = curr.next.next
            
            curr = curr.next

        return head