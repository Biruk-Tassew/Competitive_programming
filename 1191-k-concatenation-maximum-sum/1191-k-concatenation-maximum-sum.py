class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        if k == 1:
            ans = 0
            cur = 0
            for i in arr:
                if i >= 0:
                    cur += i
                    ans = max(ans, cur)
                else:
                    ans = max(ans, cur)
                    cur = 0
                    
            return ans
        
        init_sum = sum(arr)
        if init_sum > 0:
            return (self.solve(arr*2)+(k-2)*init_sum)%(10**9 + 7)
        
        return self.solve(arr*2)%(10**9 + 7)
    
    def solve(self, arr):
        dp = [0]
        max_num = 0
        
        for i in range(1, len(arr)+1):
            dp.append(max(0, dp[i-1]+arr[i-1]))
            max_num = max(max_num, dp[i])
            
        return max_num%(10**9 + 7)
        