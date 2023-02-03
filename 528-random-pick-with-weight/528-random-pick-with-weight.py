class Solution:

    def __init__(self, w: List[int]):
        for i in range(1, len(w)):
            w[i] += w[i-1] 
        self.weight = w
        

    def pickIndex(self) -> int:
        rand_w = random.randint(0, self.weight[-1]-1)
        left = 0
        right = len(self.weight)-1
        
        while left <= right:
            mid = (left + right)//2
            
            if self.weight[mid] > rand_w:
                right = mid - 1
            else:
                left = mid + 1
                
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()