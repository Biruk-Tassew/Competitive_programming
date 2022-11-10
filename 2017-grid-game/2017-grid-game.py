class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        pre_one = [0]*len(grid[0])
        pre_two = [0]*len(grid[0])
        pre_one[-1] = grid[0][-1]
        pre_two[-1] = grid[1][-1]
        
        for i in range(len(grid[0])-2, -1, -1):
            pre_one[i] = pre_one[i+1] + grid[0][i]
            pre_two[i] = pre_two[i+1] + grid[1][i]

        ans = 0
        print(pre_one, pre_two)
        for i in range(len(grid[0])-1):
            if pre_one[i+1] < pre_two[0]-pre_two[i+1]:
                return max(pre_one[i+1], pre_two[0]-pre_two[i])
            
        return pre_two[0]-pre_two[-1]