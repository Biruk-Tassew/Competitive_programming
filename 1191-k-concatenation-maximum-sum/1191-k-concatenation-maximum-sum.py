class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        if k == 1:
            return self.solve(arr)
        
        init_sum = sum(arr)
        if init_sum > 0:
            return (self.solve(arr*2)+(k-2)*init_sum)%(10**9 + 7)
        
        return self.solve(arr*2)%(10**9 + 7)
    
    def solve(self, arr):
        cur_sum = 0
        max_num = 0
        
        for i in range(1, len(arr)+1):
            cur_sum = max(0, cur_sum+arr[i-1])
            max_num = max(max_num, cur_sum)
            
        return max_num%(10**9 + 7)
        