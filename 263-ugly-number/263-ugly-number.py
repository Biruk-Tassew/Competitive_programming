class Solution:
    def isUgly(self, n: int) -> bool:
        ugly_list = [2, 3, 5]
        ugly_idx = 0
        
        while n and ugly_idx < 3:
            if not n % ugly_list[ugly_idx]:
                n //= ugly_list[ugly_idx]
            else:
                ugly_idx += 1
        
        return n==1