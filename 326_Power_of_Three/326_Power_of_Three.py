class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        def check(num):
            
            if num == 3 or num== 1:
                return True
            
            elif (num%3) != 0 or num == 0:
                return False
            
            return check(num/3)
        
        return check(n)
