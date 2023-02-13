class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        if len(a) < len(b):
            a = '0'*(len(b) - len(a)) + a
        else:
            b = '0'*(len(a) - len(b)) + b
        
        a = [int(i) for i in a]
        b = [int(i) for i in b]
        
        count = 0
        
        for i in range(len(a)-1,-1,-1):
            count, a[i] = divmod(a[i]+b[i]+count,2)
            
            
        
        if count:
             a = [count] + a
        
        return ''.join([str(i) for i in a])