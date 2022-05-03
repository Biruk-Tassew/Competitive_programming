class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def check(num):
            if num == 4 or num == 1:
                return True
            elif num%4 != 0 or num == 0:
                return False
            
            return check(num/4)
        
        return check(n)
