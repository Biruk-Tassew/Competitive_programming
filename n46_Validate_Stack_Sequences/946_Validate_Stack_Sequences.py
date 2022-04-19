class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        for i in pushed:
            stack.append(i)  
            if i == popped[0]:
                popped.remove(popped[0]) 
                stack.pop() 
            while stack and stack[-1] == popped[0]:
                popped.remove(popped[0]) 
                stack.pop()
                
        return stack==[
