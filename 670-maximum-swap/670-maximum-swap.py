class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        
        for i in range(len(num)):
            cur_max = max(num[i:])
            
            if cur_max != num[i]:
                
                for j in range(len(num)-1, i, -1):
                    if num[j] == cur_max:
                        num[i], num[j] = num[j], num[i]
                        break
                        
                break
                    
        return int("".join(num))