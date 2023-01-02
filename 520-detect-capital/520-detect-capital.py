class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        stack = []
        
        for i in word:
            
            if len(stack) >= 2 and ((stack[-1] > 90 and ord(i) <= 90) or (stack[-1] <= 90 and ord(i) > 90)):
                return False
            else:
                if stack and (stack[-1] > 90 and ord(i) <= 90):
                    return False
                stack.append(ord(i))
            
        return True