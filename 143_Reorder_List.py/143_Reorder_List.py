from math import *
class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head):
        if not head and not head.next:
            return
        temp_head = head
        listLen = 0
        while temp_head:
            listLen += 1
            temp_head = temp_head.next

        temp_head = head
        for _ in range(ceil(listLen/2) - 1):
            temp_head = temp_head.next
    

        prev = temp_head
        temp_head = temp_head.next

        prev.next = None
        prev = None
        
        curr = temp_head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        left = head
        right = prev
        while left and right:
            left_next = left.next
            right_next = right.next

            left.next = right
            right.next = left_next

            left = left_next
            right = right_next
        return head
