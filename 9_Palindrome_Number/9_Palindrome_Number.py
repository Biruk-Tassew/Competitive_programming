class Solution:
    def isPalindrome(self, x: int) -> bool:
      
    
        
        y = x
        r = 0
        while y > 0:
            r = r * 10 + (y%10)
            y = y // 10
            
        return x == r
            
        
        
        
