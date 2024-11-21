# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_l = ListNode()
        dummy_node = new_l

        off_set = 0
        while l1 or l2 or off_set:

            if l1:
                off_set += l1.val
                l1 = l1.next
            
            if l2:
                off_set += l2.val
                l2 = l2.next

            new_l.next = ListNode(val = off_set%10)
            off_set //= 10
            new_l = new_l.next



        
        return dummy_node.next
        