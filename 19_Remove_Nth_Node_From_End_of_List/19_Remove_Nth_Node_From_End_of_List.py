# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        temp = head
        prev = head
        count = 0
        comp = 1
        
        while temp:
            count += 1
            temp = temp.next
        
        if count <= n or not head:
            return head.next
        while comp + n < count:
            print(comp, n, count)
            head = head.next
            comp += 1
            
        head.next = head.next.next
        return prev
