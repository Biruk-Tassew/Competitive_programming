# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    temp = ListNode('')
    def checkPalindrome(self, head):
        global temp
        if not head:
            return True
        
        outPut = self.checkPalindrome(head.next) and head.val == temp.val
        temp = temp.next
        return outPut
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        global temp 
        temp = head
        return self.checkPalindrome(head)
