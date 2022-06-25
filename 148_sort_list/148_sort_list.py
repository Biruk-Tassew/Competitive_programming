#Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middle(self, head):
        if not head or not head.next:
            return head
        
        fast = head.next
        slow = head
        
        while fast.next and fast.next.next:
            slow = slow.next            
            fast = fast.next.next            
            
        return slow

    def merge(self, left, right):       
        temp = ListNode(0)
        temp_node = temp

        while left and right:
            if left.val <= right.val:
                temp_node.next = left
                left = left.next
            else:
                temp_node.next = right
                right = right.next
            
            temp_node = temp_node.next
            
        if left:
            temp_node.next = left
        
        if right:
            temp_node.next = right
        
        return temp.next
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        middle = self.middle(head)

        right = self.sortList(middle.next)
        
        middle.next = None
        left = self.sortList(head)        
        
        return self.merge(left, right)
