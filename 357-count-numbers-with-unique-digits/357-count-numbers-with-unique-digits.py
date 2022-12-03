class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        self.nums = [i for i in range(10)]
        self.res = 0
        self.backtrack([], -1, n)
        return self.res
    
    def backtrack(self, cur_digs, prev_num, n):
        if cur_digs and cur_digs[0] == 0:
            return 
        
        if len(cur_digs) < n:
            self.res += 1
            
        if len(cur_digs) == n:
            self.res += 1
            return 
        
        for i in range(len(self.nums)):
            temp = self.nums[i]
            cur_digs.append(temp)
            self.nums.remove(temp)
            
            self.backtrack(cur_digs, i, n)
            
            self.nums.insert(i, temp)
            cur_digs.pop()