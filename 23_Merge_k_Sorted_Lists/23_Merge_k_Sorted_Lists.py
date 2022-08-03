# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        for i in lists:
            temp = i
            while temp:
                heapq.heappush(heap, temp.val)
                temp = temp.next
        if not heap:
            return None
        
        head = ListNode(heapq.heappop(heap))
        cur = head
        while heap:
            cur.next = ListNode(heapq.heappop(heap))
            cur = cur.next
            
        return head
