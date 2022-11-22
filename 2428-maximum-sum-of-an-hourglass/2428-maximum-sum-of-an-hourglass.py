class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_sum = 0
        cur_sum = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row+2 < len(grid) and col+2 < len(grid[0]):
                    cur_sum = sum(grid[row][col: col+3])
                    cur_sum += sum(grid[row+2][col: col+3])
                    cur_sum += grid[row+1][col+1]
                    
                max_sum = max(max_sum , cur_sum)
            
        return max_sum