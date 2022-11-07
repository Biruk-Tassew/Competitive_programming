class Solution:
    def maximum69Number (self, num: int) -> int:
        factor = 10**len(str(num))
        ans = 0
        flag = 1
        
        while factor:
            if flag and num//factor == 6:
                ans += 9*factor
                flag = 0
            else:
                ans += (num//factor)*factor
                
            num %= factor
            factor //= 10
            
                
        return ans