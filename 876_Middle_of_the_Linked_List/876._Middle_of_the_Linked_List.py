# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp_head = head
        list_len = 0
        while temp_head:
            list_len += 1
            temp_head =temp_head.next
        temp_head = head
        for _ in range(floor(list_len/2)):
            temp_head = temp_head.next
    
        return temp_head
