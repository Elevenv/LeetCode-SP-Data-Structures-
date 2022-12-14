# https://leetcode.com/problems/merge-two-sorted-lists/?envType=study-plan&id=data-structure-i


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if list1 == list2 == None:
        #     return None
        # l1 = []
        # ptr1 = list1
        # ptr2 = list2
        # while ptr1!=None:
        #     l1.append(ptr1.val)
        #     ptr1 = ptr1.next
        
        # while ptr2!=None:
        #     l1.append(ptr2.val)
        #     ptr2 = ptr2.next
        
        # l1.sort()
        # list3 = ListNode(l1[0])
        # # c = ptr.ListNode(c[0])
        # head = list3
        # for i in range(1,len(l1)):
        #     list3.next = ListNode(l1[i])
        #     list3 = list3.next
        
        # return head

        if list1 == list2 == None:
            return None
        
        dummy = cur =ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        # cur.next = list1 or list2
        if list1:
            cur.next = list1
        elif list2:
            cur.next = list2
        return dummy.next
