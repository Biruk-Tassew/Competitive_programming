# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return ListNode([]).next
        else:
            if not list1:
                return list2
            elif not list2:
                return list1 
                
        if list1.val > list2.val:
            temp = ListNode(list2.val)
            list2 = list2.next
        else:
            temp = ListNode(list1.val)
            list1 = list1.next
        outPut = temp
        
        while list1 and list2:
            
            if list1.val > list2.val:
                temp.next = ListNode(list2.val)
                list2 = list2.next
                
            else:
                print(temp)
                temp.next = ListNode(list1.val)
                list1 = list1.next
            temp = temp.next
            
        while list1:
            temp.next = ListNode(list1.val)
            list1 = list1.next
            temp = temp.next
        while list2:
            temp.next = ListNode(list2.val)
            list2 = list2.next
            temp = temp.next
            
        
        return outPut
        
