class Solution:
    def reverse(self, x: int) -> int:
        
        ans = 0
        num_len = len(str(x))
        pos_num = abs(x)
        while pos_num:
            ans *= 10
            ans += (pos_num%10)
            pos_num //= 10
            if ans > (2**31 -1):
                return 0
            
        if x < 0:
            return -1*ans
        return ans