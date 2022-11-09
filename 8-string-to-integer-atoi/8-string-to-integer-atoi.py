class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not len(s):
            return 0
        res = 0
        sign = 1
        idx = 0
        
        if s[0] == "-" or s[0] == "+":
            if s[0] == "-":
                sign =-1
            idx += 1
    
        while idx < len(s) and s[idx].isdigit():
            res *= 10
            res += int(s[idx])
            idx += 1
                        
        return max(-2**31, min(sign * res,2**31-1))
                