# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first_node = None
        temp = head
        count = 0
        
        while temp:
            if count == k-1:
                first_node = temp
            temp = temp.next
            count += 1
            
        second_node = None
        temp = head
        for _ in range(count-k+1):
            second_node = temp
            temp = temp.next
            
        first_node.val, second_node.val = second_node.val, first_node.val
        return head
            