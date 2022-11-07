class Solution:
    def maximum69Number (self, num: int) -> int:
        
        temp_num = num
        six_idx = -1
        idx = 0
        while temp_num:
            if temp_num%10 == 6:
                six_idx = idx
                
            idx += 1
            temp_num //= 10
            
        if six_idx == -1:
            return num
        
        return num + 3*(10**six_idx)