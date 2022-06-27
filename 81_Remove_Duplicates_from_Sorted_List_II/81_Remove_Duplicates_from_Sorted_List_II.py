class ListNode:

    def __init__(self, val=0, next = None):

        self.val = val

        self.next = next

class Solution:

    def deleteDuplicates(self, head:ListNode) -> ListNode:

        temp = ListNode()

        prev = temp

        curr = head

        stack = []

        while curr:

            if stack and curr.val != stack[-1].val:

                if len(stack) == 1:

                    prev.next = stack.pop()

                    prev = prev.next

                else:

                    stack = []

            stack.append(curr)

            curr = curr.next

        if len(stack) == 1:

            prev.next = stack.pop()

        elif len(stack) > 1:

            prev.next = None

        return temp.next

