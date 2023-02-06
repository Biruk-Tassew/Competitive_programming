class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first = [nums[i] for i in range(n)]
        later = [nums[i] for i in range(n, 2*n)]
        
        i_f = 0
        i_l = 0
        while i_f < (2*n - 1):
            nums[i_f] = first[i_l]
            i_f += 1
            nums[i_f] = later[i_l]
            
            i_f += 1
            i_l += 1
            
        return nums