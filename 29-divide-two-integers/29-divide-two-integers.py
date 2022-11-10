class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1
        dr = abs(divisor)
        dd = abs(dividend)
        cnt = 0
        while dd >= dr:
            cur_dr = dr
            cur_cnt = 1
            while cur_dr << 1 <= dd:
                cur_dr <<= 1
                cur_cnt <<= 1
                
            dd -= cur_dr
            cnt += cur_cnt
           
            
        return max(-2**31, min(sign*cnt, 2**31 - 1))
            
            
                