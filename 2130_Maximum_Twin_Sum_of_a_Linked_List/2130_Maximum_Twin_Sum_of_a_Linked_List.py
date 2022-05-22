# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:     
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        temp = head
        tempHead = head
        count = 0
        maxSum = 0
        
        while temp:
            count += 1
            temp = temp.next
        halfWay = count // 2
        
        while count > halfWay:
            stack.append(tempHead)
            count -= 1
            tempHead = tempHead.next
      
        while tempHead:
            temp2 = stack.pop()
            if tempHead.val + temp2.val > maxSum:
                maxSum = tempHead.val+ temp2.val
            tempHead = tempHead.next
        return maxSum
        
