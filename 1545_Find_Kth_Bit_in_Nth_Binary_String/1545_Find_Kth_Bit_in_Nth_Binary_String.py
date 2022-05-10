class Solution:
    outPut = '0'
    def invert(self, n):
        newN = ""
        for i in range(len(str(n))):
            newN += str(1 - int(str(n)[i]))
        return newN
            
    def find(self, n, k):
        if n == 1:
            return 
        
        self.outPut = self.outPut + "1" + self.invert(self.outPut)[::-1]
        n -= 1
        return self.find(n, k)
    def findKthBit(self, n: int, k: int) -> str:
        self.find(n, k)
        return self.outPut[k-1]
    
    
        
        
        
