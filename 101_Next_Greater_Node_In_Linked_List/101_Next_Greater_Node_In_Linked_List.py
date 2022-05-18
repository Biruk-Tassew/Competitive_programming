# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        if not head.next:
            return [0]
        
        outPut = []
        stack = []
        end = head
        
        while end:
            stack.append(end.val)
            end = end.next
        last = [0] * len(stack)
        for i in range(len(stack)-1, -1, -1):
            while outPut and stack[i] >= stack[outPut[-1]]:
                outPut.pop()
                    
            if outPut:
                last[i] = stack[outPut[-1]]
            outPut.append(i)
                
        return last
                        
