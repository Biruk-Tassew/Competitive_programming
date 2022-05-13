# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        temp = ListNode(head.val)
        head = head.next
        outPut = temp
        while head:
            print(head.val, temp.val)
            if head.val == temp.val:
                print(not head.next)
                if True:
                    print("here")
                    temp.next = head.next
                head = head.next
            else:
                temp.next = head
                head = head.next
                temp = temp.next
                
        return outPut
                        
