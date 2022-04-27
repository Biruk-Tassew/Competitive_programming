class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        size = len(num)
        if size == k: 
            return '0'
        
        digitStack = []
        for i in num:
            
            while digitStack and k and digitStack[-1] > int(i):
                digitStack.pop()
                k -= 1
                
            digitStack.append(int(i))
            
        while k and len(digitStack) > 1:
            digitStack.pop()
            k -= 1
            
        while digitStack[0] == 0 and len(digitStack) > 1:
            digitStack.remove(digitStack[0])
            
        return ''.join(map(str,digitStack))
